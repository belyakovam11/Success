import React from "react";

function Register() {
  return (
    <div className="register-form">
      <h2>Register</h2>
      <form>
        <label>Email:</label>
        <input type="email" placeholder="Enter your email" />
        <label>Password:</label>
        <input type="password" placeholder="Enter your password" />
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default Register;
