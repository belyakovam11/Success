from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Можно добавить дополнительные поля при необходимости
    pass

