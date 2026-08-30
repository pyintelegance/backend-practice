#!/usr/bin/env bash
set -o errexit

echo "==> Install deps"
pip install -r requirements.txt

echo "==> Collect static"
python manage.py collectstatic --noinput

echo "==> Ensure Django DB exists (separate logical DB in the shared Postgres instance)"
if [ -n "$DATABASE_URL" ]; then
  python - <<'PY'
import os, psycopg, urllib.parse
url = os.environ["DATABASE_URL"]
u = urllib.parse.urlparse(url)
dbname = u.path.lstrip("/") or "ustudy_practice"
admin = url.replace(f"/{dbname}", "/postgres")
try:
    with psycopg.connect(admin, autocommit=True) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
            if cur.fetchone() is None:
                cur.execute(f'CREATE DATABASE "{dbname}"')
                print(f"created database {dbname}")
            else:
                print(f"database {dbname} already exists (skipped)")
except Exception as e:
    print("django db ensure skipped:", e)
PY
fi

echo "==> Migrate Django DB"
python manage.py migrate --noinput

echo "==> Seed tasks (demo + real workbook)"
python manage.py seed_data || echo "seed_data skipped/failed (non-fatal)"

echo "==> Seed frontend tasks (HTML, CSS, JavaScript)"
python manage.py seed_frontend || echo "seed_frontend skipped/failed (non-fatal)"

echo "==> Ensure dvdrental DB exists for student tasks"
# DVDRENTAL_DATABASE_URL указывает на ту же СУБД, но отдельную БД.
# Если БД dvdrental ещё нет — создаём и заливаем дамп.
if [ -n "$DVDRENTAL_DATABASE_URL" ]; then
  python - <<'PY'
import os, psycopg, urllib.parse
url = os.environ["DVDRENTAL_DATABASE_URL"]
u = urllib.parse.urlparse(url)
dbname = u.path.lstrip("/") or "dvdrental"
admin = url.replace(f"/{dbname}", "/postgres")
dump = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dvdrental_dump.sql")
try:
    with psycopg.connect(admin, autocommit=True) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
            exists = cur.fetchone() is not None
        if not exists:
            with conn.cursor() as cur:
                cur.execute(f'CREATE DATABASE "{dbname}"')
            print(f"created database {dbname}")
            # заливаем дамп (схема + данные) в свежесозданную БД
            if os.path.exists(dump):
                with open(dump, encoding="utf-8") as f:
                    sql = f.read()
                with psycopg.connect(url, autocommit=True) as dconn:
                    dconn.execute(sql)
                print("dvdrental dump loaded")
            else:
                print("dvdrental_dump.sql not found, skipped load")
        else:
            print(f"database {dbname} already exists (dump not reloaded)")
except Exception as e:
    print("dvdrental setup skipped:", e)
PY
fi

echo "==> Build done"
