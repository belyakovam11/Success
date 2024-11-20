import React, { useState, useEffect } from 'react';
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
    answerTime: '',
  });
  const [selectedRoom, setSelectedRoom] = useState(null);

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
      const response = await fetch('/api/user-rooms');
      const data = await response.json();
      setAvailableRooms(data.rooms || []);
    } catch (error) {
      console.error('Ошибка при получении доступных комнат:', error);
    }
  };

  // Функция для добавления новой комнаты в список
  const addNewRoom = (newRoom) => {
    setAvailableRooms((prevRooms) => {
      const updatedRooms = [...prevRooms, newRoom];
      localStorage.setItem('rooms', JSON.stringify(updatedRooms)); // Сохраняем в localStorage
      return updatedRooms;
    });
    setToastMessage('Комната успешно создана!');
    setTimeout(() => setToastMessage(''), 3000);
  };

  // Функция для выбора комнаты
  const selectRoom = (room) => {
    setSelectedRoom(room);
    setToastMessage(`Вы подключились к комнате: ${room.name}`);
    localStorage.setItem('selectedRoom', JSON.stringify(room)); // Сохраняем выбранную комнату в localStorage
    setTimeout(() => setToastMessage(''), 3000);
  };

  useEffect(() => {
    fetchUsername();
    const savedRooms = JSON.parse(localStorage.getItem('rooms'));
    if (savedRooms) {
      setAvailableRooms(savedRooms);
    } else {
      fetchAvailableRooms(); // Загружаем с сервера, если в localStorage ничего нет
    }

    const savedSelectedRoom = JSON.parse(localStorage.getItem('selectedRoom'));
    if (savedSelectedRoom) {
      setSelectedRoom(savedSelectedRoom);
      setToastMessage(`Вы выбрали комнату: ${savedSelectedRoom.name}`);
    }
  }, []);

  const handleCreateRoom = () => {
    setShowCreateRoom(true);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setRoomDetails({ ...roomDetails, [name]: value });
  };

  const handleSubmitRoom = (e) => {
    e.preventDefault();
    addNewRoom(roomDetails);
    setShowCreateRoom(false);
  };

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
              {room.name}
            </div>
          ))
        ) : (
          <p>У вас нет доступных комнат.</p>
        )}
      </div>

      {/* Модальное окно с деталями выбранной комнаты */}
      {selectedRoom && (
        <div className="modal-overlay active">
          <div className="selected-room-card">
            <h3>Информация о комнате</h3>
            <p>
              <strong>Тема викторины:</strong> {selectedRoom.theme}
            </p>
            <p>
              <strong>Время ответа на вопрос:</strong> {selectedRoom.answerTime}
            </p>
            <p>
              <strong>Количество свободных мест:</strong> {selectedRoom.freeSpaces}
            </p>
            <button
              className="join-room-button"
              onClick={() => window.location.href = '/room'} // Переход в комнату
            >
              Подключиться к комнате
            </button>
            <button className="back-button" onClick={() => setSelectedRoom(null)}>
              Назад
            </button>
          </div>
        </div>
      )}

      {toastMessage && (
        <div className="toast">
          {toastMessage}
        </div>
      )}

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
                placeholder="Количество игроков"
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

              <input
                type="number"
                name="answerTime"
                placeholder="Время ответа (в секундах)"
                value={roomDetails.answerTime}
                onChange={handleInputChange}
                required
              />
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
