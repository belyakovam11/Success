# app_quiz/serializers.py
from rest_framework import serializers
from Success.backend.user.models import QuizAnswer

class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = ['participant', 'question', 'answer']
