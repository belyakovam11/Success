// Auth.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
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

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isLogin) {
      navigate('/main');
    } else {
      setMessage('Вы успешно зарегистрированы');
      setShowMessage(true);
      setTimeout(() => {
        setShowMessage(false);
      }, 3000);
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-container">
        <div className="toggle-buttons">
          <button className={`toggle-button ${isLogin ? 'active' : ''}`} onClick={handleToggle}>Вход</button>
          <button className={`toggle-button ${!isLogin ? 'active' : ''}`} onClick={handleToggle}>Регистрация</button>
        </div>
        <form className="auth-form" onSubmit={handleSubmit}>
          {isLogin ? (
            <>
              <div className="auth-field">
                <label htmlFor="username">Username</label>
                <input type="text" id="username" placeholder="Username" required />
              </div>
              <div className="auth-field">
                <label htmlFor="password">Password</label>
                <input type="password" id="password" placeholder="Password" required />
              </div>
            </>
          ) : (
            <>
              <div className="auth-field">
                <label htmlFor="register-username">Username</label>
                <input type="text" id="register-username" placeholder="Username" required />
              </div>
              <div className="auth-field">
                <label htmlFor="email">Email</label>
                <input type="email" id="email" placeholder="Email" required />
              </div>
              <div className="auth-field">
                <label htmlFor="register-password">Password</label>
                <input type="password" id="register-password" placeholder="Password" required />
              </div>
            </>
          )}
          <button className="submit-button" type="submit">{isLogin ? 'Войти' : 'Зарегистрироваться'}</button>
        </form>
        {showMessage && <div className="message">{message}</div>}
      </div>
    </div>
  );
};

export default Auth;
