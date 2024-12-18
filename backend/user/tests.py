import django
import pytest
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from rest_framework.test import APIClient
from unittest.mock import patch
from user.models import CustomUser
from user.tasks import send_registration_email


# Django setup for pytest
django.setup()

@pytest.fixture
def api_client():
    return APIClient()
import pytest
from django.core.management import call_command


@pytest.fixture(scope='session')
def setup_db():
    """Настройка базы данных перед запуском тестов."""
    # Применяем миграции перед тестами
    call_command('migrate')  
    
    yield  # Этот момент будет использоваться для тестов
    
    # Очищаем базу данных после тестов
    call_command('flush', '--no-input')  # Очищаем все данные в базе данных


# Фикстура для отключения проверки CSRF во время тестов.
@pytest.fixture(autouse=True)
def disable_csrf_checks(settings):
    settings.CSRF_COOKIE_NAME = None
    settings.CSRF_HEADER_NAME = None
    settings.CSRF_COOKIE_HTTPONLY = False


#Фикстура для создания пользователя в базе данных.
@pytest.fixture
def create_user(db):
    def make_user(username="testuser", email="test@example.com", password="password123"):
        # Создаем пользователя через модель CustomUser
        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        return user
    return make_user


# Фикстура для настройки сессии клиента API.
@pytest.fixture
def set_up_session(api_client):
    middleware = SessionMiddleware(lambda request: None)
    api_client.handler = middleware.process_request(api_client)
    return api_client



#Фикстура для имитации задачи отправки email при регистрации.
@pytest.fixture
def mock_send_registration_email():
    with patch('user.tasks.send_registration_email.delay') as mock:
        yield mock



# Тесты для представлений (views)

@pytest.mark.django_db
def test_successful_registration(api_client, mock_send_registration_email):
    """
    Тест на успешную регистрацию пользователя.
    Проверяем корректность HTTP статуса, сообщения и вызова отправки email.
    """
    url = reverse('register') # Получаем URL для регистрации
    data = {
        "username": "new_user",
        "email": "new_user@example.com",
        "password": "password123"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.json().get("message") == "Успешно зарегистрированы!"
    # Проверяем, был ли вызван метод отправки email
    mock_send_registration_email.assert_called_once_with('new_user@example.com')



# Тест на ошибку при отсутствии обязательных полей в запросе регистрации.
@pytest.mark.django_db
def test_failed_registration_missing_fields(api_client):
    url = reverse('register')  
    data = {
        "username": "user_without_password",
        "email": "user@example.com"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.json().get("error") == "Все поля обязательны"



# Тест на успешный вход в систему.
@pytest.mark.django_db
def test_successful_login(api_client, create_user):
    # Создаем тестового пользователя
    create_user(username="login_user", password="password123")
    url = reverse('login') 
    data = {
        "username": "login_user",
        "password": "password123"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 200
    assert response.json().get("message") == "Login successful!"



# Тест на ошибку при вводе неправильных учетных данных.
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



#Тест на сохранение сессии после успешного входа в систему.
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
    assert session_data.get('username') == "session_user"



#Тест на получение имени пользователя после входа в систему.
@pytest.mark.django_db
def test_get_username_logged_in(api_client, create_user):
    create_user(username="session_user", password="session_password")
    url_login = reverse('login') 
    data = {
        "username": "session_user",
        "password": "session_password"
    }
    api_client.post(url_login, data, format='json')

    # Получаем имя пользователя через API
    url_get_username = reverse('get_username')
    response = api_client.get(url_get_username)
    assert response.status_code == 200
    assert response.json().get("username") == "session_user"



# Тест на ошибку при попытке получить имя пользователя без входа в систему.
@pytest.mark.django_db
def test_get_username_not_logged_in(api_client):
    url_get_username = reverse('get_username')
    response = api_client.get(url_get_username)
    assert response.status_code == 400
    assert response.json().get("error") == "User is not logged in"
