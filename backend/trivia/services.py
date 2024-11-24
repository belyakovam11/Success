from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from room.models import RoomParticipant
from trivia.models import Question
from trivia.models import QuizAnswer

class SubmitAnswerView(APIView):
    def post(self, request, room_name):
        user_agent = request.headers.get('User-Agent')
        if not user_agent:
            return Response({"error": "User-Agent header is required"}, status=status.HTTP_400_BAD_REQUEST)

        participant = get_object_or_404(
            RoomParticipant,
            room__name=room_name,
            user_agent=user_agent
        )

        questions = Question.objects.filter(theme=participant.room.theme).order_by('id')
        if participant.current_question_index >= len(questions):
            return Response({"error": "No more questions"}, status=status.HTTP_400_BAD_REQUEST)

        current_question = questions[participant.current_question_index]

        answer_data = request.data.get('answer')
        if not answer_data:
            return Response({"error": "Answer is required"}, status=status.HTTP_400_BAD_REQUEST)

        is_correct = answer_data.strip() == current_question.correct_answer.strip()

        # Сохраняем ответ
        QuizAnswer.objects.create(
            participant=participant,
            question=current_question,
            answer=answer_data,
            is_correct=is_correct
        )

        # Обновляем количество правильных ответов
        if is_correct:
            participant.correct_answers_count += 1

        # Обновляем индекс текущего вопроса
        participant.current_question_index += 1
        participant.save()

        return Response({
            "message": "Answer submitted",
            "is_correct": is_correct,
            "next_question": participant.current_question_index < len(questions),
            "correct_answers_count": participant.correct_answers_count  # Добавляем в ответ
        }, status=status.HTTP_201_CREATED)
