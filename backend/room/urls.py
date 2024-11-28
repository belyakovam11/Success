from django.urls import path
from room.views import create_room, join_room
from room.views import rooms, get_room_participants
from trivia.views import get_room_questions
from trivia.services import SubmitAnswerView

urlpatterns = [
    path('api/create-room', create_room, name='create_room'),  # Для создания комнаты
    path('api/join-room', join_room, name='join_room'),  # Для присоединения к комнате
    path('api/rooms', rooms, name='rooms'),  # Для получения списка комнат
    path('api/room/<str:room_name>/participants/', get_room_participants, name='get_room_participants'), # Путь для получения списка участников конкретной комнаты
    path('api/room/<str:room_name>/questions/', get_room_questions, name='get_room_questions'),  # Путь для получения вопросов для конкретной комнаты. 
    path('api/room/<str:room_name>/submit-answer/', SubmitAnswerView.as_view(), name='submit-answer'),  # Путь для отправки ответа на вопрос в комнате 
]
