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
    user = models.CharField(max_length=100)
    room = models.ForeignKey(Room, related_name='participants', on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=255)
    current_question_index = models.PositiveIntegerField(default=0)
    correct_answers_count = models.PositiveIntegerField(default=0)  

    class Meta:
        unique_together = ('user', 'room', 'user_agent')

    def __str__(self):
        return f'{self.user} in {self.room.name}'


class Question(models.Model):
    text = models.CharField(max_length=255)  # Текст вопроса
    options = models.CharField(max_length=255)  # Варианты ответа через запятую
    correct_answer = models.CharField(max_length=100)  # Правильный ответ
    answer_time = models.PositiveIntegerField()  # Время на ответ в секундах
    theme = models.CharField(max_length=100)  # Ссылка на тему (например, "Спорт")
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания вопроса

    def __str__(self):
        return self.text

    def get_options_list(self):
        """Возвращает список вариантов из строки options."""
        return self.options.split(',')

class QuizAnswer(models.Model):
    participant = models.ForeignKey(RoomParticipant, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=255)  # Ответ пользователя
    is_correct = models.BooleanField(default=False)  # Проверка правильности ответа
    submitted_at = models.DateTimeField(auto_now_add=True)  # Время отправки ответа

    def __str__(self):
        return f'{self.participant.user} - {self.question.text} - {self.answer}'
