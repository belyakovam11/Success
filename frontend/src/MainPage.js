import React, { useState } from 'react';
import './MainPage.css'; // Подключите файл стилей

const MainPage = () => {
  const [showCreateRoom, setShowCreateRoom] = useState(false);
  const [roomDetails, setRoomDetails] = useState({
    name: '',
    playerCount: '',
    theme: '',
    answerTime: '',
  });

  const availableRooms = ['Комната 1', 'Комната 2']; // Пример доступных комнат

  const handleRoomClick = (room) => {
    // Переход в выбранную комнату
    window.location.href = '/room'; // Здесь нужно указать правильный путь
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
    // Здесь добавьте логику для создания комнаты
    setShowCreateRoom(false);
  };

  return (
    <div className="main-page">
      <div className="player-card">
      <img src={`${process.env.PUBLIC_URL}/img/quizz_profile.jpg`} alt="Профиль" className="profile-pic" />
        <h2>Luntizz</h2>
        <p>Рейтинг: 1500</p>
        <p>Любимая категория: Насекомые</p>
      </div>
      <h2>Доступные комнаты:</h2>
      <div className="room-container">
        {availableRooms.map((room, index) => (
          <div className="room-card" key={index} onClick={() => handleRoomClick(room)}>
            {room}
          </div>
        ))}
      </div>
      <button className="create-room-button" onClick={handleCreateRoom}>Создать комнату</button>

      {showCreateRoom && (
        <div className="modal">
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
              <button type="button" onClick={() => setShowCreateRoom(false)}>Отмена</button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default MainPage;
