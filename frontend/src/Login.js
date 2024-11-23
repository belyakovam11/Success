// Login.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Register.css';

const Login = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });
  const [message, setMessage] = useState('');
  const navigate = useNavigate(); // используем хук для навигации

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
      const response = await fetch('/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const data = await response.json();
        console.log(data.message)
        setMessage(data.message || 'Успешный вход!');
        navigate('/main'); // переход на главную страницу после успешного входа
      } else {
        const errorData = await response.json();
        setMessage(errorData.error || 'Ошибка входа');
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
      {message && <div className="message">{message}</div>}
    </div>
  );
};

export default Login;