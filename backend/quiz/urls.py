from django.urls import path
from user.views import login_view, get_username
from user.views import register_view
from room.views import create_room, join_room
from room.views import rooms, get_room_participants
from trivia.views import get_room_questions
from trivia.services import SubmitAnswerView

urlpatterns = [
     # Авторизация и регистрация пользователей
     # Маршрут для входа пользователя в систему
    path('login/', login_view, name='login'),

    # Маршрут для регистрации нового пользователя
    path('register/', register_view, name='register'),

    # Маршрут для получения текущего имени пользователя
    path('get-username/', get_username, name='get_username'),

    # Работа с комнатами
    # Маршрут для создания новой комнаты
    path('api/create-room', create_room, name='create_room'),

    # Маршрут для присоединения пользователя к комнате  
    path('api/join-room', join_room, name='join_room'),

    # Маршрут для получения списка всех доступных комнат
    path('api/rooms', rooms, name='rooms'),

    # Маршрут для получения списка участников в конкретной комнате
    path('api/room/<str:room_name>/participants/', get_room_participants, name='get_room_participants'),

    # Работа с викторинами
    # Маршрут для получения вопросов викторины для указанной комнаты
    path('api/room/<str:room_name>/questions/', get_room_questions, name='get_room_questions'),

    # Маршрут для отправки ответа на вопрос викторины
    path('api/room/<str:room_name>/submit-answer/', SubmitAnswerView.as_view(), name='submit-answer'),    
]
