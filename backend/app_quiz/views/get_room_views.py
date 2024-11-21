from django.http import JsonResponse
from app_quiz.models import Room

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
