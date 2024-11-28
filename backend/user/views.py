from django.http import JsonResponse
from rest_framework import generics
from user.models import CustomUser  # Импортируем кастомную модель пользователя
from user.serializers import UserSerializer  # Импортируем ваш сериализатор
from django.views.decorators.csrf import csrf_exempt
from user.tasks import send_registration_email
from django.contrib.auth import authenticate
import json
import sys
from django.db import connection

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()  # Изменено на CustomUser
    serializer_class = UserSerializer


@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username') # Извлекаем имя пользователя
            email = data.get('email') # Извлекаем почту пользователя
            password = data.get('password') # Извлекаем пароль

            print(f"Username: {username}, Password: {password}")
            sys.stdout.flush()
            if not all([username, email, password]):  # Проверяем, что все поля заполнены
                return JsonResponse({"error": "Все поля обязательны"}, status=400)

            # Создаем нового пользователя с указанными данными
            new_user = CustomUser.objects.create_user(username=username, email=email, password=password)
            
            # После регистрации вызываем асинхронную задачу для отправки письма
            send_registration_email.delay(email)
            
            return JsonResponse({"message": "Успешно зарегистрированы!"}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e: # Обработка других возможных исключений
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=400)

@csrf_exempt
def get_username(request):
    username = request.session.get('username')  # Получаем username из Django сессии
    if not username:
        return JsonResponse({"error": "User is not logged in"}, status=400)

    with connection.cursor() as cursor:  # Используем курсор для выполнения SQL-запроса
        cursor.execute("""
            SELECT 
                rp.user,
                COALESCE(SUM(rp.correct_answers_count), 0) AS rating,
                COALESCE(
                    (SELECT theme 
                     FROM room_roomparticipant AS rp_inner 
                     JOIN room_room AS r ON rp_inner.room_id = r.id 
                     WHERE rp_inner.user = rp.user 
                     GROUP BY theme 
                     ORDER BY COUNT(theme) DESC LIMIT 1), 
                'Нету') AS favorite_category
            FROM room_roomparticipant AS rp
            WHERE rp.user = %s
            GROUP BY rp.user;
        """, [username])

        result = cursor.fetchone()  #Получаем результат запроса

    if result:
        return JsonResponse({
            "username": result[0],
            "rating": result[1],
            "favorite_category": result[2]
        })
    else:
        # Если статистика пользователя не найдена
        return JsonResponse({
            "username": username,
            "rating": 0,
            "favorite_category": "Нет данных"
        })

    
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            user = authenticate(request, username=username, password=password) # Аутентификация пользователя

            if user is not None:
                request.session['username'] = username  # Сохраняем username в Django сессии
                return JsonResponse({"message": "Login successful!"}, status=200)
            else:
                return JsonResponse({"error": "Неверное имя пользователя или пароль."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=400)

