import os
import django
from django.conf import settings

# Настройка Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz.settings")
django.setup()

from django.contrib.auth.models import User  # Импортируйте нужные модели

def create_superuser():
    User.objects.create_superuser('admin', 'admin@example.com', 'password')

if __name__ == "__main__":
    create_superuser()
    print("Суперпользователь создан.")
