import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Auth from './components/auth/Auth';
import MainPage from './components/main-page/MainPage';
import RoomPage from './components/room/RoomPage';
import UserProfile from './components/user/UserProfile'; // Импортируем компонент профиля
import './components/auth/Auth';

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
