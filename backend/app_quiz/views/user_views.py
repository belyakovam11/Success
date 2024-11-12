from django.http import JsonResponse
from rest_framework import generics
from app_quiz.models import CustomUser  # Импортируем кастомную модель пользователя
from app_quiz.serializers import UserSerializer  # Импортируем ваш сериализатор
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from app_quiz.models import CustomUser  # Импортируем кастомную модель пользователя
from app_quiz.serializers import UserSerializer  # Импортируем ваш сериализатор
from app_quiz.tasks import send_registration_email
import json
import sys





class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()  # Изменено на CustomUser
    serializer_class = UserSerializer



@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            print(f"Username: {username}, Password: {password}")
            sys.stdout.flush()
            if not all([username, email, password]):
                return JsonResponse({"error": "Все поля обязательны"}, status=400)

            # Создаем нового пользователя
            new_user = CustomUser.objects.create_user(username=username, email=email, password=password)
            
            # После успешной регистрации вызываем асинхронную задачу для отправки письма
            send_registration_email.delay(email)
            
            return JsonResponse({"message": "Успешно зарегистрированы!"}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=400)