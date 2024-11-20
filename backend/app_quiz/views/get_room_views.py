from django.http import JsonResponse
from app_quiz.models import Room

def user_rooms(request):
    try:
        rooms = Room.objects.filter(created_by=request.user)  # Фильтруем комнаты по пользователю
        rooms_data = []
        for room in rooms:
            rooms_data.append({
                'id': room.id,
                'name': room.name,
                'playerCount': room.player_count,
                'theme': room.theme,
                'answerTime': room.answer_time,
                'createdBy': room.created_by.username if room.created_by else None,
                'createdAt': room.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            })
        return JsonResponse({'rooms': rooms_data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
