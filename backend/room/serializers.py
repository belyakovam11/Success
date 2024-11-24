# app_quiz/serializers.py
from rest_framework import serializers
from app_quiz.models import RoomParticipant

class RoomParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomParticipant
        fields = ['id', 'user', 'room', 'joined_at']



