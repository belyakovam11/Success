from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Можно добавить дополнительные поля при необходимости
    pass


class Room(models.Model):
    name = models.CharField(max_length=100)
    player_count = models.PositiveIntegerField()
    theme = models.CharField(max_length=100)
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,  # Кастомная модель пользователя
        related_name='joined_rooms',
        blank=True
    )
    answer_time = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_rooms',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
