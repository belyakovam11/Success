# app_quiz/views/get_quiz.py

from django.http import JsonResponse
from app_quiz.models import Room, Question

def get_room_questions(request, room_name):
    try:
        room = Room.objects.get(name=room_name)
        questions = Question.objects.filter(theme=room.theme)  # Фильтрация по теме комнаты
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
