from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField


class Project(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    assigned_users = models.ManyToManyField(User, related_name="projects")

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    # Связь с проектом
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    # Связь пользователя работающего с задачей
    assigned_users = models.ManyToManyField(User, related_name="tasks")

    def __str__(self):
        return f'Название задачи: {self.title}'