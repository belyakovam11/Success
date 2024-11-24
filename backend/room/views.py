from django.http import JsonResponse
from room.models import Room, RoomParticipant
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def rooms(request):
    # Получаем все комнаты через ORM
    rooms_queryset = Room.objects.all()
    
    # Преобразуем queryset в список словарей
    rooms = []
    for room in rooms_queryset:
        rooms.append({
            'id': room.id,
            'name': room.name,
            'player_count': room.player_count,
            'theme': room.theme,
            'answer_time': room.answer_time,
            'created_at': room.created_at.isoformat(),  # Преобразуем datetime в строку
        })
    
    # Возвращаем JSON ответ
    return JsonResponse(rooms, safe=False)

def get_room_participants(request, room_name):
    try:
        room = Room.objects.get(name=room_name)
        participants = RoomParticipant.objects.filter(room=room).values('user', 'joined_at')
        return JsonResponse(list(participants), safe=False)
    except Room.DoesNotExist:
        return JsonResponse({'error': 'Room not found'}, status=404)


@csrf_exempt
def join_room(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            room_name = data.get('roomName')
            username = data.get('username')  # Получаем имя пользователя из данных

            # Проверка существования комнаты
            room = Room.objects.filter(name=room_name).first()
            if not room:
                return JsonResponse({'error': 'Комната не найдена'}, status=404)

            # Проверка лимита игроков
            current_player_count = room.participants.count()
            if current_player_count >= room.player_count:
                return JsonResponse({'error': 'Слишком много вопрсов заданно'}, status=400)

            # Извлекаем user-agent
            user_agent = request.headers.get('User-Agent', 'Unknown')

            # Добавление пользователя в комнату
            participant, created = RoomParticipant.objects.get_or_create(
                user=username, 
                room=room,
                defaults={'user_agent': user_agent}
            )

            return JsonResponse({'message': f'Вы присоединились к комнате {room_name}', 'roomId': room.id, 'userId': username})
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

            print("Полученные данные:", data)  # Логируем данные

            # Проверка, что все поля заполнены
            if not all([room_name, player_count, theme, answer_time]):
                return JsonResponse({'error': 'Все поля обязательны'}, status=400)

            # Проверка на существование комнаты с таким же названием
            if Room.objects.filter(name=room_name).exists():
                return JsonResponse({'error': 'Комната с таким названием уже существует'}, status=400)

            # Создание новой комнаты
            room = Room.objects.create(
                name=room_name,
                player_count=player_count,
                theme=theme,
                answer_time=answer_time
            )

            return JsonResponse({
                'message': 'Комната успешно создана',
                'room': {
                    'id': room.id,
                    'name': room.name,
                    'playerCount': room.player_count,
                    'theme': room.theme,
                    'answerTime': room.answer_time,
                }
            })
        except Exception as e:
            print("Ошибка:", str(e))  # Логируем ошибку
            return JsonResponse({'error': str(e)}, status=400)
