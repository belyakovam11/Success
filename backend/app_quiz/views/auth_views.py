from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import json
import sys
import requests


session = requests.Session() 

@csrf_exempt
def get_username(request):
    username = session.cookies.get('username')  # Получаем имя из cookies сессии requests
    if username:
        return JsonResponse({"username": username})
    else:
        return JsonResponse({"error": "User is not logged in"}, status=400)


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
            print(f"Authenticated user: {user}")
            sys.stdout.flush()  # Сброс вывода

            if user is not None:
                # Внешняя сессия
                session.cookies.set('username', username)  # Сохраняем username в cookies сессии requests
                print(f"SESSION: {session.cookies.get('username')}")
                sys.stdout.flush()  # Сброс вывода

                # Выводим всю информацию о сессии
                print(f"Session ID: {session.cookies.get('sessionid')}")
                print(f"Session Data: {dict(session.cookies)}")
                sys.stdout.flush()

                # Отправляем успешный ответ
                return JsonResponse({"message": "Login successful!"}, status=200)

            else:
                return JsonResponse({"error": "Неверное имя пользователя или пароль."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=400)
