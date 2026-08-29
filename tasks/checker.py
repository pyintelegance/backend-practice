"""Автопроверка решений учеников.

SQL: запрос выполняется на read-only БД в транзакции с ROLLBACK,
результат сравнивается с результатом правильного запроса.
Python: код запускается в подпроцессе с таймаутом и запретом опасных импортов,
stdout сравнивается с ожидаемым.
"""

import re
import textwrap
import time

import psycopg
from django.conf import settings

from .models import Task
from .sandbox import run_python


# Запрещённые конструкции в SQL (только чтение данных)
FORBIDDEN_SQL = re.compile(
    r'\b(insert|update|delete|drop|alter|create|truncate|grant|revoke|'
    r'copy|vacuum|reindex|set|reset|call|do|listen|notify|'
    r'pg_|lo_import|lo_export|copy)\b',
    re.IGNORECASE,
)

# Опасные импорты/вызовы Python теперь проверяются в tasks/sandbox.py
# (на уровне исходника + в рантайме через guarded_import). Здесь не дублируем.
def _strip_result(rows):
    """Приводим результат к сравнимому виду: список строк с нормализованными пробелами (без учёта регистра)."""
    norm = []
    for row in rows:
        values = []
        for v in row:
            if v is None:
                values.append('')
            else:
                values.append(str(v).strip().lower())
        norm.append('|'.join(values).strip())
    return norm


def _normalize_output(s):
    """Нормализация текста перед сравнением: убираем переносы/лишние пробелы и регистр."""
    s = s.strip()
    s = s.replace('\r\n', '\n').replace('\r', '\n')
    s = re.sub(r'[ \t]+', ' ', s)
    return s


def _norm_key(s):
    return _normalize_output(s).lower()


def check_sql(code, task):
    """Выполняет запрос ученика и правильный запрос на read-only БД, сравнивает результаты.

    Если task.allow_write=True — разрешены UPDATE/INSERT/DELETE (транзакционные задачи),
    но всё выполняется в транзакции, которая в конце откатывается.
    """
    allow_write = task.allow_write

    if not allow_write and FORBIDDEN_SQL.search(code):
        return False, (
            'Запрос содержит запрещённые операции. Разрешены только SELECT-запросы '
            '(чтение данных).'
        ), {'student': '', 'expected': '', 'error': 'forbidden'}

    db_config = _db_config()

    try:
        with psycopg.connect(**db_config) as conn:
            if allow_write:
                # Ученик сам пишет BEGIN/UPDATE/COMMIT — выполняем как есть,
                # в конце откатываем, чтобы не менять данные.
                cur = conn.cursor()
                cur.execute(code)
                conn.rollback()
                return True, 'Транзакция выполнена без ошибок.', {'student': '', 'expected': '', 'error': ''}

            with conn.transaction():
                cur = conn.cursor()
                cur.execute(code)
                try:
                    student_rows = cur.fetchall()
                except psycopg.ProgrammingError:
                    student_rows = []

            with conn.transaction():
                cur = conn.cursor()
                cur.execute(task.solution)
                expected_rows = cur.fetchall()
    except psycopg.Error as e:
        return False, f'Ошибка выполнения запроса:\n{e}', {'student': '', 'expected': '', 'error': str(e)}
    except Exception as e:
        return False, f'Непредвиденная ошибка:\n{e}', {'student': '', 'expected': '', 'error': str(e)}

    student_norm = _strip_result(student_rows)
    expected_norm = _strip_result(expected_rows)

    student_preview = '\n'.join(student_norm[:15]) or '(пусто)'
    expected_preview = '\n'.join(expected_norm[:15]) or '(пусто)'

    if student_norm == expected_norm:
        return True, 'Правильно! Результат совпадает с ожидаемым.', {'student': student_preview, 'expected': expected_preview}

    return False, (
        f'Результат не совпадает.\n\n'
        f'Твой вывод:\n{student_preview}\n\n'
        f'Ожидалось:\n{expected_preview}'
    ), {'student': student_preview, 'expected': expected_preview}


def _db_dsn():
    """DSN для подключения к dvdrental из песочницы (для задач на БД).

    В проде (Render) берётся из DVDRENTAL_DATABASE_URL, иначе строится из
    настроек Django-БД (локально dvdrental лежит в той же СУБД).
    """
    dvd_url = getattr(settings, 'DVDRENTAL_DATABASE_URL', '')
    if dvd_url:
        from urllib.parse import urlparse
        u = urlparse(dvd_url)
        host = u.hostname or 'localhost'
        port = u.port or 5432
        dbname = u.path.lstrip('/') or 'dvdrental'
        user = u.username or 'postgres'
        password = u.password or ''
        return (
            f"host={host} port={port} dbname={dbname} "
            f"user={user} password={password}"
        )
    return (
        f"host={settings.DATABASES['default']['HOST']} "
        f"port={settings.DATABASES['default']['PORT']} "
        f"dbname=dvdrental "
        f"user={settings.DATABASES['default']['USER']} "
        f"password={settings.DATABASES['default']['PASSWORD']}"
    )


def _db_config():
    """Конфиг psycopg.connect() для SQL-проверки (использует ту же БД, что и песочница)."""
    dsn = _db_dsn()
    # DSN → kwargs
    cfg = {}
    for part in dsn.split():
        if '=' in part:
            k, v = part.split('=', 1)
            cfg[k] = v
    return cfg


def check_python(code, task):
    """Запускает Python-код ученика в изолированной песочнице и сравнивает stdout с эталоном.

    Для задач на PostgreSQL (task.task_type == PYTHON и task.db_name задан) в globals
    вливается DB_DSN — строка подключения к dvdrental, ученик сам делает
    psycopg.connect(DB_DSN). Это безопасно: в песочнице заблокированы os/sys/subprocess/
    socket и т.д., а пустой env не даёт доступа к сети в обход.
    """
    # Проверка обязательных элементов (защита от «просто подставить ответ»)
    if task.required_tokens:
        tokens = [t.strip() for t in task.required_tokens.split(',') if t.strip()]
        missing = []
        for t in tokens:
            if re.fullmatch(r'[A-Za-z0-9_]+', t):
                found = re.search(r'\b' + re.escape(t) + r'\b', code)
            else:
                found = t in code
            if not found:
                missing.append(t)
        if missing:
            return False, (
                f'Похоже, ты просто подставил ответ, а не вычислил его.\n'
                f'В коде должно использоваться: {", ".join(missing)}.'
            ), {'student': '', 'expected': '', 'error': 'missing_tokens'}

    # Если задача требует БД — передаём DSN; иначе None
    db_dsn = _db_dsn() if task.db_name else None

    rc, out, err = run_python(code, timeout=5, db_dsn=db_dsn)
    if rc != 0:
        msg = err.strip() or '(без сообщения)'
        return False, f'Ошибка выполнения:\n{msg}', {'student': '', 'expected': '', 'error': msg}

    student_out = out.strip()

    # Если есть эталонное решение — сверяем вывод ученика с выводом эталона
    # (это покрывает и точные, и маркерные задачи из воркбука).
    if task.reference_solution and task.reference_solution.strip():
        rc_ref, out_ref, err_ref = run_python(task.reference_solution, timeout=5, db_dsn=db_dsn)
        if rc_ref != 0:
            # эталон сломан — падаем на обычную сверку с task.solution
            expected_out = textwrap.dedent(task.solution).strip()
        else:
            expected_out = out_ref.strip()
    else:
        expected_out = textwrap.dedent(task.solution).strip()

    # Нестрогое сравнение: регистр и лишние пробелы/переносы не важны
    if _norm_key(student_out) == _norm_key(expected_out):
        return True, 'Правильно! Вывод совпадает с ожидаемым.', {'student': student_out, 'expected': expected_out}

    return False, (
        f'Вывод не совпадает.\n\n'
        f'Твой вывод:\n{student_out or "(пусто)"}\n\n'
        f'Ожидалось:\n{expected_out}'
    ), {'student': student_out or '(пусто)', 'expected': expected_out}


def check(task, code):
    """Точка входа: возвращает (passed: bool, feedback: str, result: dict)."""
    start = time.time()
    if task.task_type == Task.Type.SQL:
        passed, feedback, result = check_sql(code, task)
    else:
        passed, feedback, result = check_python(code, task)
    elapsed = time.time() - start
    return passed, feedback, result, elapsed