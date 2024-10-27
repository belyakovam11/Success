from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from rest_framework import generics
from app_quiz.models import CustomUser  # Импортируем кастомную модель пользователя
from app_quiz.serializers import UserSerializer  # Импортируем ваш сериализатор
import json
from django.http import JsonResponse
from django.shortcuts import render
from app_quiz.models import CustomUser

def get_time(request):
    data = {
        "Name": "TEST",
        "Age": 30,
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "programming": "Python"
    }
    return JsonResponse(data)

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()  # Изменено на CustomUser
    serializer_class = UserSerializer

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_user = CustomUser.objects.create_user(email=email, password=password)  # Создаем пользователя
        return JsonResponse({"message": "User created successfully!"})  # Ответ о создании пользователя
    return render(request, 'registration.html')  # Возврат формы регистрации

from django.db import connection
from django.core.exceptions import ObjectDoesNotExist

def get_db_status(request):
    try:
        # Пытаемся выполнить простой запрос к базе данных
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({'status': 'ok', 'message': 'Database is up and running.'})
    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Database does not exist.'}, status=500)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def register_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Получаем данные из JSON
        email = data.get('email')
        password = data.get('password')
        new_user = CustomUser.objects.create_user(email=email, password=password)
        return JsonResponse({"message": "User created successfully!"})
    return render(request, 'registration.html')

