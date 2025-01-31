from django.db import models
from rest_framework import serializers


class Task(models.Model):
    id = models.UUIDField(primary_key=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
     model = Task
     fields ='__all__'
