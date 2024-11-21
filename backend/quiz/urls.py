from django.urls import path
from app_quiz.views.auth_views import login_view, get_username
from app_quiz.views.db_views import get_db_status, get_data
from app_quiz.views.user_views import register_view
from app_quiz.views.room_views import create_room, join_room
from app_quiz.views.get_room_views import rooms, get_room_participants
from app_quiz.views.get_quiz import get_room_questions

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('get-username/', get_username, name='get_username'),
    path('db-status/', get_db_status, name='db_status'),
    path('data/', get_data, name='get_data'),
    path('api/create-room', create_room, name='create_room'),  # Для создания комнаты
    path('api/join-room', join_room, name='join_room'),  # Для присоединения к комнате
    path('api/rooms', rooms, name='rooms'),  # Для получения списка комнат
    path('api/room/<str:room_name>/participants/', get_room_participants, name='get_room_participants'),
     path('api/room/<str:room_name>/questions/', get_room_questions, name='get_room_questions'),
    
]
