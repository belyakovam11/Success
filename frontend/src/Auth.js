import React, { useState } from 'react';
import Register from './Register';
import Login from './Login';
import './Auth.css';

const Auth = () => {
  const [isRegister, setIsRegister] = useState(true);

  return (
    <div className="auth-page">
      <div className="auth-container">
        <div className="toggle-buttons">
          <button
            className={`toggle-button ${isRegister ? 'active' : ''}`}
            onClick={() => setIsRegister(true)}
          >
            Register
          </button>
          <button
            className={`toggle-button ${!isRegister ? 'active' : ''}`}
            onClick={() => setIsRegister(false)}
          >
            Login
          </button>
        </div>
        {isRegister ? <Register /> : <Login />}
      </div>
    </div>
  );
};

export default Auth;
