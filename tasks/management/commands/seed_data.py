from django.core.management.base import BaseCommand

from tasks.models import Task, Topic

from .tasks_data import build_all


class Command(BaseCommand):
    help = 'Наполнение базы темами и полным набором задач (~100)'

    def handle(self, *args, **options):
        sql_topic, _ = Topic.objects.get_or_create(name='SQL', slug='sql', defaults={'order': 1})
        python_topic, _ = Topic.objects.get_or_create(name='Python', slug='python', defaults={'order': 2})
        txn_topic, _ = Topic.objects.get_or_create(name='Транзакции', slug='transactions', defaults={'order': 3})

        def pick_topic(task_type, allow_write):
            if task_type == Task.Type.PYTHON:
                return python_topic
            if allow_write:
                return txn_topic
            return sql_topic

        created_count = 0
        updated_count = 0
        for data in build_all():
            slug = data['slug']
            task_type = data['task_type']
            allow_write = data.get('allow_write', False)
            topic = pick_topic(task_type, allow_write)
            obj, created = Task.objects.get_or_create(slug=slug, defaults={**data, 'topic': topic})
            if created:
                created_count += 1
            else:
                for field, value in data.items():
                    setattr(obj, field, value)
                obj.topic = topic
                obj.save()
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Готово: тем={Topic.objects.count()}, задач={Task.objects.count()} '
            f'(создано={created_count}, обновлено={updated_count})'
        ))