// Auth.js
import React, { useState } from 'react';
import Register from './Register'; // Импортируем компонент регистрации
import Login from './Login'; // Импортируем компонент входа
import './Auth.css';

const Auth = () => {
  const [isLogin, setIsLogin] = useState(true); // Стейт для переключения между формами

  // Функция для переключения между режимами Вход/Регистрация
  const handleToggle = () => {
    setIsLogin(!isLogin);
  };

  return (
    <div className="auth-page">
      <div className="auth-container">
        {/* Переключатели между Входом и Регистрацией */}
        <div className="toggle-buttons">
          <button className={`toggle-button ${isLogin ? 'active' : ''}`} onClick={handleToggle}>
            Вход
          </button>
          <button className={`toggle-button ${!isLogin ? 'active' : ''}`} onClick={handleToggle}>
            Регистрация
          </button>
        </div>

        {/* Если isLogin === true, показываем компонент Login, иначе — Register */}
        {isLogin ? (
          <Login /> // Подключаем компонент Login для обработки входа
        ) : (
          <Register /> // Подключаем компонент Register для регистрации
        )}
      </div>
    </div>
  );
};

export default Auth;
