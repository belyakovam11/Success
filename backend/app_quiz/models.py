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
    answer_time = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class RoomParticipant(models.Model):
    user = models.CharField(max_length=100)  # Вместо ForeignKey можно использовать строку для идентификации пользователя
    room = models.ForeignKey(Room, related_name='participants', on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'room')

    def __str__(self):
        return f'{self.user} in {self.room.name}'
