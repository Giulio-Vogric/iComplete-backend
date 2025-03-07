# Generated by Django 5.1.6 on 2025-02-17 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('priority', models.IntegerField(default=0)),
                ('tags', models.JSONField()),
            ],
        ),
    ]
