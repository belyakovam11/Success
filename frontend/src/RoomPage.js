import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './RoomPage.css';

const RoomPage = () => {
  const { name } = useParams();
  const [users, setUsers] = useState([]);
  const [questions, setQuestions] = useState([]);
  const [quizStarted, setQuizStarted] = useState(false);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [remainingTime, setRemainingTime] = useState(null);
  const [hasFetched, setHasFetched] = useState(false);
  const [quizEnded, setQuizEnded] = useState(false);
  const [selectedAnswer, setSelectedAnswer] = useState(null); // Track selected answer
  const [answerCorrect, setAnswerCorrect] = useState(null); // Store correctness of the answer
  const [score, setScore] = useState(0); // Track score
  const [startTime, setStartTime] = useState(null); // Track start time
  const [endTime, setEndTime] = useState(null); // Track end time
  const [showModal, setShowModal] = useState(false); // To show modal with results

  useEffect(() => {
    if (!name) return;

    const fetchParticipants = () => {
      fetch(`/api/room/${name}/participants/`)
        .then((response) => response.json())
        .then((data) => {
          setUsers(data);
          setHasFetched(true);
        })
        .catch((error) => console.error('Ошибка загрузки участников:', error));
    };

    fetchParticipants();
    const interval = setInterval(fetchParticipants, 500);

    return () => clearInterval(interval);
  }, [name]);

  useEffect(() => {
    if (name) {
      fetch(`/api/room/${name}/questions/`)
        .then((response) => response.json())
        .then((data) => {
          setQuestions(data);
        })
        .catch((error) => console.error('Ошибка загрузки вопросов:', error));
    }
  }, [name]);

  useEffect(() => {
    if (quizStarted && remainingTime > 0 && !quizEnded) {
      const timer = setTimeout(() => setRemainingTime(remainingTime - 1), 1000);
      return () => clearTimeout(timer);
    }
  }, [quizStarted, remainingTime, quizEnded]);

  const startQuiz = () => {
    setQuizStarted(true);
    setRemainingTime(10); // Set initial time for first question
    setStartTime(new Date()); // Record the start time of the quiz
  };

  const submitAnswer = (answer) => {
    setSelectedAnswer(answer);
    const correct = answer === questions[currentQuestionIndex].correct_answer;
    setAnswerCorrect(correct);

    if (correct) {
      setScore(prevScore => prevScore + 1); // Increase score for correct answers
    }

    // Reduced the delay to 500 milliseconds (0.5 seconds)
    setTimeout(() => {
      handleNextQuestion();
    }, 500); // Faster transition between questions
  };

  const handleNextQuestion = () => {
    if (currentQuestionIndex + 1 < questions.length) {
      setCurrentQuestionIndex(prevIndex => prevIndex + 1);
      setRemainingTime(questions[currentQuestionIndex + 1].answer_time);
      setSelectedAnswer(null);
      setAnswerCorrect(null);
    } else {
      // Stop the timer when the quiz ends
      setQuizEnded(true);
      setEndTime(new Date()); // Record end time when quiz finishes
      setQuizStarted(false);
      setShowModal(true); // Show results modal when quiz ends
    }
  };

  const closeModal = () => setShowModal(false);

  // Calculate time spent in seconds
  const getElapsedTime = () => {
    if (startTime && endTime) {
      const timeSpent = Math.floor((endTime - startTime) / 1000); // in seconds
      return timeSpent;
    }
    return 0;
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
          <div className="options">
            {questions[currentQuestionIndex]?.options.map((option, index) => (
              <button
                key={index}
                className={`option-button ${selectedAnswer === option
                  ? answerCorrect
                    ? 'correct'
                    : 'incorrect'
                  : ''
                  }`}
                onClick={() => submitAnswer(option)}
              >
                {option}
              </button>
            ))}
          </div>
        </div>
      )}

      {!quizStarted && hasFetched && !quizEnded && (
        <button className="start-button" onClick={startQuiz}>
          СТАРТ
        </button>
      )}

      {quizEnded && (
        <button className="exit-button" onClick={() => window.location.href = '/main'}>
          ВЫЙТИ
        </button>
      )}

      {showModal && (
        <div className="modal-overlay">
          <div className="modal">
            <h2>Результаты</h2>
            <p>Ваши баллы: {score}</p>
            <p>Количество правильных ответов: {score}</p>
            <p>Время выполнения: {getElapsedTime()} секунд</p>
            <h3>Список вопросов и правильных ответов:</h3>
            <ul>
              {questions.map((question, index) => (
                <li key={index}>
                  {question.text} — Правильный ответ: {question.correct_answer}
                </li>
              ))}
            </ul>
            <button className="exit-button" onClick={() => window.location.href = '/main'}>Закрыть</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default RoomPage;