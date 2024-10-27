# app_quiz/serializers.py
from rest_framework import serializers
from app_quiz.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')  # Укажите необходимые поля
