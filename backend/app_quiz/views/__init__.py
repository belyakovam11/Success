from django.http import JsonResponse
import sys
import requests

session = requests.Session() 

def get_time(request):
    if request.method == 'GET':
        session_id = session.cookies.get('sessionid')  # Получаем sessionid из cookies сессии requests
        print("Session ID:", session_id)
        sys.stdout.flush()  # Сброс вывода

        username = session.cookies.get('username')  # Получаем имя из cookies сессии requests
        print("Username in session:", username)
        sys.stdout.flush()  # Сброс вывода

        if username:
            return JsonResponse({"username": username}, status=200)
        else:
            return JsonResponse({"error": "Username not found in session."}, status=404)

    return JsonResponse({"error": "Invalid request method."}, status=400)