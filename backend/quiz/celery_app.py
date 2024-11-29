from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем переменную окружения для Django, чтобы указать, какой файл настроек использовать
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')

# Создаем объект Celery с именем 'quiz'
app = Celery('quiz')

# Загружаем конфигурацию Celery из настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY') 

# Автоматически обнаруживаем задачи (tasks) из приложений
app.autodiscover_tasks()


