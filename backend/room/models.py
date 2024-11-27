# Импортируем настройки проекта Django
from django.conf import settings

# Импортируем базовый класс моделей Django для работы с базой данных
from django.db import models

# Определяем модель комнаты
class Room(models.Model):
    # Название комнаты (строка длиной до 100 символов)
    name = models.CharField(max_length=100)

    # Количество игроков в комнате (положительное целое число)
    player_count = models.PositiveIntegerField()

    # Тема комнаты (строка длиной до 100 символов)
    theme = models.CharField(max_length=100)

    # Время на ответ в секундах (положительное целое число)
    answer_time = models.PositiveIntegerField()

    # Дата и время создания комнаты (автоматически устанавливается при создании записи)
    created_at = models.DateTimeField(auto_now_add=True)

    # Метод возвращает строковое представление объекта (имя комнаты)
    def __str__(self):
        return self.name

# Определяем модель участника комнаты
class RoomParticipant(models.Model):
    # Имя пользователя (строка длиной до 100 символов)
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

    # Класс для метаинформации модели
    class Meta:
        # Ограничение на уникальную комбинацию пользователя, комнаты и user_agent
        unique_together = ('user', 'room', 'user_agent')

    # Метод возвращает строковое представление объекта (пользователь и его комната)
    def __str__(self):
        return f'{self.user} in {self.room.name}'
