from django.conf import settings
from django.db import models

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


