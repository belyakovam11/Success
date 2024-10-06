import React from "react";

function Login() {
  return (
    <div className="login-form">
      <h2>Login</h2>
      <form>
        <label>Email/Username:</label>
        <input type="text" placeholder="Enter your email or username" />
        <label>Password:</label>
        <input type="password" placeholder="Enter your password" />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
