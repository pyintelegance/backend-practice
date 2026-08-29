from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100, blank=True)
    points = models.PositiveIntegerField(default=0)
    solved_count = models.PositiveIntegerField(default=0)
    coins = models.PositiveIntegerField(default=0, help_text='Валюта: монеты за решённые задачи')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name or self.user.username