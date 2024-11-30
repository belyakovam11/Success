from django.urls import path
from user.views import login_view, get_username
from user.views import register_view
from room.views import create_room, join_room
from room.views import rooms, get_room_participants
from trivia.views import get_room_questions
from trivia.services import SubmitAnswerView

urlpatterns = [
     # Авторизация и регистрация пользователей
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('get-username/', get_username, name='get_username'),

    # Работа с комнатами
    path('api/create-room', create_room, name='create_room'), 
    path('api/join-room', join_room, name='join_room'),
    path('api/rooms', rooms, name='rooms'),
    path('api/room/<str:room_name>/participants/', get_room_participants, name='get_room_participants'),

    # Работа с викторинами
    path('api/room/<str:room_name>/questions/', get_room_questions, name='get_room_questions'),
    path('api/room/<str:room_name>/submit-answer/', SubmitAnswerView.as_view(), name='submit-answer'),    
]
