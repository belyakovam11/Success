# Используем актуальный базовый образ Node.js
FROM node:18-alpine

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src/app

# Добавляем директорию node_modules в PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# Копируем файл зависимостей и устанавливаем зависимости
COPY package.json ./
RUN npm install --silent
RUN npm install react-scripts@5.0.1 -g --silent  # Используем обновленную версию react-scripts

# Копируем остальные файлы приложения в рабочую директорию контейнера
COPY . . 

# Указываем команду для старта приложения
CMD ["npm", "start"]

# Открываем порт 3000 для работы приложения
EXPOSE 3000
