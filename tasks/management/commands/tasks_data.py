# -*- coding: utf-8 -*-
"""Библиотека задач для автопроверки. ~100 задач по Python, SQL и транзакциям.

Подсказки (hint) — наводящие: объясняют ПОДХОД, не дают готовый код/ответ.
"""

from tasks.models import Task


def build_python_tasks():
    """Простые Python-задачи (уровень 1): вывод на печать."""
    items = [
        ('Приветствие', 'python-hello', 'Напиши программу, которая выводит слово Hello.',
         'Выход:\nHello', 'Hello', 'В Python текст выводится функцией print().'),
        ('Сложение чисел', 'python-add', 'Выведи сумму чисел 7 и 3.',
         'Выход:\n10', '10', 'Сложение чисел выполняется оператором +.'),
        ('Вычитание', 'python-sub', 'Выведи результат вычитания 10 минус 4.',
         'Выход:\n6', '6', 'Вычитание — оператор -.'),
        ('Умножение', 'python-mul', 'Выведи произведение 6 и 7.',
         'Выход:\n42', '42', 'Умножение — оператор *.'),
        ('Деление', 'python-div', 'Выведи результат деления 20 на 5.',
         'Выход:\n4.0', '4.0', 'Деление — оператор / (даёт дробное число).'),
        ('Целочисленное деление', 'python-floordiv', 'Выведи целую часть от деления 17 на 5.',
         'Выход:\n3', '3', 'Целочисленное деление — оператор // (отбрасывает дробную часть).'),
        ('Остаток от деления', 'python-mod', 'Выведи остаток от деления 17 на 5.',
         'Выход:\n2', '2', 'Остаток от деления — оператор % (модуль).'),
        ('Степень', 'python-pow', 'Выведи 2 в степени 10.',
         'Выход:\n1024', '1024', 'Возведение в степень — оператор **.'),
        ('Строка из числа', 'python-str-num', 'Выведи число 42 как текст.',
         'Выход:\n42', '42', 'Функция str() превращает число в строку.'),
        ('Длина строки', 'python-len', 'Выведи длину слова Python.',
         'Выход:\n6', '6', 'Длина строки — функция len().'),
        ('Верхний регистр', 'python-upper', 'Выведи слово hello заглавными буквами.',
         'Выход:\nHELLO', 'HELLO', 'У строк есть метод upper() — превращает буквы в заглавные.'),
        ('Нижний регистр', 'python-lower', 'Выведи слово WORLD строчными буквами.',
         'Выход:\nworld', 'world', 'У строк есть метод lower() — превращает буквы в строчные.'),
        ('Конкатенация', 'python-concat', 'Соедини строки "Py" и "thon" и выведи.',
         'Выход:\nPython', 'Python', 'Строки соединяются оператором + (конкатенация).'),
        ('Умножение строки', 'python-str-mul', 'Выведи строку "ab", повторённую 3 раза.',
         'Выход:\nababab', 'ababab', 'Строку можно умножить на число — она повторится.'),
        ('Строка и число', 'python-str-int', 'Выведи строку "Ответ: " и число 42.',
         'Выход:\nОтвет: 42', 'Ответ: 42', 'print() может принять несколько аргументов через запятую.'),
    ]
    return items


def build_python_medium():
    """Средние Python-задачи (уровень 2): условия, циклы, списки."""
    items = [
        ('Условие if', 'python-if', 'Если 10 больше 5, выведи "big", иначе "small".',
         'Выход:\nbig', 'big', 'Используй if ... else: в одной ветке одно слово, в другой — второе.'),
        ('Чётное число', 'python-even', 'Выведи True, если 8 чётное.',
         'Выход:\nTrue', 'True', 'Число чётное, если остаток от деления на 2 равен нулю (%).'),
        ('Сравнение', 'python-cmp', 'Выведи True, если 3 меньше 5.',
         'Выход:\nTrue', 'True', 'Оператор сравнения «меньше» — <.'),
        ('Логическое И', 'python-and', 'Выведи True, если 5 больше 3 И 5 меньше 10.',
         'Выход:\nTrue', 'True', 'Объединяй два условия оператором and.'),
        ('Логическое ИЛИ', 'python-or', 'Выведи True, если 1 больше 10 ИЛИ 2 меньше 3.',
         'Выход:\nTrue', 'True', 'Объединяй два условия оператором or.'),
        ('Отрицание', 'python-not', 'Выведи True для not False.',
         'Выход:\nTrue', 'True', 'Оператор not меняет значение на противоположное.'),
        ('Округление', 'python-round', 'Округли число 3.7 до целого.',
         'Выход:\n4', '4', 'Функция round() округляет число.'),
        ('Модуль числа', 'python-abs', 'Выведи модуль числа -9.',
         'Выход:\n9', '9', 'Функция abs() возвращает модуль (без знака).'),
        ('Максимум', 'python-max', 'Выведи максимальное из чисел 4, 9, 2.',
         'Выход:\n9', '9', 'Функция max() находит наибольшее среди аргументов.'),
        ('Минимум', 'python-min', 'Выведи минимальное из чисел 7, 1, 5.',
         'Выход:\n1', '1', 'Функция min() находит наименьшее среди аргументов.'),
        ('Цикл от 1 до 3', 'python-loop-1-3', 'Выведи числа от 1 до 3, каждое на новой строке.',
         'Выход:\n1\n2\n3', '1\n2\n3', 'Цикл for с range() перебирает числа по очереди.'),
        ('Цикл от 0 до 2', 'python-loop-0-2', 'Выведи числа от 0 до 2.',
         'Выход:\n0\n1\n2', '0\n1\n2', 'range(n) даёт числа от 0 до n-1.'),
        ('Сумма через цикл', 'python-loop-sum', 'Вычисли и выведи сумму чисел от 1 до 5.',
         'Выход:\n15', '15', 'Функция sum() складывает все числа в последовательности.'),
        ('Сумма через цикл 2', 'python-loop-sum2', 'Вычисли и выведи сумму чисел от 2 до 6 включительно.',
         'Выход:\n20', '20', 'Сложи числа по очереди: начни с 2 и прибавляй до 6.'),
        ('Таблица умножения на 3', 'python-mul3', 'Выведи результат 3 * 4.',
         'Выход:\n12', '12', 'Умножение — оператор *.'),
        ('Цикл со счётом', 'python-loop-count', 'Сосчитай, сколько чисел от 1 до 10 включительно.',
         'Выход:\n10', '10', 'Функция len() считает элементы последовательности.'),
        ('Факториал', 'python-factorial', 'Вычисли произведение чисел от 1 до 5.',
         'Выход:\n120', '120', 'Перемножь числа от 1 до 5 по очереди.'),
        ('Среднее арифметическое', 'python-avg', 'Вычисли среднее арифметическое чисел 2 и 8.',
         'Выход:\n5.0', '5.0', 'Сложи числа и раздели сумму на их количество.'),
        ('Длина списка', 'python-list-len', 'Выведи длину списка [1, 2, 3, 4, 5].',
         'Выход:\n5', '5', 'Функция len() считает элементы списка.'),
        ('Сумма списка', 'python-list-sum', 'Выведи сумму элементов списка [1, 2, 3].',
         'Выход:\n6', '6', 'Функция sum() складывает элементы списка.'),
        ('Первый элемент', 'python-list-first', 'Выведи первый элемент списка [7, 8, 9].',
         'Выход:\n7', '7', 'Элементы списка доступны по индексу, первый — индекс 0.'),
        ('Последний элемент', 'python-list-last', 'Выведи последний элемент списка [7, 8, 9].',
         'Выход:\n9', '9', 'Последний элемент доступен по индексу -1.'),
        ('Сортировка', 'python-list-sort', 'Выведи отсортированный список [3, 1, 2].',
         'Выход:\n[1, 2, 3]', '[1, 2, 3]', 'Функция sorted() возвращает отсортированный список.'),
        ('Добавить в список', 'python-list-append', 'Выведи список [1, 2] после добавления числа 3.',
         'Выход:\n[1, 2, 3]', '[1, 2, 3]', 'У списка есть метод append() — добавляет элемент в конец.'),
        ('Срез списка', 'python-list-slice', 'Выведи элементы с индекса 1 по 2 включительно из [10, 20, 30].',
         'Выход:\n[20, 30]', '[20, 30]', 'Срез — список[начало:конец], конец не включается.'),
        ('Умножение элементов', 'python-list-mul', 'Выведи произведение всех чисел в списке [2, 3, 4].',
         'Выход:\n24', '24', 'Перемножь числа по очереди.'),
        ('Строки в список', 'python-split', 'Разбей строку "a b c" по пробелу и выведи список.',
         'Выход:\n[\'a\', \'b\', \'c\']', "['a', 'b', 'c']", 'Метод split() разбивает строку на список по разделителю.'),
    ]
    return items


def build_python_hard():
    """Сложные Python-задачи (уровень 3): функции, словари, продвинутое."""
    items = [
        ('Функция с параметром', 'python-func', 'Напиши функцию add(a, b), возвращающую сумму, и выведи add(3, 4).',
         'Выход:\n7', '7', 'Функция объявляется через def, возвращает значение через return.'),
        ('Функция квадрата', 'python-func-sq', 'Напиши функцию square(x), возвращающую x², и выведи square(6).',
         'Выход:\n36', '36', 'Квадрат — число, умноженное на само себя.'),
        ('Функция чётности', 'python-func-even', 'Напиши функцию is_even(n), возвращающую True для 4.',
         'Выход:\nTrue', 'True', 'Чётность проверяется остатком от деления на 2.'),
        ('Функция с условием', 'python-func-cmp', 'Напиши функцию bigger(a, b), возвращающую большее из 5 и 9.',
         'Выход:\n9', '9', 'Сравни два числа через if и верни большее.'),
        ('Строковая функция', 'python-func-str', 'Напиши функцию shout(s), возвращающую s с восклицательным знаком.',
         'Выход:\nHi!', 'Hi!', 'Соедини строку с символом ! через +.'),
        ('Словарь: значение', 'python-dict-get', 'Выведи значение по ключу name из словаря.',
         'Выход:\nJahongir', 'Jahongir', 'Словарь создаётся фигурными скобками, значение берётся по ключу в [].'),
        ('Словарь: длина', 'python-dict-len', 'Выведи количество ключей в словаре {"a":1, "b":2, "c":3}.',
         'Выход:\n3', '3', 'Функция len() считает ключи словаря.'),
        ('Словарь: ключи', 'python-dict-keys', 'Выведи ключи словаря {"x":1, "y":2}.',
         'Выход:\ndict_keys([\'x\', \'y\'])', "dict_keys(['x', 'y'])", 'Метод keys() возвращает все ключи словаря.'),
        ('Словарь: добавить', 'python-dict-add', 'Добавь ключ "z" со значением 3 в словарь {"x":1} и выведи.',
         'Выход:\n{\'x\': 1, \'z\': 3}', "{'x': 1, 'z': 3}", 'Новый ключ добавляется присваиванием: словарь[ключ] = значение.'),
        ('Словарь: сумма значений', 'python-dict-sum', 'Выведи сумму значений словаря {"a":2, "b":3, "c":5}.',
         'Выход:\n10', '10', 'Метод values() возвращает значения, а sum() их складывает.'),
        ('Реверс строки', 'python-reverse', 'Выведи строку "abc" задом наперёд.',
         'Выход:\ncba', 'cba', 'Срез с отрицательным шагом переворачивает строку.'),
        ('Подсчёт буквы', 'python-count-letter', 'Посчитай, сколько раз буква "l" встречается в "hello".',
         'Выход:\n2', '2', 'У строк есть метод count() — считает вхождения.'),
        ('Замена', 'python-replace', 'Замени в "a-b-c" дефисы на пробелы.',
         'Выход:\na b c', 'a b c', 'Метод replace(старое, новое) заменяет подстроки.'),
        ('Проверка подстроки', 'python-in', 'Выведи True, если "py" есть в "python".',
         'Выход:\nTrue', 'True', 'Оператор in проверяет вхождение подстроки.'),
        ('Генератор списка', 'python-listcomp', 'Выведи список квадратов чисел от 1 до 3.',
         'Выход:\n[1, 4, 9]', '[1, 4, 9]', 'List comprehension: [выражение for x in range(...)].'),
        ('Сумма через comprehension', 'python-listcomp-sum', 'Выведи сумму квадратов чисел от 1 до 4.',
         'Выход:\n30', '30', 'Сначала список квадратов, потом sum().'),
        ('f-строка', 'python-fstring', 'Выведи "x = 5" используя f-строку с переменной x=5.',
         'Выход:\nx = 5', 'x = 5', 'f-строка начинается с f перед кавычками, переменные в {} внутри.'),
        ('Тернарный оператор', 'python-ternary', 'Выведи "even", если 4 чётное, иначе "odd".',
         'Выход:\neven', 'even', 'Тернарный оператор: значение_если_да if условие else значение_если_нет.'),
        ('Цепочка сравнений', 'python-chain', 'Выведи True, если 5 находится между 1 и 10.',
         'Выход:\nTrue', 'True', 'Можно сравнивать цепочкой: a < b < c.'),
        ('Форматирование', 'python-format', 'Выведи число 3.14159 с двумя знаками после запятой.',
         'Выход:\n3.14', '3.14', 'Формат f-строки: {значение:.2f} — два знака после запятой.'),
    ]
    return items


def build_sql_basic():
    """Простые SQL-задачи (уровень 1): SELECT, WHERE, ORDER BY, LIMIT."""
    items = [
        ('Выбрать название фильма', 'sql-film-title', 'Выведи название фильма с film_id = 1 из таблицы film.',
         'Ожидается: 1 строка (title)', 'SELECT title FROM film WHERE film_id = 1;',
         'Сначала выбери колонку title, потом таблицу film, потом условие по film_id.'),
        ('Пять фильмов', 'sql-film-5', 'Выведи первые 5 названий фильмов из таблицы film.',
         'Ожидается: 5 строк (title)', 'SELECT title FROM film LIMIT 5;',
         'LIMIT ограничивает количество строк.'),
        ('Все актёры', 'sql-actor-all', 'Выведи имена всех актёров из таблицы actor.',
         'Ожидается: 200 строк (first_name)', 'SELECT first_name FROM actor;',
         'Простой SELECT нужной колонки из таблицы.'),
        ('Актёр по фамилии', 'sql-actor-lastname', 'Выведи имя актёра с last_name = "GUINESS".',
         'Ожидается: имя актёра', "SELECT first_name FROM actor WHERE last_name = 'GUINESS';",
         'Фильтр по строке пишется в WHERE с кавычками.'),
        ('Фильмы дешевле 1', 'sql-film-cheap', 'Выведи названия фильмов с rental_rate меньше 1.',
         'Ожидается: названия фильмов', 'SELECT title FROM film WHERE rental_rate < 1;',
         'Условие «меньше» — оператор < в WHERE.'),
        ('Фильмы длиннее 120', 'sql-film-long', 'Выведи названия фильмов длиной больше 120 минут.',
         'Ожидается: названия фильмов', 'SELECT title FROM film WHERE length > 120;',
         'Условие «больше» — оператор > в WHERE.'),
        ('Фильмы с рейтингом PG', 'sql-film-pg', 'Выведи названия фильмов с рейтингом PG.',
         'Ожидается: названия фильмов', "SELECT title FROM film WHERE rating = 'PG';",
         'Сравнение строки с равенством — оператор =.'),
        ('Сортировка по длине', 'sql-order-length', 'Выведи 5 самых длинных фильмов (title, length) по убыванию длины.',
         'Ожидается: 5 строк', 'SELECT title, length FROM film ORDER BY length DESC LIMIT 5;',
         'Сортировка по убыванию — ORDER BY ... DESC.'),
        ('Сортировка по имени', 'sql-order-name', 'Выведи 3 актёров в алфавитном порядке по имени.',
         'Ожидается: 3 строки', 'SELECT first_name FROM actor ORDER BY first_name LIMIT 3;',
         'Сортировка по возрастанию — ORDER BY (по умолчанию ASC).'),
        ('Сортировка по цене', 'sql-order-price', 'Выведи 3 самых дорогих фильма по rental_rate.',
         'Ожидается: 3 строки', 'SELECT title FROM film ORDER BY rental_rate DESC LIMIT 3;',
         'ORDER BY ... DESC + LIMIT.'),
        ('Дорогие фильмы', 'sql-price-high', 'Выведи названия фильмов с rental_rate больше 4.',
         'Ожидается: названия фильмов', 'SELECT title FROM film WHERE rental_rate > 4;',
         'Условие «больше» — оператор >.'),
        ('Количество фильмов', 'sql-count-film', 'Посчитай, сколько всего фильмов в таблице film.',
         'Ожидается: 1000', 'SELECT COUNT(*) FROM film;',
         'Агрегатная функция COUNT считает строки.'),
        ('Количество актёров', 'sql-count-actor', 'Посчитай, сколько всего актёров в таблице actor.',
         'Ожидается: 200', 'SELECT COUNT(*) FROM actor;',
         'COUNT(*) считает все строки.'),
        ('Количество клиентов', 'sql-count-customer', 'Посчитай, сколько всего клиентов в таблице customer.',
         'Ожидается: 599', 'SELECT COUNT(*) FROM customer;',
         'COUNT(*) считает все строки.'),
        ('Первый клиент', 'sql-customer-first', 'Выведи имя и фамилию клиента с customer_id = 1.',
         'Ожидается: 1 строка', 'SELECT first_name, last_name FROM customer WHERE customer_id = 1;',
         'Выбери две колонки, фильтр по id.'),
        ('Уникальные рейтинги', 'sql-distinct-rating', 'Выведи уникальные значения рейтинга (rating) из film.',
         'Ожидается: 5 строк', 'SELECT DISTINCT rating FROM film;',
         'DISTINCT убирает дубли.'),
        ('Фильмы на английском', 'sql-film-en', 'Выведи названия фильмов с language_id = 1.',
         'Ожидается: 1000 строк', 'SELECT title FROM film WHERE language_id = 1;',
         'Фильтр по числовой колонке.'),
        ('Фильмы начинаются на A', 'sql-film-a', 'Выведи названия фильмов, начинающиеся на букву "A".',
         'Ожидается: названия фильмов', "SELECT title FROM film WHERE title LIKE 'A%';",
         'LIKE с паттерном: % означает «любое количество символов».'),
        ('Фильмы с 2000 годом', 'sql-film-2000', 'Выведи названия фильмов, выпущенных в 2000 году.',
         'Ожидается: названия фильмов', "SELECT title FROM film WHERE release_year = 2000;",
         'Фильтр по колонке release_year.'),
        ('Короткие фильмы', 'sql-film-short', 'Выведи названия фильмов длиной меньше 60 минут.',
         'Ожидается: названия фильмов', 'SELECT title FROM film WHERE length < 60;',
         'Условие «меньше» — оператор <.'),
        ('Бесплатные фильмы', 'sql-film-free', 'Выведи названия фильмов с rental_rate = 0.',
         'Ожидается: названия фильмов', 'SELECT title FROM film WHERE rental_rate = 0;',
         'Фильтр по числовой колонке равенством.'),
        ('Средняя длина', 'sql-avg-length', 'Вычисли среднюю длину фильмов в таблице film.',
         'Ожидается: одно число', 'SELECT AVG(length) FROM film;',
         'AVG — среднее арифметическое.'),
        ('Максимальная длина', 'sql-max-length', 'Вычисли максимальную длину фильма.',
         'Ожидается: одно число', 'SELECT MAX(length) FROM film;',
         'MAX — максимум.'),
        ('Минимальная цена', 'sql-min-rate', 'Вычисли минимальную rental_rate в таблице film.',
         'Ожидается: одно число', 'SELECT MIN(rental_rate) FROM film;',
         'MIN — минимум.'),
        ('Сумма платежей', 'sql-sum-payment', 'Вычисли сумму всех платежей (amount) в таблице payment.',
         'Ожидается: одно число', 'SELECT SUM(amount) FROM payment;',
         'SUM — сумма значений колонки.'),
    ]
    return items


def build_sql_medium():
    """Средние SQL-задачи (уровень 2): WHERE с несколькими условиями, GROUP BY, JOIN."""
    items = [
        ('Фильмы PG и длинные', 'sql-pg-long', 'Выведи названия фильмов с рейтингом PG и длиной больше 120.',
         'Ожидается: названия фильмов', "SELECT title FROM film WHERE rating = 'PG' AND length > 120;",
         'Объединяй два условия оператором AND.'),
        ('Фильмы PG или G', 'sql-pg-g', 'Выведи названия фильмов с рейтингом PG или G.',
         'Ожидается: названия фильмов', "SELECT title FROM film WHERE rating = 'PG' OR rating = 'G';",
         'Объединяй условия оператором OR.'),
        ('Фильмы в диапазоне', 'sql-between', 'Выведи названия фильмов длиной от 90 до 120 минут.',
         'Ожидается: названия фильмов', 'SELECT title FROM film WHERE length BETWEEN 90 AND 120;',
         'Диапазон задаётся BETWEEN ... AND ....'),
        ('Клиенты с email', 'sql-customer-email', 'Выведи email клиентов, начинающийся с "m".',
         'Ожидается: email', "SELECT email FROM customer WHERE email LIKE 'm%';",
         'LIKE с паттерном: буква и %.'),
        ('Группировка по рейтингу', 'sql-group-rating', 'Посчитай количество фильмов для каждого рейтинга.',
         'Ожидается: рейтинг + количество', 'SELECT rating, COUNT(*) FROM film GROUP BY rating;',
         'GROUP BY группирует строки, COUNT считает в группе.'),
        ('Группировка по языку', 'sql-group-lang', 'Посчитай количество фильмов для каждого языка.',
         'Ожидается: язык + количество', 'SELECT language_id, COUNT(*) FROM film GROUP BY language_id;',
         'GROUP BY по колонке + COUNT.'),
        ('Средняя длина по рейтингу', 'sql-avg-rating', 'Вычисли среднюю длину фильмов для каждого рейтинга.',
         'Ожидается: рейтинг + средняя длина', 'SELECT rating, AVG(length) FROM film GROUP BY rating;',
         'GROUP BY + AVG по длине.'),
        ('Платежи по клиентам', 'sql-group-payment', 'Посчитай количество платежей для каждого клиента (первые 5).',
         'Ожидается: customer_id + count', 'SELECT customer_id, COUNT(*) FROM payment GROUP BY customer_id LIMIT 5;',
         'GROUP BY customer_id + COUNT + LIMIT.'),
        ('Сумма платежей по клиентам', 'sql-sum-customer', 'Вычисли сумму платежей для каждого клиента (первые 5).',
         'Ожидается: customer_id + сумма', 'SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id LIMIT 5;',
         'GROUP BY customer_id + SUM по amount.'),
        ('Топ-5 по платежам', 'sql-top-payment', 'Выведи 5 клиентов с наибольшей суммой платежей.',
         'Ожидается: 5 строк', 'SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id ORDER BY SUM(amount) DESC LIMIT 5;',
         'Группируй по клиенту, сортируй по сумме по убыванию.'),
        ('Клиенты с 30+ платежами', 'sql-having', 'Выведи клиентов, у которых больше 30 платежей.',
         'Ожидается: customer_id + count', 'SELECT customer_id, COUNT(*) FROM payment GROUP BY customer_id HAVING COUNT(*) > 30;',
         'HAVING фильтрует группы (не строки!).'),
        ('JOIN: фильмы и язык', 'sql-join-lang', 'Выведи названия фильмов и названия их языков (join film и language).',
         'Ожидается: title + language name', 'SELECT f.title, l.name FROM film f JOIN language l ON f.language_id = l.language_id LIMIT 10;',
         'JOIN соединяет две таблицы по общему ключу через ON.'),
        ('JOIN: актёр и фильмы', 'sql-join-actor', 'Выведи имя актёра и названия его фильмов (первый актёр).',
         'Ожидается: first_name + title', 'SELECT a.first_name, f.title FROM actor a JOIN film_actor fa ON a.actor_id = fa.actor_id JOIN film f ON fa.film_id = f.film_id WHERE a.actor_id = 1 LIMIT 10;',
         'Цепочка JOIN: actor → film_actor → film.'),
        ('JOIN: клиент и платежи', 'sql-join-customer', 'Выведи имя клиента и сумму его платежа (первый клиент).',
         'Ожидается: first_name + amount', 'SELECT c.first_name, p.amount FROM customer c JOIN payment p ON c.customer_id = p.customer_id WHERE c.customer_id = 1 LIMIT 5;',
         'JOIN customer и payment по customer_id.'),
        ('Категории фильмов', 'sql-join-category', 'Посчитай количество фильмов в каждой категории.',
         'Ожидается: категория + количество', 'SELECT c.name, COUNT(*) FROM category c JOIN film_category fc ON c.category_id = fc.category_id GROUP BY c.name;',
         'JOIN category → film_category, потом GROUP BY по имени.'),
        ('Фильмы с актёром 5', 'sql-actor-5', 'Выведи названия фильмов, где снимался актёр с actor_id = 5.',
         'Ожидается: названия фильмов', 'SELECT f.title FROM film f JOIN film_actor fa ON f.film_id = fa.film_id WHERE fa.actor_id = 5;',
         'JOIN film и film_actor, фильтр по актёру.'),
        ('Аренда по клиенту', 'sql-join-rental', 'Выведи даты аренды для клиента с id = 1 (первые 5).',
         'Ожидается: 5 дат', 'SELECT rental_date FROM rental WHERE customer_id = 1 LIMIT 5;',
         'Простой фильтр по customer_id + LIMIT.'),
        ('Платежи больше среднего', 'sql-avg-sub', 'Выведи платежи больше среднего значения amount.',
         'Ожидается: суммы', 'SELECT amount FROM payment WHERE amount > (SELECT AVG(amount) FROM payment) LIMIT 10;',
         'Подзапрос в скобках вычисляет среднее, с ним сравнивай.'),
        ('Фильмы без инвентаря', 'sql-no-inventory', 'Выведи названия фильмов, которых нет в таблице inventory.',
         'Ожидается: названия фильмов', 'SELECT title FROM film WHERE film_id NOT IN (SELECT DISTINCT film_id FROM inventory);',
         'NOT IN + подзапрос, возвращающий список film_id.'),
        ('Актёры с 30+ фильмами', 'sql-actor-30', 'Выведи актёров, снявшихся более чем в 30 фильмах.',
         'Ожидается: имя + количество', 'SELECT a.first_name, COUNT(*) FROM actor a JOIN film_actor fa ON a.actor_id = fa.actor_id GROUP BY a.first_name HAVING COUNT(*) > 30;',
         'JOIN + GROUP BY + HAVING по количеству.'),
    ]
    return items


def build_sql_hard():
    """Сложные SQL-задачи (уровень 3): подзапросы, оконные функции."""
    items = [
        ('Фильмы длиннее среднего', 'sql-longer-avg', 'Выведи названия фильмов длиннее средней длины.',
         'Ожидается: названия фильмов', 'SELECT title FROM film WHERE length > (SELECT AVG(length) FROM film) LIMIT 20;',
         'Сравни длину с подзапросом, вычисляющим среднюю.'),
        ('Второй по длине', 'sql-second-long', 'Выведи второй по длине фильм (title, length).',
         'Ожидается: 1 строка', 'SELECT title, length FROM film ORDER BY length DESC LIMIT 1 OFFSET 1;',
         'OFFSET пропускает первую строку.'),
        ('Нумерация фильмов', 'sql-window-row', 'Пронумеруй фильмы по длине (ROW_NUMBER) — первые 5.',
         'Ожидается: 5 строк', 'SELECT title, ROW_NUMBER() OVER (ORDER BY length DESC) FROM film LIMIT 5;',
         'Оконная функция ROW_NUMBER() OVER (ORDER BY ...).'),
        ('Ранг фильмов', 'sql-window-rank', 'Назначь ранг (RANK) фильмам по rental_rate — первые 5.',
         'Ожидается: 5 строк', 'SELECT title, RANK() OVER (ORDER BY rental_rate DESC) FROM film LIMIT 5;',
         'Оконная функция RANK() OVER (ORDER BY ...).'),
        ('Клиенты выше среднего', 'sql-customer-above-avg', 'Выведи клиентов, чья сумма платежей выше средней суммы всех платежей.',
         'Ожидается: customer_id + сумма', 'SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id HAVING SUM(amount) > (SELECT AVG(amount) FROM payment) LIMIT 10;',
         'HAVING с подзапросом среднего.'),
        ('Фильмы с несколькими актёрами', 'sql-multi-actor', 'Выведи фильмы, в которых больше 5 актёров.',
         'Ожидается: title + количество', 'SELECT f.title, COUNT(*) FROM film f JOIN film_actor fa ON f.film_id = fa.film_id GROUP BY f.title HAVING COUNT(*) > 5;',
         'JOIN + GROUP BY + HAVING по количеству.'),
        ('Среднее по категориям', 'sql-category-avg', 'Вычисли среднюю длину фильмов для каждой категории.',
         'Ожидается: категория + средняя длина', 'SELECT c.name, AVG(f.length) FROM category c JOIN film_category fc ON c.category_id = fc.category_id JOIN film f ON fc.film_id = f.film_id GROUP BY c.name;',
         'Тройной JOIN + GROUP BY + AVG.'),
        ('Актёр во многих фильмах', 'sql-actor-many', 'Выведи 3 актёров с наибольшим количеством фильмов.',
         'Ожидается: имя + количество', 'SELECT a.first_name, COUNT(*) cnt FROM actor a JOIN film_actor fa ON a.actor_id = fa.actor_id GROUP BY a.first_name ORDER BY cnt DESC LIMIT 3;',
         'GROUP BY + ORDER BY по убыванию + LIMIT.'),
        ('Платежи по годам', 'sql-year-payment', 'Сгруппируй платежи по году и посчитай количество в каждом (первые 5).',
         'Ожидается: год + количество', 'SELECT EXTRACT(YEAR FROM payment_date), COUNT(*) FROM payment GROUP BY EXTRACT(YEAR FROM payment_date) LIMIT 5;',
         'EXTRACT(YEAR FROM ...) извлекает год из даты.'),
        ('Фильмы без актёров', 'sql-no-actor', 'Выведи фильмы, в которых нет ни одного актёра.',
         'Ожидается: названия фильмов', 'SELECT title FROM film WHERE film_id NOT IN (SELECT DISTINCT film_id FROM film_actor) LIMIT 10;',
         'NOT IN + подзапрос списка film_id.'),
        ('Самый дорогой фильм', 'sql-most-expensive', 'Выведи самый дорогой фильм (по replacement_cost).',
         'Ожидается: 1 строка', 'SELECT title, replacement_cost FROM film ORDER BY replacement_cost DESC LIMIT 1;',
         'Сортировка по убыванию + LIMIT 1.'),
        ('Средняя цена фильма', 'sql-avg-cost', 'Вычисли среднюю replacement_cost всех фильмов.',
         'Ожидается: одно число', 'SELECT AVG(replacement_cost) FROM film;',
         'AVG по колонке.'),
        ('Уникальные актёры', 'sql-distinct-actor', 'Посчитай количество уникальных актёров в film_actor.',
         'Ожидается: 200', 'SELECT COUNT(DISTINCT actor_id) FROM film_actor;',
         'COUNT(DISTINCT ...) считает уникальные значения.'),
        ('Фильмы с PG-13', 'sql-pg13', 'Выведи названия фильмов с рейтингом PG-13 длиной меньше 90.',
         'Ожидается: названия фильмов', "SELECT title FROM film WHERE rating = 'PG-13' AND length < 90;",
         'Два условия через AND.'),
        ('Дубли имён', 'sql-duplicate-name', 'Выведи имена актёров, которые повторяются (больше 1 раза).',
         'Ожидается: имя + количество', 'SELECT first_name, COUNT(*) FROM actor GROUP BY first_name HAVING COUNT(*) > 1;',
         'GROUP BY по имени + HAVING.'),
        ('Топ платежей с join', 'sql-join-payment-customer', 'Выведи имена клиентов и сумму их платежей по убыванию (первые 5).',
         'Ожидается: 5 строк', 'SELECT c.first_name, SUM(p.amount) FROM customer c JOIN payment p ON c.customer_id = p.customer_id GROUP BY c.first_name ORDER BY SUM(p.amount) DESC LIMIT 5;',
         'JOIN + GROUP BY + ORDER BY по убыванию.'),
        ('Фильмы с высоким рейтингом', 'sql-high-rating', 'Выведи фильмы с рейтингом G и длиной больше 150.',
         'Ожидается: названия фильмов', "SELECT title FROM film WHERE rating = 'G' AND length > 150;",
         'Два условия через AND.'),
        ('Самая длинная категория', 'sql-longest-category', 'Выведи категорию с наибольшей средней длиной фильмов.',
         'Ожидается: 1 категория', 'SELECT c.name, AVG(f.length) FROM category c JOIN film_category fc ON c.category_id = fc.category_id JOIN film f ON fc.film_id = f.film_id GROUP BY c.name ORDER BY AVG(f.length) DESC LIMIT 1;',
         'Тройной JOIN + GROUP BY + сортировка по среднему.'),
        ('Количество аренд', 'sql-count-rental', 'Посчитай общее количество аренд (rental).',
         'Ожидается: число', 'SELECT COUNT(*) FROM rental;',
         'COUNT(*).'),
        ('Активные клиенты', 'sql-active-customer', 'Выведи имена активных клиентов (active = 1).',
         'Ожидается: имена', 'SELECT first_name FROM customer WHERE active = 1 LIMIT 10;',
         'Фильтр по колонке active.'),
    ]
    return items


def build_python_extra():
    """Дополнительные Python-задачи (уровень 2-3): строки, списки, словари."""
    return [
        ('Длина без пробелов', 'python-strip-len', 'Выведи длину строки "  hello  " после удаления пробелов по краям.',
         'Выход:\n5', '5', 'Метод strip() убирает пробелы по краям, потом len().'),
        ('Заглавная буква', 'python-capitalize', 'Выведи слово "python" с заглавной первой буквой.',
         'Выход:\nPython', 'Python', 'Метод capitalize() делает первую букву заглавной.'),
        ('Начинается с', 'python-startswith', 'Выведи True, если слово "python" начинается на "py".',
         'Выход:\nTrue', 'True', 'Метод startswith() проверяет начало строки.'),
        ('Заканчивается на', 'python-endswith', 'Выведи True, если слово "python" заканчивается на "on".',
         'Выход:\nTrue', 'True', 'Метод endswith() проверяет конец строки.'),
        ('Поиск подстроки', 'python-find', 'Выведи индекс первого вхождения "l" в строку "hello".',
         'Выход:\n2', '2', 'Метод find() возвращает индекс вхождения (с 0).'),
        ('Убрать пробелы', 'python-replace-space', 'Замени в "a b c" все пробелы на дефисы.',
         'Выход:\na-b-c', 'a-b-c', 'Метод replace() меняет символы.'),
        ('Список в строку', 'python-join', 'Соедини список ["a","b","c"] в строку через запятую.',
         'Выход:\na,b,c', 'a,b,c', 'Метод join() соединяет список строк с разделителем.'),
        ('Дважды словарь', 'python-dict-nested', 'Выведи значение вложенного словаря: {"a": {"b": 7}} ключ a затем b.',
         'Выход:\n7', '7', 'Доступ по двум ключам подряд: d["a"]["b"].'),
        ('Счётчик в словаре', 'python-dict-count', 'Создай словарь {"x": 1} и увеличь значение x на 5, выведи.',
         'Выход:\n6', '6', 'Сложи: d["x"] = d["x"] + 5, потом print.'),
        ('Список по шагу', 'python-step', 'Выведи список чисел от 0 до 10 с шагом 2.',
         'Выход:\n[0, 2, 4, 6, 8, 10]', '[0, 2, 4, 6, 8, 10]', 'range(0, 11, 2) — третий аргумент шаг.'),
        ('Реверс списка', 'python-reverse-list', 'Выведи список [1, 2, 3] в обратном порядке.',
         'Выход:\n[3, 2, 1]', '[3, 2, 1]', 'Срез [::-1] или метод reverse().'),
        ('Максимум в списке', 'python-list-max', 'Выведи максимальный элемент списка [3, 9, 1, 7].',
         'Выход:\n9', '9', 'Функция max() для списка.'),
        ('Минимум в списке', 'python-list-min', 'Выведи минимальный элемент списка [5, 2, 8, 1].',
         'Выход:\n1', '1', 'Функция min() для списка.'),
        ('Количество в списке', 'python-list-count', 'Посчитай, сколько раз число 2 встречается в [1, 2, 2, 3].',
         'Выход:\n2', '2', 'Метод count() у списка.'),
        ('Первые два', 'python-slice-first', 'Выведи первые два элемента списка [10, 20, 30, 40].',
         'Выход:\n[10, 20]', '[10, 20]', 'Срез [0:2].'),
        ('Сумма чётных', 'python-sum-even', 'Выведи сумму чётных чисел от 2 до 6 включительно.',
         'Выход:\n12', '12', '2+4+6.'),
        ('Второй элемент', 'python-list-index', 'Выведи элемент с индексом 1 в списке ["a","b","c"].',
         'Выход:\nb', 'b', 'Индексы с 0: [1] — второй элемент.'),
        ('Умножение двух списков', 'python-zip-sum', 'Сложи поэлементно [1, 2, 3] и [10, 20, 30] и выведи сумму.',
         'Выход:\n66', '66', '11+22+33.'),
    ]


def build_sql_extra():
    """Дополнительные SQL-задачи (уровень 2-3): CASE, LIKE, сложные JOIN."""
    return [
        ('Фильмы с Night', 'sql-like-night', 'Выведи названия фильмов, содержащие слово "Night".',
         'Ожидается: названия фильмов', "SELECT title FROM film WHERE title LIKE '%Night%' LIMIT 5;",
         "LIKE '%Night%' — содержит подстроку."),
        ('Актёры на J', 'sql-actor-j', 'Выведи имя и фамилию актёров, чьё имя начинается на "J", по алфавиту.',
         'Ожидается: строки', "SELECT first_name, last_name FROM actor WHERE first_name LIKE 'J%' ORDER BY first_name LIMIT 5;",
         "LIKE 'J%' + ORDER BY."),
        ('Группы цен', 'sql-case', 'Выведи название фильма и группу цены (дешёвый/средний/дорогой) через CASE.',
         'Ожидается: title + price_group', "SELECT title, CASE WHEN rental_rate < 1 THEN 'cheap' WHEN rental_rate < 4 THEN 'medium' ELSE 'expensive' END FROM film LIMIT 5;",
         'CASE WHEN условие THEN ... WHEN ... ELSE ... END.'),
        ('Популярные имена', 'sql-popular-name', 'Выведи имена актёров по убыванию частоты (сколько актёров с таким именем).',
         'Ожидается: имя + количество', 'SELECT first_name, COUNT(*) FROM actor GROUP BY first_name ORDER BY COUNT(*) DESC, first_name LIMIT 5;',
         'GROUP BY + ORDER BY по количеству, потом по имени.'),
        ('Нумерация в категории', 'sql-window-partition', 'Пронумеруй фильмы по длине внутри каждого рейтинга (PARTITION BY rating).',
         'Ожидается: 5 строк', 'SELECT title, length, ROW_NUMBER() OVER (PARTITION BY rating ORDER BY length DESC) FROM film LIMIT 5;',
         'ROW_NUMBER() OVER (PARTITION BY rating ORDER BY ...).'),
        ('LEFT JOIN аренды', 'sql-left-join', 'Выведи клиентов и количество их аренд (включая тех, у кого 0 аренд).',
         'Ожидается: имя + количество', 'SELECT c.first_name, COUNT(r.rental_id) FROM customer c LEFT JOIN rental r ON c.customer_id = r.customer_id GROUP BY c.first_name ORDER BY COUNT(r.rental_id) DESC LIMIT 5;',
         'LEFT JOIN — сохраняет всех клиентов слева.'),
        ('Платежи по месяцам', 'sql-month-payment', 'Выведи сумму платежей по месяцам (первые 6).',
         'Ожидается: месяц + сумма', 'SELECT EXTRACT(MONTH FROM payment_date), SUM(amount) FROM payment GROUP BY EXTRACT(MONTH FROM payment_date) ORDER BY EXTRACT(MONTH FROM payment_date) LIMIT 6;',
         'EXTRACT(MONTH FROM ...) + GROUP BY.'),
        ('Дороже среднего замены', 'sql-cost-avg', 'Выведи фильмы с replacement_cost выше средней.',
         'Ожидается: title + cost', 'SELECT title, replacement_cost FROM film WHERE replacement_cost > (SELECT AVG(replacement_cost) FROM film) LIMIT 5;',
         'Подзапрос AVG в WHERE.'),
        ('Дороже среднего аренды', 'sql-rate-avg', 'Выведи фильмы с rental_rate выше средней.',
         'Ожидается: title + rate', 'SELECT title, rental_rate FROM film WHERE rental_rate > (SELECT AVG(rental_rate) FROM film) LIMIT 5;',
         'Подзапрос AVG в WHERE.'),
        ('Фильмы G', 'sql-rating-g', 'Посчитай количество фильмов с рейтингом G.',
         'Ожидается: число', "SELECT COUNT(*) FROM film WHERE rating = 'G';",
         'COUNT + WHERE.'),
        ('Платежи больше 5', 'sql-payment-5', 'Посчитай количество платежей больше 5.',
         'Ожидается: число', 'SELECT COUNT(*) FROM payment WHERE amount > 5;',
         'COUNT + WHERE.'),
        ('Уникальные фамилии', 'sql-distinct-lastname', 'Посчитай количество уникальных фамилий актёров.',
         'Ожидается: число', 'SELECT COUNT(DISTINCT last_name) FROM actor;',
         'COUNT(DISTINCT ...).'),
    ]
    return items


def build_transaction_tasks():
    """Задачи по транзакциям (уровень 2)."""
    items = [
        ('Транзакция: BEGIN и COMMIT', 'txn-begin-commit', 'Опиши SQL: открой транзакцию, обнови amount платежа с id = 1 на 50, зафиксируй (COMMIT).',
         'BEGIN;\nUPDATE payment SET amount = 50 WHERE payment_id = 1;\nCOMMIT;',
         'BEGIN;\nUPDATE payment SET amount = 50 WHERE payment_id = 1;\nCOMMIT;',
         'BEGIN открывает транзакцию, COMMIT фиксирует. UPDATE меняет значение.', True),
        ('Транзакция: ROLLBACK', 'txn-rollback', 'Открой транзакцию, измени amount платежа с id = 2 на 10, затем откати (ROLLBACK).',
         'BEGIN;\nUPDATE payment SET amount = 10 WHERE payment_id = 2;\nROLLBACK;',
         'BEGIN;\nUPDATE payment SET amount = 10 WHERE payment_id = 2;\nROLLBACK;',
         'ROLLBACK отменяет изменения внутри транзакции.', True),
        ('Перевод денег', 'txn-money-transfer', 'Переведи 100 единиц со счёта 1 на счёт 2 внутри транзакции.',
         'BEGIN;\nUPDATE payment SET amount = amount - 100 WHERE payment_id = 1;\nUPDATE payment SET amount = amount + 100 WHERE payment_id = 2;\nCOMMIT;',
         'BEGIN;\nUPDATE payment SET amount = amount - 100 WHERE payment_id = 1;\nUPDATE payment SET amount = amount + 100 WHERE payment_id = 2;\nCOMMIT;',
         'Два UPDATE (минус и плюс) в одной транзакции.', True),
        ('Процентное изменение', 'txn-percent', 'В транзакции увеличь amount на 5% у платежей клиента с id = 1, затем откати.',
         'BEGIN;\nUPDATE payment SET amount = amount * 1.05 WHERE customer_id = 1;\nROLLBACK;',
         'BEGIN;\nUPDATE payment SET amount = amount * 1.05 WHERE customer_id = 1;\nROLLBACK;',
         'Увеличение на 5% — умножение на 1.05.', True),
        ('Тест: перевод (уровень 3)', 'txn-test-3', 'САМЫЙ СЛОЖНЫЙ ТЕСТ: переведи 50 единиц от платежа с id = 3 к платежу с id = 4, зафиксируй.',
         'BEGIN;\nUPDATE payment SET amount = amount - 50 WHERE payment_id = 3;\nUPDATE payment SET amount = amount + 50 WHERE payment_id = 4;\nCOMMIT;',
         'BEGIN;\nUPDATE payment SET amount = amount - 50 WHERE payment_id = 3;\nUPDATE payment SET amount = amount + 50 WHERE payment_id = 4;\nCOMMIT;',
         'Аналог перевода: минус у одного, плюс у другого.', True),
    ]
    return items


def build_level_tests():
    """Тесты уровня — самая сложная задача каждого уровня."""
    return [
        ('Тест уровня: Новичок → Ученик', 'test-level-novice', 'САМЫЙ СЛОЖНЫЙ ТЕСТ ТВОЕГО УРОВНЯ. Реши его — и перейдёшь на следующий уровень.\n\nНапиши программу, которая выводит квадрат числа 7.',
         'Выход:\n49', '49', 'Квадрат числа — число, умноженное на само себя.', 1, 10),
        ('Тест уровня: Ученик → Кодер', 'test-level-uchenik', 'САМЫЙ СЛОЖНЫЙ ТЕСТ ТВОЕГО УРОВНЯ. Реши его — и перейдёшь на следующий уровень.\n\nВнутри транзакции увеличь amount на 5% у платежей клиента с id = 1, затем откати.',
         'BEGIN;\nUPDATE payment SET amount = amount * 1.05 WHERE customer_id = 1;\nROLLBACK;',
         'BEGIN;\nUPDATE payment SET amount = amount * 1.05 WHERE customer_id = 1;\nROLLBACK;',
         'Увеличение на 5% — умножение на 1.05, в конце откат.', 2, 12, True),
    ]


# Обязательные элементы кода (защита от подстановки готового ответа)
REQUIRED_TOKENS = {
    'python-add': '7,3',
    'python-sub': '10,4',
    'python-mul': '6,7',
    'python-div': '20,5',
    'python-floordiv': '17,5',
    'python-mod': '17,5',
    'python-pow': '2,10',
    'python-str-num': '42',
    'python-len': 'Python',
    'python-upper': 'hello',
    'python-lower': 'WORLD',
    'python-concat': 'Py,thon',
    'python-str-mul': 'ab,3',
    'python-str-int': '42',
    'python-cmp': '3,5',
    'python-and': '5,3,10',
    'python-or': '1,2,3',
    'python-not': 'False',
    'python-round': '3,7',
    'python-abs': '9',
    'python-max': '4,9,2',
    'python-min': '7,1,5',
    'python-loop-1-3': '1,3',
    'python-loop-0-2': '3',
    'python-loop-sum': '1,5',
    'python-loop-sum2': '2,6',
    'python-mul3': '3,4',
    'python-loop-count': '1,10',
    'python-factorial': '5',
    'python-avg': '2,8',
    'python-list-len': '1,2,3,4,5',
    'python-list-sum': '1,2,3',
    'python-list-first': '7,8,9',
    'python-list-last': '7,8,9',
    'python-list-sort': '3,1,2',
    'python-list-append': '1,2,3',
    'python-list-slice': '10,20,30',
    'python-list-mul': '2,3,4',
    'python-func': '3,4',
    'python-func-sq': '6',
    'python-func-even': '4',
    'python-func-cmp': '5,9',
    'python-func-str': 'Hi',
    'python-dict-get': 'name',
    'python-dict-len': 'a,b,c',
    'python-dict-keys': 'x,y',
    'python-dict-add': 'x,z,3',
    'python-dict-sum': 'a,b,c',
    'python-reverse': 'abc',
    'python-count-letter': 'hello,l',
    'python-replace': 'a-b-c',
    'python-in': 'py,python',
    'python-listcomp': '1,3',
    'python-listcomp-sum': '1,4',
    'python-fstring': '5',
    'python-ternary': '4',
    'python-chain': '1,5,10',
    'python-format': '3.14159',
    'python-strip-len': 'hello',
    'python-capitalize': 'python',
    'python-startswith': 'python,py',
    'python-endswith': 'python,on',
    'python-find': 'hello,l',
    'python-replace-space': 'a b c',
    'python-join': 'a,b,c',
    'python-dict-nested': 'a,b',
    'python-dict-count': 'x,5',
    'python-step': '0,10,2',
    'python-reverse-list': '1,2,3',
    'python-list-max': '3,9,1,7',
    'python-list-min': '5,2,8,1',
    'python-list-count': '1,2,3',
    'python-slice-first': '10,20,30,40',
    'python-sum-even': '2,4,6',
    'python-list-index': 'a,b,c',
    'python-zip-sum': '1,2,3,10,20,30',
    'test-level-novice': '7',
}


def build_all():
    """Собирает полный список задач с готовыми полями."""
    tasks = []

    def add(title, slug, description, example, solution, hint, lvl, reward, task_type,
            difficulty, allow_write=False, is_test=False, hint_price=None, order=None,
            db_name='', required_tokens='', reference=''):
        if hint_price is None:
            hint_price = {Task.Difficulty.EASY: 8, Task.Difficulty.MEDIUM: 15, Task.Difficulty.HARD: 20}[difficulty]
        tasks.append({
            'title': title,
            'slug': slug,
            'task_type': task_type,
            'description': description,
            'example': example,
            'solution': solution,
            'hint': hint,
            'hint_price': hint_price,
            'reward': reward,
            'required_level': lvl,
            'difficulty': difficulty,
            'allow_write': allow_write,
            'is_level_test': is_test,
            'required_tokens': REQUIRED_TOKENS.get(slug, required_tokens),
            'db_name': db_name or REQUIRED_TOKENS.get(slug + '_db', ''),
            'reference_solution': reference,
            'order': order if order is not None else len(tasks) + 1,
        })

    # Python — уровень 1 (easy)
    for title, slug, desc, ex, sol, hint in build_python_tasks():
        add(title, slug, desc, ex, sol, hint, 1, 5, Task.Type.PYTHON, Task.Difficulty.EASY)

    # Python — уровень 2 (medium)
    for title, slug, desc, ex, sol, hint in build_python_medium():
        add(title, slug, desc, ex, sol, hint, 2, 8, Task.Type.PYTHON, Task.Difficulty.MEDIUM)

    # Python — уровень 3 (hard)
    for title, slug, desc, ex, sol, hint in build_python_hard():
        add(title, slug, desc, ex, sol, hint, 3, 12, Task.Type.PYTHON, Task.Difficulty.HARD)

    # Python — extra (уровень 2)
    for title, slug, desc, ex, sol, hint in build_python_extra():
        add(title, slug, desc, ex, sol, hint, 2, 8, Task.Type.PYTHON, Task.Difficulty.MEDIUM)

    # SQL — уровень 1 (easy)
    for title, slug, desc, ex, sol, hint in build_sql_basic():
        add(title, slug, desc, ex, sol, hint, 1, 5, Task.Type.SQL, Task.Difficulty.EASY)

    # SQL — уровень 2 (medium)
    for title, slug, desc, ex, sol, hint in build_sql_medium():
        add(title, slug, desc, ex, sol, hint, 2, 8, Task.Type.SQL, Task.Difficulty.MEDIUM)

    # SQL — уровень 3 (hard)
    for title, slug, desc, ex, sol, hint in build_sql_hard():
        add(title, slug, desc, ex, sol, hint, 3, 12, Task.Type.SQL, Task.Difficulty.HARD)

    # SQL — extra (уровень 2-3)
    for title, slug, desc, ex, sol, hint in build_sql_extra():
        add(title, slug, desc, ex, sol, hint, 2, 8, Task.Type.SQL, Task.Difficulty.MEDIUM)

    # Транзакции — allow_write
    for title, slug, desc, ex, sol, hint, allow_write in build_transaction_tasks():
        add(title, slug, desc, ex, sol, hint, 2, 10, Task.Type.SQL, Task.Difficulty.MEDIUM, allow_write=allow_write)

    # Тесты уровня
    for title, slug, desc, ex, sol, hint, lvl, reward, *rest in build_level_tests():
        allow_write = rest[0] if rest else False
        diff = Task.Difficulty.HARD if allow_write else Task.Difficulty.MEDIUM
        add(title, slug, desc, ex, sol, hint, lvl, reward,
            Task.Type.SQL if allow_write else Task.Type.PYTHON, diff,
            allow_write=allow_write, is_test=True)

    # Реальные задачи курса (Python+PostgreSQL воркбук, dvdrental)
    for d in build_real_python_tasks():
        add(d['title'], d['slug'], d['description'], d['example'], d['solution'],
            d['hint'], 1, 5, Task.Type.PYTHON, Task.Difficulty.EASY,
            db_name='dvdrental', required_tokens=d['token'],
            reference=d.get('reference', ''))

    # Чистые Python-задачи курса (OOP/полиморфизм/словари) — без БД
    for d in build_pure_python_tasks():
        add(d['title'], d['slug'], d['description'], d['example'], d['solution'],
            d['hint'], 1, 5, Task.Type.PYTHON, Task.Difficulty.EASY,
            reference=d.get('reference', ''))

    return tasks
def build_real_python_tasks():
    """Реальные задачи из курсового Python+PostgreSQL воркбука (dvdrental).

    Условия и правильные решения — из твоего реального воркбука
    (Python_PostgreSQL_Practice_Workbook_dvdrental.pdf). Проверка: вывод ученика
    сравнивается с выводом эталонного решения (tasks/workbook_solutions.py),
    запущенного на реальной dvdrental. Для задач, требующих БД, в globals песочницы
    вливается DB_DSN (psycopg.connect(DB_DSN)).
    """
    from tasks.workbook_solutions import ALL_SOLS, EXACT_SOLS

    meta = {
        1: ("PostgreSQL ga ulanish",
            "Python dasturidan dvdrental bazasiga ulaning. Ulanish muvaffaqiyatli bo'lsa konsolga xabar chiqaring.",
            "Database connected", "psycopg", "Connection string yoki alohida host/dbname/user/password parametrlaridan foydalaning."),
        2: ("Cursor yaratish va SELECT 1",
            "Connection ichidan cursor yarating va SELECT 1 querysini bajaring.",
            "1", "psycopg", "fetchone() dan foydalaning."),
        3: ("Bitta actorni olish",
            "actor_id=1 bo'lgan actorning first_name va last_name qiymatlarini Python orqali oling.",
            "PENELOPE GUINESS", "psycopg", "SQL ichiga f-string bilan ID joylamang — parametrli query yozing."),
        4: ("Barcha kategoriyalarni olish",
            "category jadvalidagi barcha category_name qiymatlarini Python list sifatida oling.",
            "[(1,'Action'), ...]", "psycopg", "fetchall() ishlating."),
        5: ("Film title bo'yicha qidirish",
            "Berilgan title bo'yicha filmni toping va uning ma'lumotlarini chiqaring.",
            "film ma'lumotlari", "psycopg", "Placeholder (%s) ishlating."),
        6: ("Narxi katta filmlar",
            "rental_rate qiymati berilgan qiymatdan katta filmlarni chiqaring.",
            "mos filmlar ro'yxati", "psycopg", "Decimal bilan ishlashga e'tibor bering."),
        7: ("Yangi actor qo'shish",
            "Python orqali yangi actor qo'shing va transactionni commit qiling.",
            "actor yaratildi", "psycopg", "INSERT parametrli bo'lsin."),
        8: ("INSERT dan keyin ID olish",
            "Yangi actor qo'shing va yaratilgan actor_id ni oling (RETURNING).",
            "Yangi actor_id", "psycopg", "fetchone()[0] yoki row factory ishlating."),
        9: ("Actor ismini yangilash",
            "actor_id va yangi first_name qabul qilib actorni yangilang.",
            "1 row updated", "psycopg", "cursor.rowcount ni tekshiring."),
        10: ("Actor o'chirish",
            "actor_id orqali actorni o'chiring. Foreign key sabab o'chmasa xatoni boshqaring.",
            "deleted yoki cannot delete", "psycopg", "Database exceptionni ushlang."),
        11: ("Customer fullname chiqarish",
            "customer_id bo'yicha first_name va last_name ni olib, Python ichida full_name hosil qiling.",
            "Full Name: ...", "psycopg", "SQL va Python mas'uliyatini ajrating."),
        12: ("Film + category JOIN",
            "film_id bo'yicha film title va category nomini oling (JOIN).",
            "title, category", "psycopg", "JOINni SQLda bajaring."),
        13: ("Customer umumiy to'lovi",
            "customer_id bo'yicha jami payment amount ni hisoblab chiqaring (SUM).",
            "total_amount", "psycopg", "SUM NULL qaytarishi mumkin — 0 ga fallback qiling."),
    }

    items = []
    for num in sorted(meta):
        title, desc, expected, tok, hint = meta[num]
        item = ALL_SOLS[num]
        code = item[0] if isinstance(item, tuple) else item
        is_exact = num in EXACT_SOLS
        # В solution кладём ОЖИДАЕМЫЙ ВЫВОД (точная проверка) или заглушку (маркерная).
        solution_text = expected if is_exact else "(проверка по выполнению на БД)"
        slug = "wb-py-%02d" % num
        items.append({
            'num': num,
            'title': "%02d. %s" % (num, title),
            'slug': slug,
            'description': desc,
            'example': "Kutilgan natija:\n" + expected,
            'solution': solution_text,
            'hint': hint,
            'reference': code,
            'is_exact': is_exact,
            'token': tok,
        })
    return items


def build_pure_python_tasks():
    """Чистые Python-задачи из курса (OOP, полиморфизм, словари) — БЕЗ БД.

    Условия собраны из твоих курсовых PDF (klass_masalalari, Polimorfizm,
    Dictionary OOP). Решения self-contained: ученик пишет класс/функцию и
    выводит результат, который сравнивается с эталоном (workbook_solutions не
    нужен — вывод детерминированный).
    """
    # (title, slug, desc, example, solution_stdout, hint, reference_code)
    data = [
        ("IkkiSon klassi",
         "pure-ikki-son",
         "Sоздай класс IkkiSon(a, b) с методом yigindi(), возвращающим a + b. "
         "Выведи результат для IkkiSon(3, 4).",
         "Вывод:\n7",
         "7",
         "Метод должен возвращать значение через return, а не print внутри.",
         "class IkkiSon:\n    def __init__(self, a, b):\n        self.a = a\n        self.b = b\n    def yigindi(self):\n        return self.a + self.b\nprint(IkkiSon(3, 4).yigindi())"),

        ("Uchburchak yuzasi",
         "pure-uchburchak",
         "Создай класс Uchburchak(a, b, c) с методом yuza() (площадь по Герону).\n"
         "Выведи yuza() для сторон 3, 4, 5.",
         "Вывод:\n6.0",
         "6.0",
         "p = (a+b+c)/2; sqrt(p*(p-a)*(p-b)*(p-c)).",
         "import math\nclass Uchburchak:\n    def __init__(self, a, b, c):\n        self.a, self.b, self.c = a, b, c\n    def yuza(self):\n        p = (self.a + self.b + self.c) / 2\n        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))\nprint(Uchburchak(3, 4, 5).yuza())"),

        ("Eng katta va eng kichik",
         "pure-eng-katta",
         "Напиши функцию eng(a, b, c), возвращающую (max, min). Выведи eng(7, 2, 9).",
         "Вывод:\n(9, 2)",
         "(9, 2)",
         "Используй встроенные max() и min().",
         "def eng(a, b, c):\n    return max(a, b, c), min(a, b, c)\nprint(eng(7, 2, 9))"),

        ("Словарь статистики",
         "pure-dict-stats",
         "Дан список чисел. Выведи словарь {'sum': сумма, 'count': количество} "
         "для [1, 2, 3, 4].",
         "Вывод:\n{'sum': 10, 'count': 4}",
         "{'sum': 10, 'count': 4}",
         "sum() и len() по списку.",
         "nums = [1, 2, 3, 4]\nprint({'sum': sum(nums), 'count': len(nums)})"),

        ("Полиморфизм: животные",
         "pure-polymorphism",
         "Создай базовый класс Animal с методом sound() (возвращает '...'), и класс "
         "Dog, переопределяющий sound() -> 'Woof'. Выведи Dog().sound().",
         "Вывод:\nWoof",
         "Woof",
         "Метод в наследнике переопределяет метод родителя.",
         "class Animal:\n    def sound(self):\n        return '...'\nclass Dog(Animal):\n    def sound(self):\n        return 'Woof'\nprint(Dog().sound())"),

        ("Факториал через рекурсию",
         "pure-factorial",
         "Напиши функцию factorial(n) (рекурсивно). Выведи factorial(5).",
         "Вывод:\n120",
         "120",
         "n * factorial(n-1), база factorial(1)=1.",
         "def factorial(n):\n    return 1 if n <= 1 else n * factorial(n-1)\nprint(factorial(5))"),
    ]

    items = []
    for title, slug, desc, example, solution, hint, reference in data:
        items.append({
            'title': title,
            'slug': slug,
            'description': desc,
            'example': example,
            'solution': solution,
            'hint': hint,
            'reference': reference,
            'db_name': '',
            'token': '',
        })
    return items
