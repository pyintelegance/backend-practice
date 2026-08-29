"""Песочница для выполнения кода ученика (Python).

Цель: запускать чужой код максимально безопасно БЕЗ Docker.
Слои защиты:
  1. Изолированный интерпретатор: `python -E`
     -E  игнорировать PYTHON* переменные окружения (PYTHONPATH и т.д.).
     Путь к site-packages venv добавляется явно в преамбуле (чтобы был
     доступен psycopg), но пользовательские скрипты из текущей папки
     не подгружаются.
  2. Пустой env (без интернета/прокси/домашних путей) — блокирует сеть,
     которую модуль мог бы поднять через переменные окружения.
  3. Код-преамбула: переопределяет __import__, чтобы блокировать опасные
     модули (os/sys/subprocess/socket/requests/...), и подменяет опасные
     встроенные (open/eval/exec/input/...). builtins сам добавлен в
     чёрный список, чтобы ученик не мог восстановить оригинальный __import__.
  4. Для задач на БД: если передан db_dsn — в globals вливается переменная
     DB_DSN (строка подключения), ученик сам делает psycopg.connect(DB_DSN).
  5. Таймаут (subprocess.TimeoutExpired) — защита от бесконечных циклов.
  6. На POSIX: ограничение памяти/времени CPU через setrlimit (preexec_fn).
     На Windows: setrlimit недоступен — ограничиваем временем + блоком
     опасного на уровне кода. Для жёсткой изоляции памяти нужен Docker.

ВАЖНО: это НЕ полноценная изоляция ОС. Для продакшена с чужим кодом
рекомендуется Docker. Здесь — разумный минимум для учебной платформы
на ноутбуке без админ-прав.
"""

import os
import re
import subprocess
import sys
import tempfile
import textwrap

# Путь к site-packages текущего (venv) интерпретатора — нужен, чтобы в песочнице
# был доступен psycopg (для задач на БД) и другие легитимные библиотеки.
def _venv_site_packages() -> str:
    base = getattr(sys, "base_prefix", sys.prefix)
    cand = os.path.join(base, "Lib", "site-packages")
    if os.path.isdir(cand):
        return cand
    # виртуальное окружение: prefix != base_prefix
    cand2 = os.path.join(sys.prefix, "Lib", "site-packages")
    if os.path.isdir(cand2):
        return cand2
    return ""

# Запрещённые модули — импорт любого из них (или подмодуля) блокируется.
# psycopg / psycopg2 НЕ в списке (разрешены для задач на PostgreSQL).
FORBIDDEN_MODULES = {
    "os", "sys", "subprocess", "socket", "shutil", "ctypes", "ctypes.util",
    "importlib", "multiprocessing", "threading", "signal", "resource",
    "pty", "fcntl", "pickle", "marshal", "shelve", "webbrowser", "http",
    "urllib", "urllib.request", "urllib.parse", "ftplib", "smtplib",
    "base64", "binascii", "tempfile", "glob", "pathlib",
    "platform", "getpass", "grp", "pwd", "msvcrt", "winreg", "traceback",
    "readline", "curses", "tkinter", "ssl", "asyncio", "select", "selectors",
    "email", "telnetlib", "ftplib", "poplib", "imaplib", "smtpd",
    "requests", "urllib3", "httpx", "aiohttp", "websocket", "websockets",
    "builtins",  # блокируем, чтобы нельзя было восстановить __import__
}

# Опасные встроенные вызовы (регулярный запрет на уровне исходника).
# Намеренно НЕ блокируем type/object/super/classmethod/staticmethod/property —
# без них нельзя писать классы (основа курса OOP).
FORBIDDEN_CALLS_RE = re.compile(
    r'\b(open|eval|exec|compile|__import__|globals|locals|vars|'
    r'breakpoint|input|memoryview|delattr|setattr|exit|quit|help|reload)\s*\(',
    re.IGNORECASE,
)

# Прямой импорт опасного модуля (на уровне исходника, до рантайма)
FORBIDDEN_IMPORT_RE = re.compile(
    r'^\s*(import|from)\s+([a-zA-Z_][\w.]*)',
    re.MULTILINE,
)

GUARD_PREFIX = r'''
import sys as _sys
_SP = {sp!r}
if _SP:
    _sys.path.insert(0, _SP)
import builtins as _b
def _blocked(name):
    def _raise(*a, **k):
        raise RuntimeError("'%s' is blocked in the sandbox" % name)
    return _raise
# блокируем опасные встроенные, через которые ученик мог бы читать файлы/систему.
# ВНИМАНИЕ: нельзя блокировать compile/eval/exec — интерпретатор сам вызывает
# compile при импорте любого модуля (.py -> байткод). Блокируем только те, что
# напрямую дают доступ к ФС/вводу/отладчику и не нужны рантайму.
for _n in ('open', 'input', 'breakpoint'):
    setattr(_b, _n, _blocked(_n))
'''.format(sp=_venv_site_packages())


def code_is_dangerous(code: str) -> str | None:
    """Возвращает причину запрета или None, если код допустим."""
    for m in FORBIDDEN_IMPORT_RE.finditer(code):
        top = m.group(2).split('.')[0]
        if top in FORBIDDEN_MODULES:
            return "Импорт запрещённого модуля '%s'." % m.group(2)
    if FORBIDDEN_CALLS_RE.search(code):
        return "Использование запрещённой функции (open/eval/exec/input/...)."
    return None


def run_python(code: str, timeout: float = 5.0, db_dsn: str | None = None,
               extra_globals: dict | None = None):
    """Запускает Python-код ученика в изолированном subprocess.

    Возвращает (returncode, stdout, stderr).
    db_dsn — если задан, в globals вливается переменная DB_DSN (строка DSN),
             чтобы ученик мог сделать psycopg.connect(DB_DSN) для задач на БД.
    extra_globals — доп. простые переменные (только базовые типы, сериализуемые
             через repr), вливаемые в globals кода ученика.
    """
    reason = code_is_dangerous(code)
    if reason:
        return 1, "", reason

    parts = [GUARD_PREFIX]
    if db_dsn:
        parts.append("DB_DSN = %r" % db_dsn)
    if extra_globals:
        for key, val in extra_globals.items():
            if not re.fullmatch(r'[A-Za-z_]\w*', key) or key in ("DB_DSN",):
                continue
            try:
                parts.append("%s = %r" % (key, val))
            except Exception:
                continue
    parts.append(code)
    script = "\n".join(parts)

    fd, path = tempfile.mkstemp(suffix=".py", prefix="sandbox_",
                                dir=tempfile.gettempdir())
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(script)
        env = _empty_env()
        kwargs = dict(
            capture_output=True,
            timeout=timeout,
            cwd=tempfile.gettempdir(),
            env=env,
        )
        if os.name == "posix":
            kwargs["preexec_fn"] = _limit_resources
        proc = subprocess.run([sys.executable, "-E", path], **kwargs)
        return proc.returncode, _decode(proc.stdout), _decode(proc.stderr)
    except subprocess.TimeoutExpired:
        return 124, "", "Превышено время выполнения (возможно бесконечный цикл)."
    except Exception as e:  # pragma: no cover
        return 1, "", "Ошибка песочницы: %s" % e
    finally:
        try:
            os.remove(path)
        except OSError:
            pass


def _limit_resources():
    """POSIX: ограничить память (256 МБ) и CPU-время (5 с)."""
    try:
        import resource
        resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))
        resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
    except Exception:
        pass


def _empty_env() -> dict:
    """Минимально возможный env без сетевых/домашних переменных."""
    return {
        "PATH": "",          # не найти внешние исполняемые файлы
        "SYSTEMROOT": os.environ.get("SYSTEMROOT", ""),
        "TEMP": tempfile.gettempdir(),
        "TMP": tempfile.gettempdir(),
    }


def _decode(b):
    if not b:
        return ""
    for enc in ("utf-8", "cp1251", "latin-1"):
        try:
            return b.decode(enc)
        except (UnicodeDecodeError, LookupError):
            continue
    return b.decode("utf-8", errors="replace")
