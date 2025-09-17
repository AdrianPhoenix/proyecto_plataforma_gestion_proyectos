from django.contrib import admin
from .models import Task, TaskComment

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'status', 'assigned_to', 'created_by', 'due_date', 'created_at')
    list_filter = ('status', 'project', 'created_at', 'due_date')
    search_fields = ('name', 'description', 'project__name')
    date_hierarchy = 'created_at'

@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('task__name', 'user__username', 'content')
