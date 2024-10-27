from django.contrib import admin
from django.urls import path
from app_quiz.views import get_time, get_db_status, UserList, register_view
from app_quiz.views import get_time, UserList, get_db_status, register_view, login_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', get_time, name='get_time'),
    path('api/db-status/', get_db_status, name='db_status'),
    path('api/users/', UserList.as_view(), name='user_list'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),  # Добавляем маршрут для регистрации
     ]
