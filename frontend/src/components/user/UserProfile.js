import React, { useState, useEffect } from 'react';

const UserProfile = () => {
    const [username, setUsername] = useState('');
    const [userRooms, setUserRooms] = useState([]);

    const fetchUserProfile = async () => {
        try {
            const response = await fetch('/api/user-rooms');
            const data = await response.json();

            // Если данные о комнатах есть, сохраняем их в состояние
            if (data.rooms) {
                setUserRooms(data.rooms);  // Сохраняем список комнат в состояние
            }
        } catch (error) {
            console.error('Ошибка при получении данных пользователя:', error);
        }

        try {
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
    }, []); 

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
