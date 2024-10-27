import React, { useState } from 'react'; 
import './Register.css'; 
 
const Register = () => { 
  const [formData, setFormData] = useState({ 
    username: '', 
    email: '', 
    password: '', 
  }); 
  const [message, setMessage] = useState(''); 
 
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
      const response = await fetch('http://127.0.0.1:5000/register/', { 
        method: 'POST', 
        headers: { 
          'Content-Type': 'application/json', 
        }, 
        body: JSON.stringify(formData), 
      }); 
 
      if (response.ok) { 
        const data = await response.json(); 
        setMessage(data.message || 'Успешно зарегистрированы!'); 
        setFormData({ username: '', email: '', password: '' }); 
      } else { 
        const errorData = await response.json(); 
        setMessage(errorData.error || 'Ошибка регистрации'); 
      } 
    } catch (error) { 
      setMessage('Ошибка при попытке регистрации: ' + error.message); 
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
          <label htmlFor="email">Email</label> 
          <input 
            type="email" 
            className="login__input" 
            placeholder="Email" 
            name="email" 
            value={formData.email} 
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
          <span className="button__text">Register Now</span> 
        </button> 
      </form> 
      {message && <div className="message">{message}</div>} 
    </div> 
  ); 
}; 
 
export default Register;