# Generated by Django 4.2 on 2024-11-21 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_quiz', '0002_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.RemoveField(
            model_name='room',
            name='created_by',
        ),
    ]