import React, { useState } from "react";
import "./App.css";
import Auth from "./Auth"; // Импортируйте ваш компонент auth.js

function App() {
  const [isLogin, setIsLogin] = useState(true);

  return (
    <div className="App">
      <div className="auth-container">
        <Auth isLogin={isLogin} />
      </div>
    </div>
  );
}

export default App;
