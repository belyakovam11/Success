from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from app_quiz.models import Room

@csrf_exempt
def create_room(request):
    if request.method == 'POST':
        try:
            # Получение данных из POST-запроса
            data = json.loads(request.body)
            room_name = data.get('name')
            player_count = data.get('playerCount')
            theme = data.get('theme')
            answer_time = data.get('answerTime')

            # Проверка наличия всех обязательных параметров
            if not all([room_name, player_count, theme, answer_time]):
                return JsonResponse({'error': 'Все поля обязательны'}, status=400)

            # Создание комнаты и сохранение в базе данных
            room = Room.objects.create(
                name=room_name,
                player_count=player_count,
                theme=theme,
                answer_time=answer_time,
                created_by=request.user if request.user.is_authenticated else None  # Привязка пользователя
            )

            return JsonResponse({'message': 'Комната успешно создана', 'room': room.name})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
@csrf_exempt
def join_room(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            room_name = data.get('roomName')

            # Логика подключения к комнате (например, добавить игрока в комнату)

            return JsonResponse({'message': f'Вы присоединились к комнате {room_name}'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
