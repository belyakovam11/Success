from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.get_time, name='get_time'),
]
