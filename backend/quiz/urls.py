from django.urls import path
from user.views import login_view, get_username
from user.views import register_view
from room.views import create_room, join_room
from room.views import rooms, get_room_participants
from trivia.views import get_room_questions
from trivia.services import SubmitAnswerView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('get-username/', get_username, name='get_username'),
    path('api/create-room', create_room, name='create_room'),  # Для создания комнаты
    path('api/join-room', join_room, name='join_room'),  # Для присоединения к комнате
    path('api/rooms', rooms, name='rooms'),  # Для получения списка комнат
    path('api/room/<str:room_name>/participants/', get_room_participants, name='get_room_participants'),
    path('api/room/<str:room_name>/questions/', get_room_questions, name='get_room_questions'),
    path('api/room/<str:room_name>/submit-answer/', SubmitAnswerView.as_view(), name='submit-answer'),    
]
