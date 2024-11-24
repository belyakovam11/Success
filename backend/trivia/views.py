from django.http import JsonResponse
from room.models import Room
from trivia.models import Question

def get_room_questions(request, room_name):
    try:
        # Получаем комнату по имени
        room = Room.objects.get(name=room_name)
        
        # Извлекаем количество вопросов из player_count
        question_limit = room.player_count
        
        # Фильтруем вопросы по теме комнаты и ограничиваем их количеством из player_count
        questions = Question.objects.filter(theme=room.theme).order_by('?')[:question_limit]
        
        # Формируем данные для ответа
        question_data = [
            {
                "text": question.text,
                "options": question.get_options_list(),
                "answer_time": question.answer_time,
                "correct_answer": question.correct_answer,
            }
            for question in questions
        ]
        
        return JsonResponse(question_data, safe=False)
    except Room.DoesNotExist:
        return JsonResponse({"error": "Room not found"}, status=404)
