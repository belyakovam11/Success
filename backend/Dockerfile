# Базовый образ Python 3.9
FROM python:3.9-slim

# Установка зависимостей для системы, включая ping
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev musl-dev postgresql-client && \
    apt-get clean

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Обновление pip до последней версии
RUN pip install --upgrade pip

# Установка Python-зависимостей
RUN pip install --no-cache-dir -r requirements.txt  # Устанавливаются все зависимости

# Установка pytest-django
RUN pip install pytest-django

# Копируем всё содержимое проекта в рабочую директорию
COPY . .

# Открываем порт 5000 для Django
EXPOSE 5000

# Установка переменной среды для установки адреса хоста
ENV PYTHONUNBUFFERED=1

# Запуск миграций, сервера Django и Celery worker
CMD ["sh", "-c", "python manage.py migrate && DJANGO_SETTINGS_MODULE='quiz.settings' python init_sql.py && python manage.py runserver 0.0.0.0:5000 & celery -A quiz worker --loglevel=info"]