// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Auth from './Auth';
import MainPage from './MainPage';
import RoomPage from './RoomPage';
import './Auth.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Auth />} />
        <Route path="/main" element={<MainPage />} />
        <Route path="/room" element={<RoomPage />} />
      </Routes>
    </Router>
  );
}

export default App;
