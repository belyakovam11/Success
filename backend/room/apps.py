# Импортируем базовый класс конфигурации приложения из Django
from django.apps import AppConfig

# Определяем конфигурацию для приложения "room"
class AppQuizConfig(AppConfig):     
    # Указываем тип поля по умолчанию для моделей в этом приложении
    default_auto_field = 'django.db.models.BigAutoField'
    # Указываем имя приложения, которое используется в настройках Django
    name = 'room'
