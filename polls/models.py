from django.db import models
from rest_framework import serializers


class Task(models.Model):
    id = models.UUIDField(primary_key=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    tags = models.JSONField()

    objects = models.Manager()


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class Habit(models.Model):
    id = models.UUIDField(primary_key=True)
    creation_date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    desired_pomodoro = models.IntegerField(default=0, null=True)
    time_spent_today = models.IntegerField(default=0)
    total_time_spent = models.IntegerField(default=0)
    schedule = models.JSONField()

    objects = models.Manager()


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
