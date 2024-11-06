from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from rest_framework import generics
from app_quiz.models import CustomUser  # Импортируем кастомную модель пользователя
from app_quiz.serializers import UserSerializer  # Импортируем ваш сериализатор
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
import json
import sys

def get_time(request):
    if request.method in ['POST', 'GET']:  # Поддержка как POST, так и GET запросов
        try:
            # Проверяем, существует ли пользователь с именем 'test'
            if CustomUser.objects.filter(username='test').exists():
                return JsonResponse({"message": "USER 'test' IS ALREDY!"}, status=200)
            
            # Создаем нового пользователя с именем 'test'
            new_user = CustomUser.objects.create_user(
                username='test', 
                email='test@example.com', 
                password='test123'
            )
            return JsonResponse({"message": "USER  'test' CREATED"}, status=201)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid request method."}, status=400)

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()  # Изменено на CustomUser
    serializer_class = UserSerializer

def get_db_status(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({'status': 'ok', 'message': 'Database is up and running.'})
    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Database does not exist.'}, status=500)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt  # Используйте с осторожностью
def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            print(f"Username: {username}, Password: {password}")
            sys.stdout.flush()  # Сброс вывода
            if not all([username, email, password]):
                return JsonResponse({"error": "Все поля обязательны"}, status=400)

            # Создаем нового пользователя
            new_user = CustomUser.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({"message": "Успешно зарегистрированы!"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=400)

import sys

@csrf_exempt
def login_view(request):
    print("login_view вызван", flush=True)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            print(f"Username: {username}, Password: {password}")
            sys.stdout.flush()  # Сброс вывода

            user = authenticate(request, username=username, password=password)
            print(user)
            sys.stdout.flush()  # Сброс вывода
            if user is not None:
                login(request, user)
                return JsonResponse({"message": "Успешный вход!"}, status=200)
            else:
                return JsonResponse({"error": "Неверное имя пользователя или пароль."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=400)

