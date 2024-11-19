from django.urls import path
from app_quiz.views.auth_views import login_view, get_username
from app_quiz.views.db_views import get_db_status, get_data
from app_quiz.views.user_views import register_view
from app_quiz.views.room_views import create_room, join_room

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('get-username/', get_username, name='get_username'),
    path('db-status/', get_db_status, name='db_status'),
    path('data/', get_data, name='get_data'),
    path('api/create-room', create_room, name='create_room'),  # Исправленный путь
    path('join-room/', join_room, name='join_room'),
]
