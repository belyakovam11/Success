import React, { useState } from 'react';
import './Register.css'; // Используем те же стили

const Login = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Login data:', formData);
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
    </div>
  );
};

export default Login;
