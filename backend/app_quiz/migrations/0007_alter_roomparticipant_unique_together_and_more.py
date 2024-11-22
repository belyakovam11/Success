# Generated by Django 4.2 on 2024-11-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_quiz', '0006_remove_question_room_question_theme'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='roomparticipant',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='roomparticipant',
            name='user_agent',
            field=models.CharField(default='Unknown', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='roomparticipant',
            unique_together={('user', 'room', 'user_agent')},
        ),
    ]
