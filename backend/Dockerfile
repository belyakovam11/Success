# Базовый образ Python 3.9
FROM python:3.9-slim

# Установка зависимостей для системы
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev musl-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Обновление pip до последней версии
RUN pip install --upgrade pip

# Установка Python-зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё содержимое проекта в рабочую директорию
COPY . .

# Удаляем не нужные пакеты, чтобы уменьшить размер образа
RUN apt-get purge -y gcc python3-dev musl-dev

# Открываем порт 5000 для Django
EXPOSE 5000

# Установка переменной среды для установки адреса хоста
ENV PYTHONUNBUFFERED=1

# Запуск Django сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
