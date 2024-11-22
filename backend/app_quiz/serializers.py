# app_quiz/serializers.py
from rest_framework import serializers
from app_quiz.models import CustomUser, RoomParticipant, QuizAnswer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')  # Укажите необходимые поля

class RoomParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomParticipant
        fields = ['id', 'user', 'room', 'joined_at']


from rest_framework import serializers

class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = ['participant', 'question', 'answer']
