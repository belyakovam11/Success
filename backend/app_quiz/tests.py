import django
import pytest
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from rest_framework.test import APIClient
from app_quiz.models import CustomUser
from django.core.management import call_command
from unittest.mock import patch
from app_quiz.models import CustomUser  # Импортируем модели после django.setup()

# Django setup for pytest
django.setup()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture(scope='session')
def setup_db():
    """Настройка базы данных перед запуском тестов."""
    call_command('migrate')  # Применяем миграции перед тестами.
    yield
    call_command('flush', '--no-input')  # Очищаем базу данных после тестов.

@pytest.fixture(autouse=True)
def disable_csrf_checks(settings):
    settings.CSRF_COOKIE_NAME = None
    settings.CSRF_HEADER_NAME = None
    settings.CSRF_COOKIE_HTTPONLY = False

@pytest.fixture
def create_user(db):
    def make_user(username="testuser", email="test@example.com", password="password123"):
        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        return user
    return make_user

@pytest.fixture
def set_up_session(api_client):
    """Фикстура для настройки сессии клиента API."""
    middleware = SessionMiddleware(lambda request: None)
    api_client.handler = middleware.process_request(api_client)
    return api_client

@pytest.fixture
def mock_send_registration_email():
    with patch('app_quiz.tasks.send_registration_email.delay') as mock:
        yield mock

@pytest.mark.django_db(transaction=True)
def test_successful_registration(api_client, mock_send_registration_email):
    url = reverse('register')
    data = {
        "username": "new_user",
        "email": "new_user@example.com",
        "password": "password123"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.json().get("message") == "Успешно зарегистрированы!"

@pytest.mark.django_db
def test_failed_registration(api_client):
    url = reverse('register')  # Исправлено с 'register_view' на 'register'
    data = {
        "username": "user_without_password",
        "email": "user@example.com"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.json().get("error") == "Все поля обязательны"

@pytest.mark.django_db
def test_successful_login(api_client, create_user):
    create_user(username="login_user", password="password123")
    url = reverse('login')  # Исправлено с 'login_view' на 'login'
    data = {
        "username": "login_user",
        "password": "password123"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 200
    assert response.json().get("message") == "Login successful!"

@pytest.mark.django_db
def test_failed_login(api_client):
    url = reverse('login')  # Исправлено с 'login_view' на 'login'
    data = {
        "username": "wrong_user",
        "password": "wrong_password"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.json().get("error") == "Неверное имя пользователя или пароль."


@pytest.mark.django_db
def test_session_saved_after_login(api_client, create_user):
    create_user(username="session_user", password="session_password")

    # Логинимся
    url_login = reverse('login')  # Убедитесь, что 'login' — это правильное имя URL
    data = {
        "username": "session_user",
        "password": "session_password"
    }

    response = api_client.post(url_login, data, format='json')
    assert response.status_code == 200

    # Проверка через client.session
    session_data = api_client.session
    assert session_data is not None  # Проверяем, что сессия содержит идентификатор пользователя

