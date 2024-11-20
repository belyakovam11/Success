import React, { useState } from 'react';

const CreateRoomComponent = ({ onRoomCreated, setShowCreateRoom }) => {
  const [roomDetails, setRoomDetails] = useState({
    name: '',
    playerCount: '',
    theme: '',
    answerTime: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setRoomDetails({ ...roomDetails, [name]: value });
  };

  const handleSubmitRoom = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('/api/create-room', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(roomDetails),
      });
      const data = await response.json();

      if (data.room) {
        onRoomCreated(data.room);  // Передаем данные о новой комнате в MainPage
        setShowCreateRoom(false);  // Закрываем форму создания комнаты
      }
    } catch (error) {
      console.error('Ошибка при создании комнаты:', error);
    }
  };

  return (
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
          <button type="button" onClick={() => setShowCreateRoom(false)}>Отмена</button>
        </form>
      </div>
    </div>
  );
};

export default CreateRoomComponent;
