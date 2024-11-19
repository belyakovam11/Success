from django.urls import path
from .views import login_view, register_view, get_username
from .views.db_views import get_db_status, get_data  # Импорты из db_views


urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('username/', get_username, name='get_username'),
    path('db-status/', get_db_status, name='db_status'),
    path('data/', get_data, name='get_data'),
]
