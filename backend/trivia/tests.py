import django
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from trivia.models import Question
from room.models import Room
from django.core.management import call_command
import random

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

@pytest.fixture
def create_room_with_questions(db):
    """Фикстура для создания комнаты с вопросами."""
    def make_room(name, player_count, theme, answer_time):
        room = Room.objects.create(
            name=name,
            player_count=player_count,
            theme=theme,
            answer_time=answer_time
        )
        
        questions = [
            Question.objects.create(
                text=f'Вопрос по теме {theme} №{i+1}',
                options='Ответ1,Ответ2,Ответ3,Ответ4',
                correct_answer=f'Ответ{i+1}',
                answer_time=answer_time,
                theme=theme
            ) for i in range(player_count)
        ]
        
        return room, questions
    return make_room

@pytest.fixture(autouse=True)
def fix_random_seed():
    random.seed(42)  # Зафиксировать случайный сид перед тестом

@pytest.mark.django_db
def test_get_room_questions(api_client, create_room_with_questions):
    # Создаем комнату с вопросами
    room, questions = create_room_with_questions(name="Test Room 1", player_count=5, theme="Спорт", answer_time=10)

    # Отправляем запрос на получение вопросов для комнаты
    url = reverse('get_room_questions', args=[room.name])
    response = api_client.get(url)
    
    # Проверяем, что запрос выполнен успешно
    assert response.status_code == 200
    
    # Проверяем, что количество вопросов в ответе соответствует player_count
    assert len(response.json()) == room.player_count

@pytest.mark.django_db
def test_get_room_questions_limited(api_client, create_room_with_questions):
    # Создаем комнату с вопросами, где player_count ограничивает количество вопросов
    room, questions = create_room_with_questions(name="Test Room 2", player_count=3, theme="Спорт", answer_time=10)

    # Отправляем запрос на получение вопросов для комнаты
    url = reverse('get_room_questions', args=[room.name])
    response = api_client.get(url)
    
    # Проверяем, что запрос выполнен успешно
    assert response.status_code == 200
    
    # Проверяем, что количество вопросов в ответе соответствует player_count
    assert len(response.json()) == room.player_count

@pytest.mark.django_db
def test_get_room_questions_random_order(api_client, create_room_with_questions):
    # Создаем комнату с вопросами, где player_count = 4
    room, questions = create_room_with_questions(name="Test Room 3", player_count=4, theme="История", answer_time=10)

    # Отправляем запрос на получение вопросов для комнаты
    url = reverse('get_room_questions', args=[room.name])
    response = api_client.get(url)
    
    # Проверяем, что запрос выполнен успешно
    assert response.status_code == 200
    
    # Проверяем, что количество вопросов в ответе соответствует player_count
    assert len(response.json()) == room.player_count
    
    # Проверяем, что вопросы не находятся в исходном порядке (поскольку они должны быть случайными)
    questions_text = [question['text'] for question in response.json()]
    assert questions_text != [f'Вопрос по теме История №{i+1}' for i in range(room.player_count)]

@pytest.mark.django_db
def test_get_room_questions_empty(api_client, create_room_with_questions):
    # Создаем комнату с вопросами, но player_count = 0, чтобы не было вопросов
    room, _ = create_room_with_questions(name="Test Room 4", player_count=0, theme="История", answer_time=0)

    # Отправляем запрос на получение вопросов для комнаты
    url = reverse('get_room_questions', args=[room.name])
    response = api_client.get(url)
    
    # Проверяем, что запрос выполнен успешно
    assert response.status_code == 200
    
    # Проверяем, что в ответе нет вопросов
    assert len(response.json()) == 0

@pytest.mark.django_db
def test_get_room_questions_not_found(api_client):
    # Отправляем запрос на получение вопросов для несуществующей комнаты
    url = reverse('get_room_questions', args=["NonExistentRoom"])
    response = api_client.get(url)
    
    # Проверяем, что статус ответа равен 404 (комната не найдена)
    assert response.status_code == 404
    
    # Проверяем, что возвращается ошибка
    assert response.json() == {"error": "Room not found"}
