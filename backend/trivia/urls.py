from django.urls import path
from trivia.views import get_room_questions


urlpatterns = [
    path('api/room/<str:room_name>/questions/', get_room_questions, name='get_room_questions'),    
]
