from django.conf import settings
from django.db import models
from room.models import RoomParticipant


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