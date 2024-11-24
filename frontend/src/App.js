import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Auth from './Auth';
import MainPage from './MainPage';
import RoomPage from './RoomPage';
import UserProfile from './UserProfile'; // Импортируем компонент профиля
import './Auth.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Auth />} />
        <Route path="/main" element={<MainPage />} />
        <Route path="/room/:name" element={<RoomPage />} />
        <Route path="/profile" element={<UserProfile />} /> {/* Новый маршрут */}
      </Routes>
    </Router>
  );
}

export default App;
