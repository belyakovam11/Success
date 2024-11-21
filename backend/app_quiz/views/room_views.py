from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from app_quiz.models import Room

@csrf_exempt
def create_room(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            room_name = data.get('name')
            player_count = data.get('playerCount')
            theme = data.get('theme')
            answer_time = data.get('answerTime')

            # Проверка, что все поля заполнены
            if not all([room_name, player_count, theme, answer_time]):
                return JsonResponse({'error': 'Все поля обязательны'}, status=400)

            # Проверка на существование комнаты с таким же названием
            if Room.objects.filter(name=room_name).exists():
                return JsonResponse({'error': 'Комната с таким названием уже существует'}, status=400)

            # Создание комнаты
            room = Room.objects.create(
                name=room_name,
                player_count=player_count,
                theme=theme,
                answer_time=answer_time,
                created_by=request.user if request.user.is_authenticated else None
            )

            # Добавление текущего пользователя как участника
            if request.user.is_authenticated:
                room.participants.add(request.user)

            return JsonResponse({
                'message': 'Комната успешно создана',
                'room': {
                    'id': room.id,
                    'name': room.name,
                    'playerCount': room.player_count,
                    'theme': room.theme,
                    'answerTime': room.answer_time,
                    'createdBy': room.created_by.username if room.created_by else None,
                    'createdAt': room.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                }
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)



@csrf_exempt
def join_room(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            room_name = data.get('roomName')

            # Проверка существования комнаты
            room = Room.objects.filter(name=room_name).first()
            if not room:
                return JsonResponse({'error': 'Комната не найдена'}, status=404)

            # Проверка лимита игроков
            current_player_count = room.participants.count()
            if current_player_count >= room.player_count:
                return JsonResponse({'error': 'Лимит игроков в комнате исчерпан'}, status=400)

            # Добавление пользователя в комнату
            if request.user.is_authenticated:
                room.participants.add(request.user)

            return JsonResponse({'message': f'Вы присоединились к комнате {room_name}'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        

@csrf_exempt
def create_room(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            room_name = data.get('name')
            player_count = data.get('playerCount')
            theme = data.get('theme')
            answer_time = data.get('answerTime')

            # Проверка, что все поля заполнены
            if not all([room_name, player_count, theme, answer_time]):
                return JsonResponse({'error': 'Все поля обязательны'}, status=400)

            # Проверка на существование комнаты с таким же названием
            if Room.objects.filter(name=room_name).exists():
                return JsonResponse({'error': 'Комната с таким названием уже существует'}, status=400)

            # Проверка на существование пользователя, если он аутентифицирован
            created_by = request.user if request.user.is_authenticated else None

            # Создание новой комнаты
            room = Room.objects.create(
                name=room_name,
                player_count=player_count,
                theme=theme,
                answer_time=answer_time,
                created_by=created_by  # Сохраняем пользователя, если он аутентифицирован
            )

            # Возвращаем информацию о созданной комнате
            return JsonResponse({
                'message': 'Комната успешно создана',
                'room': {
                    'id': room.id,
                    'name': room.name,
                    'playerCount': room.player_count,
                    'theme': room.theme,
                    'answerTime': room.answer_time,
                    'createdBy': room.created_by.username if room.created_by else None,
                    'createdAt': room.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                }
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)