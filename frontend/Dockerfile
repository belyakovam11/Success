# Используем актуальный базовый образ Node.js
FROM node:18-alpine
# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
# Устанавливаем react-scripts с увеличением лимита памяти
RUN NODE_OPTIONS="--max_old_space_size=1024"
RUN npm install --silent
RUN npm install react-scripts@5.0.1 -g --silent

# add app
COPY . ./

# start app
CMD ["npm", "start"]
# Открываем порт 3000 для работы приложения
EXPOSE 3000