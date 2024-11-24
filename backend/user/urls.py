from django.urls import path
from user.views import login_view, get_username
from user.views import register_view


urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('get-username/', get_username, name='get_username'),
   
]
