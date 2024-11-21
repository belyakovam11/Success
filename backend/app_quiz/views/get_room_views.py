from django.http import JsonResponse
from app_quiz.models import Room, RoomParticipant

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