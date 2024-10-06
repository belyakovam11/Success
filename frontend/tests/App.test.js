import React from 'react';
import { render, screen, act } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from '../src/App'; // Путь к вашему компоненту App

// Mock для функции fetch
global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true, // имитируем успешный ответ
    json: () => Promise.resolve({
      Name: 'John Doe', 
      Age: 30, 
      Date: '2024-01-01', 
      programming: 'JavaScript'
    }),
  })
);

test('renders data after fetch', async () => {
  await act(async () => {
    render(<App />);
  });

  // Проверяем, что данные отобразились
  expect(screen.getByText(/John Doe/i)).toBeInTheDocument();
  expect(screen.getByText(/30/i)).toBeInTheDocument();
  expect(screen.getByText(/2024-01-01/i)).toBeInTheDocument();
  expect(screen.getByText(/JavaScript/i)).toBeInTheDocument();
});
