import django
import pytest
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from rest_framework.test import APIClient
from Success.backend.user.models import CustomUser
from django.core.management import call_command
from unittest.mock import patch
from Success.backend.user.models import CustomUser,Question  
from trivia.views import get_questions_by_theme  # Импортируем вашу функцию


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
    url = reverse('register')  
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
    url = reverse('login') 
    data = {
        "username": "login_user",
        "password": "password123"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 200
    assert response.json().get("message") == "Login successful!"

@pytest.mark.django_db
def test_failed_login(api_client):
    url = reverse('login') 
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
    url_login = reverse('login') 
    data = {
        "username": "session_user",
        "password": "session_password"
    }

    response = api_client.post(url_login, data, format='json')
    assert response.status_code == 200

    # Проверка через client.session
    session_data = api_client.session
    assert session_data is not None  # Проверяем, что сессия содержит идентификатор пользователя


@pytest.mark.django_db
def test_get_questions_by_theme(create_user):
    # Создаем несколько вопросов с разными темами
    question_1 = Question.objects.create(
        text='Кто выиграл чемпионат мира 2018 года?',
        options='Бразилия,Франция,Германия,Аргентина',
        correct_answer='Франция',
        answer_time=10,
        theme='Спорт'
    )
    question_2 = Question.objects.create(
        text='Какой год был основан Твиттер?',
        options='2004,2005,2006,2007',
        correct_answer='2006',
        answer_time=10,
        theme='Технологии'
    )
    question_3 = Question.objects.create(
        text='Какая страна выиграла чемпионат мира по футболу в 2014 году?',
        options='Германия,Аргентина,Бразилия,Нидерланды',
        correct_answer='Германия',
        answer_time=10,
        theme='Спорт'
    )

    # Вызов функции для темы 'Спорт'
    sport_questions = get_questions_by_theme('Спорт')

    # Проверяем, что в списке вопросов только вопросы с темой 'Спорт'
    assert sport_questions.count() == 2
    assert all(question.theme == 'Спорт' for question in sport_questions)
    assert question_1 in sport_questions
    assert question_3 in sport_questions
    assert question_2 not in sport_questions
