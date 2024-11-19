import React, { useState } from 'react';

const CreateRoomComponent = () => {
    const [showCreateRoom, setShowCreateRoom] = useState(false);
    const [roomDetails, setRoomDetails] = useState({
        name: '',
        playerCount: '',
        theme: '',
        answerTime: '',
    });

    // Обработчик изменений в полях формы
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        console.log(`Изменение данных: ${name} = ${value}`);  // Логирование изменений
        setRoomDetails({ ...roomDetails, [name]: value });
    };

    // Обработчик отправки формы
    const handleSubmitRoom = (e) => {
        e.preventDefault();  // предотвращает стандартное поведение формы
        console.log("Данные комнаты при отправке:", roomDetails);  // Логирование данных перед отправкой

        // Закрытие формы
        setShowCreateRoom(false);

        // Отправка данных на сервер
        fetch('http://localhost:8000/api/create-room', {  // полный путь к серверу
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(roomDetails),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log('Комната создана:', data);
                // Логика после успешного создания комнаты
            })
            .catch((error) => {
                console.error('Ошибка при создании комнаты:', error);
            });
    };

    // Обработчик для открытия формы создания комнаты
    const handleCreateRoom = () => {
        console.log("Открытие формы создания комнаты...");
        setShowCreateRoom(true);  // Показываем форму для создания комнаты
    };

    return (
        <div>
            <button onClick={handleCreateRoom}>Создать комнату</button>

            {showCreateRoom && (
                <div className="modal-overlay active">
                    <div className="modal-content">
                        <h2>Создать комнату</h2>
                        <form onSubmit={handleSubmitRoom}>
                            <input
                                type="text"
                                name="name"
                                placeholder="Название комнаты"
                                value={roomDetails.name}
                                onChange={handleInputChange}
                                required
                            />
                            <input
                                type="number"
                                name="playerCount"
                                placeholder="Количество игроков"
                                value={roomDetails.playerCount}
                                onChange={handleInputChange}
                                required
                            />
                            <input
                                type="text"
                                name="theme"
                                placeholder="Тема викторины"
                                value={roomDetails.theme}
                                onChange={handleInputChange}
                                required
                            />
                            <input
                                type="number"
                                name="answerTime"
                                placeholder="Время ответа (в секундах)"
                                value={roomDetails.answerTime}
                                onChange={handleInputChange}
                                required
                            />
                            <button type="submit">Создать комнату</button>
                            <button type="button" onClick={() => setShowCreateRoom(false)}>
                                Отмена
                            </button>
                        </form>
                    </div>
                </div>
            )}
        </div>
    );
};

export default CreateRoomComponent;
