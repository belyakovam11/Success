// RoomPage.js

import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './RoomPage.css';

const RoomPage = () => {
  const { name } = useParams(); // Получаем параметр "name" из URL
  const [users, setUsers] = useState([]);
  const [questions, setQuestions] = useState([]); // Храним вопросы
  const [quizStarted, setQuizStarted] = useState(false); // Флаг для отслеживания старта викторины
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0); // Индекс текущего вопроса
  const [remainingTime, setRemainingTime] = useState(null);
  const [hasFetched, setHasFetched] = useState(false);

  useEffect(() => {
    if (!name) return;

    const fetchParticipants = () => {
      fetch(`/api/room/${name}/participants/`)
        .then((response) => {
          if (response.status === 200) {
            return response.json();
          } else {
            throw new Error('Не удалось загрузить участников');
          }
        })
        .then((data) => {
          setUsers(data);
          setHasFetched(true); // Устанавливаем флаг, когда данные загружены
        })
        .catch((error) => console.error('Ошибка загрузки участников:', error));
    };

    // Загружаем участников при первом рендере
    fetchParticipants();

    // Устанавливаем периодическую проверку данных
    const interval = setInterval(fetchParticipants, 500); // Обновляем список участников каждые 5 секунд

    // Очистка интервала при размонтировании компонента
    return () => clearInterval(interval);
  }, [name]); // Запускаем только при изменении имени комнаты

  useEffect(() => {
    if (name) {
      // Загружаем вопросы при монтировании компонента
      fetch(`/api/room/${name}/questions/`)
        .then((response) => response.json())
        .then((data) => {
          console.log("Загруженные вопросы:", data); // Выводим все загруженные вопросы в консоль
          setQuestions(data);
        })
        .catch((error) => console.error('Ошибка загрузки вопросов:', error));
    }
  }, [name]);


  useEffect(() => {
    if (quizStarted && remainingTime > 0) {
      const timer = setTimeout(() => setRemainingTime(remainingTime - 1), 1000);
      return () => clearTimeout(timer);
    }
  }, [quizStarted, remainingTime]);

  const startQuiz = () => {
    setQuizStarted(true);
    setRemainingTime(10); // Устанавливаем время на ответ из первого вопроса
  };


  const submitAnswer = (answer) => {
    fetch(`/api/room/${name}/submit-answer/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'User-Agent': navigator.userAgent,
      },
      body: JSON.stringify({ answer }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Ответ отправлен:", data);
        if (data.is_correct) {
          alert(`Правильно! Количество правильных ответов: ${data.correct_answers_count}`);
        } else {
          alert(`Неправильно! Количество правильных ответов: ${data.correct_answers_count}`);
        }

        // Переход к следующему вопросу
        if (data.next_question) {
          handleNextQuestion();
        } else {
          alert("Викторина завершена!");
        }
      })
      .catch((error) => console.error('Ошибка отправки ответа:', error));
  };

  const handleNextQuestion = () => {
    if (currentQuestionIndex + 1 < questions.length) {
      setCurrentQuestionIndex((prevIndex) => prevIndex + 1);
      setRemainingTime(questions[currentQuestionIndex + 1].answer_time);
    } else {
      // Если вопросов больше нет, заканчиваем викторину
      alert("Викторина завершена!");
      setQuizStarted(false);
    }
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

      {!quizStarted ? (
        <div className="instructions">
          <p>Добро пожаловать в викторину! Нажмите кнопку "СТАРТ", чтобы начать.</p>
        </div>
      ) : (
        <div className="quiz-section">
          <h2>Вопрос:</h2>
          <p>{questions[currentQuestionIndex]?.text}</p>
          <div className="timer">Осталось времени: {remainingTime} секунд</div>
          <div className="options">
            {questions[currentQuestionIndex]?.options.map((option, index) => (
              <button
                key={index}
                className="option-button"
                onClick={() => submitAnswer(option)}
              >
                {option}
              </button>

            ))
            }
          </div>
        </div>
      )}

      {!quizStarted && hasFetched && (
        <button className="start-button" onClick={startQuiz}>
          СТАРТ
        </button>
      )}

      {remainingTime === 0 && quizStarted && (
        <button className="next-question-button" onClick={handleNextQuestion}>
          Следующий вопрос
        </button>
      )}
    </div>
  );
};

export default RoomPage;
