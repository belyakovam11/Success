// RoomPage.js
import React from 'react';

const RoomPage = () => {
  return (
    <div>
      <h1>Комната для викторины</h1>
      <div className="room-layout">
        {/* Здесь будет логика для отображения игроков */}
        <div className="host">Ведущий</div>
        {/* Динамически добавьте игроков в полукруг */}
      </div>
    </div>
  );
};

export default RoomPage;
