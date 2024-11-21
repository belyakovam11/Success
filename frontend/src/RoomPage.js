import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './RoomPage.css';

const RoomPage = () => {
  const { name } = useParams(); // Получаем параметр "name" из URL
  const [users, setUsers] = useState([]);
  const [question, setQuestion] = useState({
    text: 'Какой год был основан React?',
    options: ['2010', '2013', '2015', '2018'],
    timer: 10, // Время на ответ (в секундах)
  });
  const [remainingTime, setRemainingTime] = useState(question.timer);

  useEffect(() => {
    if (!name) return;

    // Загружаем участников комнаты
    fetch(`/api/room/${name}/participants/`)
      .then((response) => response.json())
      .then((data) => setUsers(data))
      .catch((error) => console.error('Ошибка загрузки участников:', error));
  }, [name]);

  useEffect(() => {
    if (remainingTime > 0) {
      const timer = setTimeout(() => setRemainingTime(remainingTime - 1), 1000);
      return () => clearTimeout(timer);
    }
  }, [remainingTime]);

  const handleNextQuestion = () => {
    setQuestion({
      text: 'Кто разработал JavaScript?',
      options: ['Microsoft', 'Netscape', 'Apple', 'Google'],
      timer: 15,
    });
    setRemainingTime(15);
  };

  return (
    <div className="room-page">
      <h1>Комната для викторины: {name}</h1>

      <div className="user-info">
        <h2>Участники:</h2>
        <ul>
          {users.map((user, index) => (
            <li key={index}>{user.user}</li>
          ))}
        </ul>
      </div>

      <div className="quiz-section">
        <h2>Вопрос:</h2>
        <p>{question.text}</p>
        <div className="timer">Осталось времени: {remainingTime} секунд</div>
        <div className="options">
          {question.options.map((option, index) => (
            <button key={index} className="option-button">
              {option}
            </button>
          ))}
        </div>
      </div>

      {remainingTime === 0 && (
        <button className="next-question-button" onClick={handleNextQuestion}>
          Следующий вопрос
        </button>
      )}
    </div>
  );
};

export default RoomPage;
