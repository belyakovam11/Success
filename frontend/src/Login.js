import React, { useState } from 'react';
import './Register.css'; // Используем те же стили

const Login = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });
  const [message, setMessage] = useState(''); // Для отображения сообщений

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:5000/login/', { // Измените на ваш URL для входа
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const data = await response.json();
        setMessage(data.message || 'Успешный вход!'); // Успешное сообщение
        // Здесь вы можете добавить код для перенаправления пользователя или обработки входа
      } else {
        const errorData = await response.json();
        setMessage(errorData.error || 'Ошибка входа'); // Сообщение об ошибке
      }
    } catch (error) {
      setMessage('Ошибка при попытке входа: ' + error.message);
    }
  };

  return (
    <div className="auth-form">
      <form onSubmit={handleSubmit}>
        <div className="login__field">
          <i className="login__icon fas fa-user"></i>
          <input
            type="text"
            className="login__input"
            placeholder="Username"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
          />
        </div>
        <div className="login__field">
          <i className="login__icon fas fa-lock"></i>
          <input
            type="password"
            className="login__input"
            placeholder="Password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        <button className="button login__submit" type="submit">
          <span className="button__text">Login</span>
          <i className="button__icon fas fa-chevron-right"></i>
        </button>
      </form>
      {message && <div className="message">{message}</div>} {/* Отображаем сообщение */}
    </div>
  );
};

export default Login;
