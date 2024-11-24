# Используем актуальный базовый образ Node.js
FROM node:18-alpine

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Добавляем `/app/node_modules/.bin` в $PATH
ENV PATH /app/node_modules/.bin:$PATH

# Копируем файл зависимостей и устанавливаем зависимости
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent

# Устанавливаем react-router-dom
RUN npm install react-router-dom --silent

# Копируем остальные файлы приложения в рабочую директорию контейнера
COPY . .

# Устанавливаем переменные окружения для уменьшения использования памяти
ENV NODE_OPTIONS="--max_old_space_size=512"

# Указываем команду для старта приложения
CMD ["npm", "start"]

# Открываем порт 3000 для работы приложения
EXPOSE 3000
