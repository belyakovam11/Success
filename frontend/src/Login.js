// Login.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Register.css';

const Login = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });
<<<<<<< HEAD
  const [message, setMessage] = useState('');
  const navigate = useNavigate(); // используем хук для навигации
=======
  const [message, setMessage] = useState(''); // Для отображения сообщений
>>>>>>> 5dc94ec76a5ef8ce6fd345ac021f36f1d6f258b2

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
<<<<<<< HEAD
      const response = await fetch('http://127.0.0.1:5000/login/', {
=======
      const response = await fetch('http://127.0.0.1:5000/login/', { // Измените на ваш URL для входа
>>>>>>> 5dc94ec76a5ef8ce6fd345ac021f36f1d6f258b2
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const data = await response.json();
<<<<<<< HEAD
        setMessage(data.message || 'Успешный вход!');
        navigate('/main'); // переход на главную страницу после успешного входа
      } else {
        const errorData = await response.json();
        setMessage(errorData.error || 'Ошибка входа');
=======
        setMessage(data.message || 'Успешный вход!'); // Успешное сообщение
        // Здесь вы можете добавить код для перенаправления пользователя или обработки входа
      } else {
        const errorData = await response.json();
        setMessage(errorData.error || 'Ошибка входа'); // Сообщение об ошибке
>>>>>>> 5dc94ec76a5ef8ce6fd345ac021f36f1d6f258b2
      }
    } catch (error) {
      setMessage('Ошибка при попытке входа: ' + error.message);
    }
  };

  return (
    <div className="auth-form">
      <form onSubmit={handleSubmit}>
        <div className="login__field">
          <label htmlFor="username">Username</label>
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
          <label htmlFor="password">Password</label>
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
        </button>
      </form>
<<<<<<< HEAD
      {message && <div className="message">{message}</div>}
=======
      {message && <div className="message">{message}</div>} {/* Отображаем сообщение */}
>>>>>>> 5dc94ec76a5ef8ce6fd345ac021f36f1d6f258b2
    </div>
  );
};

export default Login;
