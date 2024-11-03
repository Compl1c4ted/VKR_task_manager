from django.contrib import admin
from .models import Project, Task, User

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptions')
    filter_horizontal = ('assigned_users', )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptions', 'project')

