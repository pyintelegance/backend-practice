from django.core.management.base import BaseCommand

from tasks.models import Task, Topic


class Command(BaseCommand):
    help = 'Наполнение базы frontend-задачами (HTML, CSS, JavaScript)'

    def handle(self, *args, **options):
        topic, _ = Topic.objects.get_or_create(
            name='Frontend', slug='frontend', defaults={'order': 4}
        )

        tasks = [
            # === HTML (7 задач) ===
            {
                'title': 'Привет, мир!',
                'slug': 'html-hello-world',
                'description': 'Напиши HTML-страницу, которая выводит текст "Hello, World!" в теге <h1>.',
                'example': '<h1>Hello, World!</h1>',
                'task_type': Task.Type.HTML,
                'required_tokens': 'h1',
                'solution': '<h1>Hello, World!</h1>',
                'hint': 'Используй тег <h1> для заголовка.',
                'difficulty': Task.Difficulty.EASY,
                'order': 1,
            },
            {
                'title': 'Список покупок',
                'slug': 'html-shopping-list',
                'description': 'Создай ненумерованный список (<ul>) из трёх элементов: "Молоко", "Хлеб", "Яйца".',
                'example': '<ul>\n  <li>Молоко</li>\n  <li>Хлеб</li>\n  <li>Яйца</li>\n</ul>',
                'task_type': Task.Type.HTML,
                'required_tokens': 'ul,li',
                'solution': '<ul>\n  <li>Молоко</li>\n  <li>Хлеб</li>\n  <li>Яйца</li>\n</ul>',
                'hint': 'Используй <ul> для списка и <li> для элементов.',
                'difficulty': Task.Difficulty.EASY,
                'order': 2,
            },
            {
                'title': 'Ссылка на сайт',
                'slug': 'html-link',
                'description': 'Создай ссылку (<a>) на https://google.com с текстом "Google".',
                'example': '<a href="https://google.com">Google</a>',
                'task_type': Task.Type.HTML,
                'required_tokens': 'a,href',
                'solution': '<a href="https://google.com">Google</a>',
                'hint': 'Тег <a> с атрибутом href задаёт ссылку.',
                'difficulty': Task.Difficulty.EASY,
                'order': 3,
            },
            {
                'title': 'Изображение',
                'slug': 'html-image',
                'description': 'Вставь изображение (<img>) с src="photo.jpg" и alt="Фото".',
                'example': '<img src="photo.jpg" alt="Фото">',
                'task_type': Task.Type.HTML,
                'required_tokens': 'img,src,alt',
                'solution': '<img src="photo.jpg" alt="Фото">',
                'hint': 'Тег <img> — самозакрывающийся, нужен src и alt.',
                'difficulty': Task.Difficulty.EASY,
                'order': 4,
            },
            {
                'title': 'Форма входа',
                'slug': 'html-login-form',
                'description': 'Создай форму (<form>) с полем ввода для email и кнопкой "Войти".',
                'example': '<form>\n  <input type="email" name="email">\n  <button type="submit">Войти</button>\n</form>',
                'task_type': Task.Type.HTML,
                'required_tokens': 'form,input,button',
                'solution': '<form>\n  <input type="email" name="email">\n  <button type="submit">Войти</button>\n</form>',
                'hint': 'Используй <form>, <input> и <button>.',
                'difficulty': Task.Difficulty.MEDIUM,
                'order': 5,
            },
            {
                'title': 'Таблица пользователей',
                'slug': 'html-table',
                'description': 'Создай таблицу (<table>) с заголовком "Имя" и одной строкой данных "Али".',
                'example': '<table>\n  <tr><th>Имя</th></tr>\n  <tr><td>Али</td></tr>\n</table>',
                'task_type': Task.Type.HTML,
                'required_tokens': 'table,tr,th,td',
                'solution': '<table>\n  <tr><th>Имя</th></tr>\n  <tr><td>Али</td></tr>\n</table>',
                'hint': '<table> → <tr> (строка) → <th> (заголовок) или <td> (данные).',
                'difficulty': Task.Difficulty.MEDIUM,
                'order': 6,
            },
            {
                'title': 'Страница с секциями',
                'slug': 'html-sections',
                'description': 'Создай страницу с тремя секциями: <header>, <main>, <footer>. В каждой по одному заголовку <h2>.',
                'example': '<header><h2>Шапка</h2></header>\n<main><h2>Контент</h2></main>\n<footer><h2>Подвал</h2></footer>',
                'task_type': Task.Type.HTML,
                'required_tokens': 'header,main,footer,h2',
                'solution': '<header><h2>Шапка</h2></header>\n<main><h2>Контент</h2></main>\n<footer><h2>Подвал</h2></footer>',
                'hint': 'Используй семантические теги HTML5.',
                'difficulty': Task.Difficulty.MEDIUM,
                'order': 7,
            },

            # === CSS (7 задач) ===
            {
                'title': 'Цвет текста',
                'slug': 'css-text-color',
                'description': 'Сделай текст красным (color: red) для элемента с классом .warning.',
                'example': '.warning { color: red; }',
                'task_type': Task.Type.CSS,
                'required_tokens': 'color',
                'solution': '.warning { color: red; }',
                'hint': 'Свойство color задаёт цвет текста.',
                'difficulty': Task.Difficulty.EASY,
                'order': 1,
            },
            {
                'title': 'Фон страницы',
                'slug': 'css-background',
                'description': 'Задай фон страницы (body) светло-серым цветом (#f0f0f0).',
                'example': 'body { background-color: #f0f0f0; }',
                'task_type': Task.Type.CSS,
                'required_tokens': 'background-color',
                'solution': 'body { background-color: #f0f0f0; }',
                'hint': 'Свойство background-color задаёт цвет фона.',
                'difficulty': Task.Difficulty.EASY,
                'order': 2,
            },
            {
                'title': 'Размер шрифта',
                'slug': 'css-font-size',
                'description': 'Установи размер шрифта 24px для заголовка <h1>.',
                'example': 'h1 { font-size: 24px; }',
                'task_type': Task.Type.CSS,
                'required_tokens': 'font-size',
                'solution': 'h1 { font-size: 24px; }',
                'hint': 'Свойство font-size задаёт размер шрифта.',
                'difficulty': Task.Difficulty.EASY,
                'order': 3,
            },
            {
                'title': 'Отступы',
                'slug': 'css-padding',
                'description': 'Добавь внутренний отступ 20px для блока с классом .card.',
                'example': '.card { padding: 20px; }',
                'task_type': Task.Type.CSS,
                'required_tokens': 'padding',
                'solution': '.card { padding: 20px; }',
                'hint': 'Свойство padding задаёт внутренний отступ.',
                'difficulty': Task.Difficulty.EASY,
                'order': 4,
            },
            {
                'title': 'Граница элемента',
                'slug': 'css-border',
                'description': 'Добавь границу 1px solid black для элемента с классом .box.',
                'example': '.box { border: 1px solid black; }',
                'task_type': Task.Type.CSS,
                'required_tokens': 'border',
                'solution': '.box { border: 1px solid black; }',
                'hint': 'Свойство border задаёт границу: ширина, стиль, цвет.',
                'difficulty': Task.Difficulty.MEDIUM,
                'order': 5,
            },
            {
                'title': 'Flexbox центрирование',
                'slug': 'css-flexbox-center',
                'description': 'Отцентрируй элемент .container по горизонтали и вертикали с помощью flexbox.',
                'example': '.container { display: flex; justify-content: center; align-items: center; }',
                'task_type': Task.Type.CSS,
                'required_tokens': 'display:flex,justify-content,align-items',
                'solution': '.container { display: flex; justify-content: center; align-items: center; }',
                'hint': 'Используй display: flex, justify-content и align-items.',
                'difficulty': Task.Difficulty.MEDIUM,
                'order': 6,
            },
            {
                'title': 'Адаптивная сетка',
                'slug': 'css-grid',
                'description': 'Создай CSS-сетку (grid) с двумя колонками одинаковой ширины для .grid.',
                'example': '.grid { display: grid; grid-template-columns: 1fr 1fr; }',
                'task_type': Task.Type.CSS,
                'required_tokens': 'display:grid,grid-template-columns',
                'solution': '.grid { display: grid; grid-template-columns: 1fr 1fr; }',
                'hint': 'Используй display: grid и grid-template-columns.',
                'difficulty': Task.Difficulty.HARD,
                'order': 7,
            },

            # === JavaScript (7 задач) ===
            {
                'title': 'Привет, мир!',
                'slug': 'js-hello-world',
                'description': 'Выведи "Hello, World!" в консоль с помощью console.log.',
                'example': 'console.log("Hello, World!");',
                'task_type': Task.Type.JAVASCRIPT,
                'required_tokens': 'console.log',
                'solution': 'Hello, World!',
                'hint': 'Используй console.log("текст") для вывода.',
                'difficulty': Task.Difficulty.EASY,
                'order': 1,
            },
            {
                'title': 'Переменная',
                'slug': 'js-variable',
                'description': 'Создай переменную name со значением "Али" и выведи её в консоль.',
                'example': 'let name = "Али";\nconsole.log(name);',
                'task_type': Task.Type.JAVASCRIPT,
                'required_tokens': 'let,console.log',
                'solution': 'Али',
                'hint': 'Используй let name = "значение" для создания переменной.',
                'difficulty': Task.Difficulty.EASY,
                'order': 2,
            },
            {
                'title': 'Арифметика',
                'slug': 'js-math',
                'description': 'Вычисли сумму 15 + 27 и выведи результат в консоль.',
                'example': 'console.log(15 + 27);',
                'task_type': Task.Type.JAVASCRIPT,
                'required_tokens': 'console.log',
                'solution': '42',
                'hint': 'Используй оператор + для сложения.',
                'difficulty': Task.Difficulty.EASY,
                'order': 3,
            },
            {
                'title': 'Условие',
                'slug': 'js-if-else',
                'description': 'Если переменная age больше 18, выведи "Дорослый", иначе "Несовершеннолетний".',
                'example': 'let age = 20;\nif (age > 18) {\n  console.log("Дорослый");\n} else {\n  console.log("Несовершеннолетний");\n}',
                'task_type': Task.Type.JAVASCRIPT,
                'required_tokens': 'if,else,console.log',
                'solution': 'Дорослый',
                'hint': 'Используй if (условие) { ... } else { ... }.',
                'difficulty': Task.Difficulty.MEDIUM,
                'order': 4,
            },
            {
                'title': 'Цикл',
                'slug': 'js-loop',
                'description': 'Выведи числа от 1 до 5 (каждое с новой строки) с помощью цикла for.',
                'example': 'for (let i = 1; i <= 5; i++) {\n  console.log(i);\n}',
                'task_type': Task.Type.JAVASCRIPT,
                'required_tokens': 'for,console.log',
                'solution': '1\n2\n3\n4\n5',
                'hint': 'Используй for (let i = 1; i <= 5; i++).',
                'difficulty': Task.Difficulty.MEDIUM,
                'order': 5,
            },
            {
                'title': 'Функция',
                'slug': 'js-function',
                'description': 'Создай функцию add(a, b), которая возвращает сумму двух чисел. Вызови add(3, 4) и выведи результат.',
                'example': 'function add(a, b) {\n  return a + b;\n}\nconsole.log(add(3, 4));',
                'task_type': Task.Type.JAVASCRIPT,
                'required_tokens': 'function,return,console.log',
                'solution': '7',
                'hint': 'Используй function имя(параметры) { return значение; }.',
                'difficulty': Task.Difficulty.MEDIUM,
                'order': 6,
            },
            {
                'title': 'Массив',
                'slug': 'js-array',
                'description': 'Создай массив [10, 20, 30] и выведи его длину в консоль.',
                'example': 'let arr = [10, 20, 30];\nconsole.log(arr.length);',
                'task_type': Task.Type.JAVASCRIPT,
                'required_tokens': 'length,console.log',
                'solution': '3',
                'hint': 'Массив создаётся через [], длина — .length.',
                'difficulty': Task.Difficulty.HARD,
                'order': 7,
            },
        ]

        created_count = 0
        updated_count = 0
        for data in tasks:
            slug = data['slug']
            obj, created = Task.objects.get_or_create(
                slug=slug, defaults={**data, 'topic': topic}
            )
            if created:
                created_count += 1
            else:
                for field, value in data.items():
                    setattr(obj, field, value)
                obj.topic = topic
                obj.save()
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Frontend задачи: создано={created_count}, обновлено={updated_count}, '
            f'всего задач в теме={Task.objects.filter(topic=topic).count()}'
        ))
