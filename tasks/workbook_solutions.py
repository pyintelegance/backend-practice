"""Эталонные решения задач из Python+PostgreSQL воркбука (dvdrental).

Каждое решение — это корректный код ученика (использует DB_DSN, который
песочница вливает в globals). Мы прогоняем их на реальной dvdrental, чтобы
зафиксировать ожидаемый вывод, и сравниваем с выводом ученика.

Ключ задачи -> (reference_code, expected_markers)
- expected_markers: список подстрок, которые ДОЛЖНЫ быть в выводе (мягкая проверка)
  либо точный вывод (если детерминирован).
"""

# 1. Подключение
SOL_1 = """import psycopg
conn = psycopg.connect(DB_DSN)
print("Database connected")
conn.close()
"""

# 2. Cursor + SELECT 1
SOL_2 = """import psycopg
conn = psycopg.connect(DB_DSN)
with conn.cursor() as cur:
    cur.execute("SELECT 1")
    print(cur.fetchone()[0])
conn.close()
"""

# 3. Один актёр
SOL_3 = """import psycopg
conn = psycopg.connect(DB_DSN)
actor_id = 1
with conn.cursor() as cur:
    cur.execute("SELECT first_name, last_name FROM actor WHERE actor_id = %s", (actor_id,))
    row = cur.fetchone()
    print(row[0], row[1])
conn.close()
"""

# 4. Все категории
SOL_4 = """import psycopg
conn = psycopg.connect(DB_DSN)
with conn.cursor() as cur:
    cur.execute("SELECT category_id, name FROM category ORDER BY category_id")
    rows = cur.fetchall()
    print(rows)
conn.close()
"""

# 5. Поиск фильма по названию (реальное значение в dvdrental: "Academy Dinosaur")
SOL_5 = """import psycopg
conn = psycopg.connect(DB_DSN)
title = "Academy Dinosaur"
with conn.cursor() as cur:
    cur.execute("SELECT title, description FROM film WHERE title = %s", (title,))
    row = cur.fetchone()
    print(row)
conn.close()
"""

# 6. Фильмы дороже заданного
SOL_6 = """import psycopg
conn = psycopg.connect(DB_DSN)
min_rate = 3.0
with conn.cursor() as cur:
    cur.execute("SELECT title, rental_rate FROM film WHERE rental_rate > %s ORDER BY rental_rate DESC", (min_rate,))
    for r in cur.fetchall():
        print(r[0], r[1])
conn.close()
"""

# 7. Добавить актёра
SOL_7 = """import psycopg
conn = psycopg.connect(DB_DSN)
first_name = 'ALI'
last_name = 'VALIYEV'
with conn.cursor() as cur:
    cur.execute("INSERT INTO actor (first_name, last_name) VALUES (%s, %s)", (first_name, last_name))
    conn.commit()
    print("actor yaratildi")
conn.close()
"""

# 8. INSERT ... RETURNING actor_id
SOL_8 = """import psycopg
conn = psycopg.connect(DB_DSN)
with conn.cursor() as cur:
    cur.execute("INSERT INTO actor (first_name, last_name) VALUES (%s, %s) RETURNING actor_id", ('NEW', 'ACTOR'))
    new_id = cur.fetchone()[0]
    conn.commit()
    print("Yangi actor_id", new_id)
conn.close()
"""

# 9. Обновить имя актёра
SOL_9 = """import psycopg
conn = psycopg.connect(DB_DSN)
actor_id = 201
new_name = 'JACK'
with conn.cursor() as cur:
    cur.execute("UPDATE actor SET first_name = %s WHERE actor_id = %s", (new_name, actor_id))
    conn.commit()
    print(cur.rowcount, "row updated")
conn.close()
"""

# 10. Удалить актёра
SOL_10 = """import psycopg
conn = psycopg.connect(DB_DSN)
actor_id = 201
with conn.cursor() as cur:
    try:
        cur.execute("DELETE FROM actor WHERE actor_id = %s", (actor_id,))
        conn.commit()
        print("deleted")
    except psycopg.IntegrityError:
        conn.rollback()
        print("cannot delete")
conn.close()
"""

# 11. Full name клиента
SOL_11 = """import psycopg
conn = psycopg.connect(DB_DSN)
customer_id = 10
with conn.cursor() as cur:
    cur.execute("SELECT first_name, last_name FROM customer WHERE customer_id = %s", (customer_id,))
    fn, ln = cur.fetchone()
    print("Full Name:", fn, ln)
conn.close()
"""

# 12. Film + category JOIN
SOL_12 = """import psycopg
conn = psycopg.connect(DB_DSN)
film_id = 5
with conn.cursor() as cur:
    cur.execute(
        "SELECT f.title, c.name FROM film f "
        "JOIN film_category fc ON f.film_id = fc.film_id "
        "JOIN category c ON fc.category_id = c.category_id WHERE f.film_id = %s",
        (film_id,))
    row = cur.fetchone()
    print(row[0], row[1])
conn.close()
"""

# 13. Сумма платежей клиента
SOL_13 = """import psycopg
conn = psycopg.connect(DB_DSN)
customer_id = 1
with conn.cursor() as cur:
    cur.execute("SELECT SUM(amount) FROM payment WHERE customer_id = %s", (customer_id,))
    total = cur.fetchone()[0]
    print("total_amount", total)
conn.close()
"""


# Детерминированные задачи (точное сравнение после нормализации)
EXACT_SOLS = {
    1: SOL_1,
    2: SOL_2,
    3: SOL_3,
    4: SOL_4,
    11: SOL_11,
    12: SOL_12,
    13: SOL_13,
}

# Маркерные задачи (вывод должен содержать подстроки)
MARKER_SOLS = {
    5: (SOL_5, ["ACADEMY DINOSAUR"]),
    6: (SOL_6, [""]),  # просто непустой вывод
    7: (SOL_7, ["actor yaratildi"]),
    8: (SOL_8, ["Yangi actor_id"]),
    9: (SOL_9, ["row updated"]),
    10: (SOL_10, ["deleted", "cannot delete"]),
}

ALL_SOLS = {**EXACT_SOLS, **MARKER_SOLS}
