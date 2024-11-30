from django.conf import settings
from django.db import models

# Определяем модель комнаты
class Room(models.Model):
    name = models.CharField(max_length=100)
    player_count = models.PositiveIntegerField()
    theme = models.CharField(max_length=100)
    answer_time = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Определяем модель участника комнаты
class RoomParticipant(models.Model):
    user = models.CharField(max_length=100)

    # Ссылка на комнату, к которой принадлежит участник (с удалением участника при удалении комнаты)
    room = models.ForeignKey(Room, related_name='participants', on_delete=models.CASCADE)

    # Дата и время, когда пользователь присоединился к комнате (автоматически устанавливается)
    joined_at = models.DateTimeField(auto_now_add=True)

    # Информация о браузере или устройстве пользователя
    user_agent = models.CharField(max_length=255)

    # Индекс текущего вопроса (начинается с 0)
    current_question_index = models.PositiveIntegerField(default=0)

    # Количество правильных ответов пользователя (по умолчанию 0)
    correct_answers_count = models.PositiveIntegerField(default=0)

    class Meta:
        # Ограничение на уникальную комбинацию пользователя, комнаты и user_agent
        unique_together = ('user', 'room', 'user_agent')


    def __str__(self):
        return f'{self.user} in {self.room.name}'
