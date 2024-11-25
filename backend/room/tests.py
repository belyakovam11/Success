import json
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from room.models import Room, RoomParticipant
from django.core.management import call_command

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
def create_room(db):
    def _create_room(name, player_count, theme, answer_time):
        room = Room.objects.create(
            name=name,
            player_count=player_count,
            theme=theme,
            answer_time=answer_time
        )
        return room
    return _create_room

@pytest.mark.django_db
def test_get_rooms(api_client, create_room):
    # Создаем комнаты для теста
    create_room('Test Room 1', 5, 'Science', 30)
    create_room('Test Room 2', 3, 'Math', 20)

    url = reverse('rooms')
    response = api_client.get(url)

    assert response.status_code == 200
    rooms = response.json()
    assert len(rooms) == 2
    assert rooms[0]['name'] == 'Test Room 1'
    assert rooms[1]['name'] == 'Test Room 2'

@pytest.mark.django_db
def test_get_room_participants(api_client, create_room):
    room = create_room('Test Room', 3, 'History', 15)
    RoomParticipant.objects.create(user='user1', room=room, user_agent='Mozilla')
    RoomParticipant.objects.create(user='user2', room=room, user_agent='Chrome')

    url = reverse('get_room_participants', args=[room.name])
    response = api_client.get(url)

    assert response.status_code == 200
    participants = response.json()
    assert len(participants) == 2
    assert participants[0]['user'] == 'user1'
    assert participants[1]['user'] == 'user2'

@pytest.mark.django_db
def test_join_room(api_client, create_room):
    room = create_room('Test Room', 3, 'Music', 20)
    data = {
        'roomName': room.name,
        'username': 'user1'
    }

    url = reverse('join_room')
    response = api_client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    response_data = response.json()
    assert response_data['message'] == f'Вы присоединились к комнате {room.name}'
    assert response_data['roomId'] == room.id
    assert response_data['userId'] == 'user1'

    # Проверка, что пользователь был добавлен
    participant = RoomParticipant.objects.get(user='user1', room=room)
    assert participant is not None
    assert participant.user_agent == 'Unknown'  # поскольку мы не передавали user-agent

@pytest.mark.django_db
def test_join_room_full(api_client, create_room):
    room = create_room('Test Room', 2, 'Math', 15)
    RoomParticipant.objects.create(user='user1', room=room, user_agent='Mozilla')
    RoomParticipant.objects.create(user='user2', room=room, user_agent='Chrome')

    data = {
        'roomName': room.name,
        'username': 'user3'
    }

    url = reverse('join_room')
    response = api_client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'error': 'Слишком много вопрсов заданно'}

@pytest.mark.django_db
def test_create_room(api_client):
    data = {
        'name': 'New Room',
        'playerCount': 4,
        'theme': 'Technology',
        'answerTime': 10
    }

    url = reverse('create_room')
    response = api_client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    response_data = response.json()
    assert response_data['message'] == 'Комната успешно создана'
    assert response_data['room']['name'] == 'New Room'
    assert response_data['room']['playerCount'] == 4
    assert response_data['room']['theme'] == 'Technology'
    assert response_data['room']['answerTime'] == 10

@pytest.mark.django_db
def test_create_room_already_exists(api_client, create_room):
    create_room('Existing Room', 5, 'Science', 30)

    data = {
        'name': 'Existing Room',
        'playerCount': 4,
        'theme': 'Technology',
        'answerTime': 20
    }

    url = reverse('create_room')
    response = api_client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'error': 'Комната с таким названием уже существует'}

@pytest.mark.django_db
def test_create_room_missing_fields(api_client):
    data = {
        'name': 'Incomplete Room',
        'playerCount': 4
    }

    url = reverse('create_room')
    response = api_client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert response.json() == {'error': 'Все поля обязательны'}
