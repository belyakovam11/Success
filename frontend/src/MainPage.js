import React, { useState } from 'react';
import './MainPage.css';

const MainPage = () => {
  const [showCreateRoom, setShowCreateRoom] = useState(false);
  const [roomDetails, setRoomDetails] = useState({
    name: '',
    playerCount: '',
    theme: '',
    answerTime: '',
  });
  const [selectedRoom, setSelectedRoom] = useState(null);
  const [showModal, setShowModal] = useState(false);

  const availableRooms = [
    {
      name: 'Комната 1',
      theme: 'История',
      answerTime: '30 сек',
      freeSpaces: 2,
    },
    {
      name: 'Комната 2',
      theme: 'Наука',
      answerTime: '20 сек',
      freeSpaces: 1,
    },
  ];

  const handleRoomClick = (room) => {
    setSelectedRoom(room);
    setShowModal(true);
  };

  const handleJoinRoom = () => {
    window.location.href = '/room'; // Переход в комнату
  };

  const handleCreateRoom = () => {
    setShowCreateRoom(true);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setRoomDetails({ ...roomDetails, [name]: value });
  };

  const handleSubmitRoom = (e) => {
    e.preventDefault();
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
        <h2>Luntizz</h2>
        <p>Рейтинг: 1500</p>
        <p>Любимая категория: Насекомые</p>
      </div>

      <h2>Доступные комнаты:</h2>
      <div className="room-container">
        {availableRooms.map((room, index) => (
          <div
            className="room-card"
            key={index}
            onClick={() => handleRoomClick(room)}
          >
            {room.name}
          </div>
        ))}
      </div>

      {/* Модальное окно с деталями комнаты */}
      {showModal && selectedRoom && (
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
            <button className="join-room-button" onClick={handleJoinRoom}>
              Подключиться к комнате
            </button>
            <button className="back-button" onClick={() => setShowModal(false)}>
              Назад
            </button>
          </div>
        </div>
      )}

      {/* Кнопка создания комнаты */}
      <button className="create-room-button" onClick={handleCreateRoom}>
        Создать комнату
      </button>

      {/* Модальное окно для создания комнаты */}
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
              <input
                type="text"
                name="theme"
                placeholder="Тема викторины"
                value={roomDetails.theme}
                onChange={handleInputChange}
                required
              />
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
