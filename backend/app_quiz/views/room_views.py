from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_room(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            room_name = data.get('name')
            player_count = data.get('playerCount')
            theme = data.get('theme')
            answer_time = data.get('answerTime')

            # Логика создания комнаты (например, сохранить в базе данных)

            return JsonResponse({'message': 'Комната успешно создана', 'room': room_name})
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
