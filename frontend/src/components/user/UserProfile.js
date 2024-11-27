import React, { useState, useEffect } from 'react';

const UserProfile = () => {
    // Состояние для имени пользователя
    const [username, setUsername] = useState('');
    // Состояние для списка созданных комнат
    const [userRooms, setUserRooms] = useState([]);

    // Получение данных о пользователе и его созданных комнатах
    const fetchUserProfile = async () => {
        try {
            // Запрос для получения списка комнат, созданных пользователем
            const response = await fetch('/api/user-rooms');  // API для получения созданных комнат
            const data = await response.json();

            // Если данные о комнатах есть, сохраняем их в состояние
            if (data.rooms) {
                setUserRooms(data.rooms);  // Сохраняем список комнат в состояние
            }
        } catch (error) {
            console.error('Ошибка при получении данных пользователя:', error);
        }

        try {
            // Запрос для получения имени пользователя
            const userResponse = await fetch('/get-username/');
            const userData = await userResponse.json();
            setUsername(userData.username);  // Сохраняем имя пользователя в состояние
        } catch (error) {
            console.error('Ошибка при получении имени пользователя:', error);
        }
    };

    // Используем useEffect для вызова fetchUserProfile при монтировании компонента
    useEffect(() => {
        fetchUserProfile();
    }, []);  // Пустой массив зависимостей для вызова только один раз при монтировании компонента

    return (
        <div>
            <h2>Профиль пользователя: {username}</h2>
            <h3>Созданные комнаты:</h3>
            <ul>
                {userRooms.length > 0 ? (
                    userRooms.map((room, index) => (
                        <li key={index}>
                            <strong>{room.name}</strong> - Тема: {room.theme}, Количество игроков: {room.playerCount}
                        </li>
                    ))
                ) : (
                    <p>У вас нет созданных комнат.</p>  // Сообщение, если нет созданных комнат
                )}
            </ul>
        </div>
    );
};

export default UserProfile;
