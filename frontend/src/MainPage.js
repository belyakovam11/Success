import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom'; // Импортируем useNavigate для редиректа
import './MainPage.css';

const MainPage = () => {
  const [username, setUsername] = useState('');
  const [availableRooms, setAvailableRooms] = useState([]);
  const [showCreateRoom, setShowCreateRoom] = useState(false);
  const [toastMessage, setToastMessage] = useState('');
  const [roomDetails, setRoomDetails] = useState({
    name: '',
    playerCount: '',
    theme: '',
    answerTime: '10',
  });
  const [selectedRoom, setSelectedRoom] = useState(null);
  const navigate = useNavigate(); // Для навигации

  const themes = ['Спорт', 'История'];

  // Получение имени пользователя
  const fetchUsername = async () => {
    try {
      const response = await fetch('/get-username/');
      const data = await response.json();
      setUsername(data.username);
    } catch (error) {
      console.error('Ошибка при получении имени пользователя:', error);
    }
  };

  // Получение доступных комнат
  const fetchAvailableRooms = async () => {
    try {
      const response = await fetch('/api/rooms');
      if (response.ok) {
        const data = await response.json();
        setAvailableRooms(data);
      } else {
        const errorData = await response.json();
        setToastMessage(errorData.error || 'Ошибка при получении доступных комнат');
      }
    } catch (error) {
      console.error('Ошибка при получении доступных комнат:', error);
      setToastMessage('Ошибка при получении доступных комнат');
    }
  };

  // Функция для добавления новой комнаты в список
  const addNewRoom = (newRoom) => {
    setAvailableRooms((prevRooms) => [newRoom, ...prevRooms]);
    setToastMessage('Комната успешно создана!');
    setTimeout(() => setToastMessage(''), 3000);
  };

  // Функция для выбора комнаты
  const selectRoom = async (room) => {
    try {
      const response = await fetch('/api/join-room', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ roomName: room.name, username: username }),
      });

      const data = await response.json();

      if (data.roomId && data.userId) {
        setSelectedRoom(room);
        setToastMessage(`Вы подключились к комнате: ${room.name}`);
        // После успешного подключения перенаправляем на комнату
        navigate(`/room/${room.name}`); // Используем navigate для перехода в комнату
      } else {
        setToastMessage('Не удалось подключиться к комнате');
      }
    } catch (error) {
      console.error('Ошибка при подключении к комнате:', error);
      setToastMessage('Ошибка при подключении к комнате');
    }
  };

  // Функция для создания случайной комнаты (Быстрая игра)
  const startQuickGame = async () => {
    const randomTheme = themes[Math.floor(Math.random() * themes.length)];
    const randomPlayerCount = Math.floor(Math.random() * 20) + 1;
    const randomName = `Random ${randomTheme} ${Math.floor(Math.random() * 900) + 100}`;

    const randomRoomDetails = {
      name: randomName,
      playerCount: randomPlayerCount,
      theme: randomTheme,
      answerTime: '10',
    };

    try {
      const response = await fetch('/api/create-room', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(randomRoomDetails),
      });

      const data = await response.json();

      if (response.ok) {
        addNewRoom(data); // Добавляем новую комнату
      } else {
        setToastMessage(data.error || 'Ошибка при создании комнаты');
      }
    } catch (error) {
      console.error('Ошибка при создании комнаты:', error);
      setToastMessage('Ошибка при создании комнаты');
    }
  };

  // Функция для создания новой комнаты
  const handleCreateRoom = () => {
    setShowCreateRoom(true);
  };

  const handleSubmitRoom = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/create-room', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(roomDetails),
      });

      const data = await response.json();

      if (response.ok) {
        addNewRoom(data); // Добавляем новую комнату
        setToastMessage('Комната успешно создана!');
        setTimeout(() => setToastMessage(''), 1000);
      } else {
        setToastMessage(data.error || 'Ошибка при создании комнаты');
      }
    } catch (error) {
      console.error('Ошибка при создании комнаты:', error);
      setToastMessage('Ошибка при создании комнаты');
    }
    setShowCreateRoom(false); // Закрываем форму создания комнаты
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setRoomDetails({ ...roomDetails, [name]: value });
  };

  useEffect(() => {
    fetchUsername();
    fetchAvailableRooms();

    // Обновляем список комнат каждые 0.5 секунд
    const intervalId = setInterval(fetchAvailableRooms, 500);

    // Очистка интервала при размонтировании компонента
    return () => clearInterval(intervalId);
  }, [username]);

  return (
    <div className="main-page">
      <div className="player-card">
        <img
          src={`${process.env.PUBLIC_URL}/img/quizz_profile.jpg`}
          alt="Профиль"
          className="profile-pic"
        />
        <h2>{username || 'Загрузка...'}</h2>
        <p>Рейтинг: 1500</p>
        <p>Любимая категория: Насекомые</p>
      </div>

      <h2>Доступные комнаты:</h2>
      <div className="room-container">
        {availableRooms.length > 0 ? (
          availableRooms.map((room, index) => (
            <div
              className="room-card"
              key={index}
              onClick={() => selectRoom(room)} // При клике на комнату
            >
              {room.name} {/* Отображаем только название комнаты */}
            </div>
          ))
        ) : (
          <p>У вас нет доступных комнат.</p>
        )}
      </div>

      {toastMessage && (
        <div className="toast">
          {toastMessage}
        </div>
      )}

      <button className="quick-game-button" onClick={startQuickGame}>
        Быстрая игра
      </button>
      <button className="create-room-button" onClick={handleCreateRoom}>
        Создать комнату
      </button>

      {showCreateRoom && (
        <div className="modal-overlay active">
          <div className="modal-content">
            <h2>Создать комнату</h2>
            <form onSubmit={handleSubmitRoom}>
              <input
                type="text"
                name="name"
                placeholder="Название комнаты"
                value={roomDetails.name}
                onChange={handleInputChange}
                required
              />
              <input
                type="number"
                name="playerCount"
                placeholder="Количество вопросов"
                value={roomDetails.playerCount}
                onChange={handleInputChange}
                required
              />
              <select
                name="theme"
                value={roomDetails.theme}
                onChange={handleInputChange}
                required
              >
                <option value="" disabled>
                  Выберите тему
                </option>
                <option value="Спорт">Спорт</option>
                <option value="История">История</option>
              </select>

              <button type="submit">Создать комнату</button>
              <button type="button" onClick={() => setShowCreateRoom(false)}>
                Отмена
              </button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default MainPage;