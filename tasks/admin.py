from django.contrib import admin

from .models import HintPurchase, Task, Topic, Submission


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'task_type', 'difficulty', 'required_level', 'is_level_test', 'reward', 'hint_price', 'allow_write')
    list_filter = ('topic', 'difficulty', 'task_type', 'is_level_test', 'required_level')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'status', 'submitted_at')
    list_filter = ('status', 'task__topic')


@admin.register(HintPurchase)
class HintPurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'purchased_at')
    list_filter = ('task__topic',)