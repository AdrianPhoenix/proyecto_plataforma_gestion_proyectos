from django.contrib import admin
from .models import Project, ProjectMember

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_by', 'start_date', 'end_date', 'created_at')
    list_filter = ('status', 'created_at', 'start_date', 'end_date')
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'

@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'role', 'joined_at')
    list_filter = ('role', 'joined_at')
    search_fields = ('project__name', 'user__username')
