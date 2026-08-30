from django.conf import settings
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Task(models.Model):
    class Difficulty(models.TextChoices):
        EASY = 'easy', 'Easy'
        MEDIUM = 'medium', 'Medium'
        HARD = 'hard', 'Hard'

    class Type(models.TextChoices):
        SQL = 'sql', 'SQL'
        PYTHON = 'python', 'Python'
        HTML = 'html', 'HTML'
        CSS = 'css', 'CSS'
        JAVASCRIPT = 'javascript', 'JavaScript'

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(help_text='Текст задачи для ученика')
    example = models.TextField(blank=True, help_text='Пример ввода/вывода')
    task_type = models.CharField(max_length=10, choices=Type.choices, default=Type.SQL)
    db_name = models.CharField(max_length=64, blank=True, default='dvdrental', help_text='База для SQL-проверки')
    tables = models.CharField(max_length=200, blank=True, help_text='Таблицы для задачи (через запятую)')
    required_tokens = models.CharField(max_length=200, blank=True, help_text='Обязательные элементы в коде (через запятую)')
    allow_write = models.BooleanField(default=False, help_text='Разрешить UPDATE/INSERT/DELETE (для транзакционных задач)')
    solution = models.TextField(help_text='Правильный ответ: SQL-запрос или ожидаемый stdout для Python')
    hint = models.TextField(blank=True, help_text='Подсказка (покупается за монеты)')
    hint_price = models.PositiveIntegerField(default=0, help_text='Цена подсказки в монетах')
    reference_solution = models.TextField(blank=True, help_text='Эталонное решение (Python) для сверки вывода ученика')
    reward = models.PositiveIntegerField(default=5, help_text='Монеты за решение задачи')
    required_level = models.PositiveIntegerField(default=1, help_text='Минимальный уровень для решения (1-5)')
    is_level_test = models.BooleanField(default=False, help_text='Тест уровня: решающий переходит на следующий уровень')
    difficulty = models.CharField(max_length=10, choices=Difficulty.choices, default=Difficulty.EASY)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['topic', 'order', 'title']

    def __str__(self):
        return f'[{self.topic}] {self.title}'


class Submission(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        PASSED = 'passed', 'Passed'
        FAILED = 'failed', 'Failed'
        ERROR = 'error', 'Error'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submissions')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='submissions')
    code = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    feedback = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f'{self.user} -> {self.task} ({self.status})'


class HintPurchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hint_purchases')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='hint_purchases')
    purchased_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-purchased_at']
        unique_together = ('user', 'task')

    def __str__(self):
        return f'{self.user} -> hint {self.task}'