// Auth.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Register from './Register'; // Импортируем компонент регистрации
import './Auth.css';

const Auth = () => {
  const [isLogin, setIsLogin] = useState(true);
  const [message, setMessage] = useState('');
  const [showMessage, setShowMessage] = useState(false);
  const navigate = useNavigate();

  const handleToggle = () => {
    setIsLogin(!isLogin);
    setMessage('');
  };

  const handleLogin = (e) => {
    e.preventDefault();
    // Логика для входа (например, проверка учетных данных)
    navigate('/main');
  };

  return (
    <div className="auth-page">
      <div className="auth-container">
        <div className="toggle-buttons">
          <button className={`toggle-button ${isLogin ? 'active' : ''}`} onClick={handleToggle}>Вход</button>
          <button className={`toggle-button ${!isLogin ? 'active' : ''}`} onClick={handleToggle}>Регистрация</button>
        </div>
        {isLogin ? (
          <form className="auth-form" onSubmit={handleLogin}>
            <div className="auth-field">
              <label htmlFor="username">Username</label>
              <input type="text" id="username" placeholder="Username" required />
            </div>
            <div className="auth-field">
              <label htmlFor="password">Password</label>
              <input type="password" id="password" placeholder="Password" required />
            </div>
            <button className="submit-button" type="submit">Войти</button>
          </form>
        ) : (
          <Register />
        )}
        {showMessage && <div className="message">{message}</div>}
      </div>
    </div>
  );
};

export default Auth;
