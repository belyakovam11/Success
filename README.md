
## Используемые технологии




### 1. **.github**
- **Назначение**: Содержит конфигурационные файлы для непрерывной интеграции (CI).
- **Технологии**: Используются GitHub Actions для автоматического тестирования и развертывания.

### 2. **backend**
- **Фреймворк**: [Django](https://www.djangoproject.com/) — высокоуровневый веб-фреймворк на Python, который способствует быстрой разработке и чистому, прагматичному дизайну.
- **Асинхронные задачи**: [Celery](https://docs.celeryproject.org/en/stable/) — асинхронная очередь задач, основанная на распределенной передаче сообщений. Используется для обработки фоновых задач.
- **Тестирование**: [pytest](https://docs.pytest.org/en/latest/) — фреймворк для тестирования, который упрощает создание простых и масштабируемых тестов.
- **Структура**:
  - `manage.py` — утилита командной строки для выполнения административных задач.
  - `requirements.txt` — список зависимостей для проекта.

### 3. **env**
- **Назначение**: Виртуальное окружение для Python, чтобы изолировать зависимости проекта.
- **Инструменты**: Использует [venv](https://docs.python.org/3/library/venv.html) для создания легковесной среды, которая может содержать свои собственные зависимости.

### 4. **frontend**
- **Библиотека**: [React](https://reactjs.org/) — библиотека JavaScript для создания пользовательских интерфейсов, позволяющая разрабатывать одностраничные приложения с компонентным подходом.
- **Структура**:
  - `public/` содержит статические файлы, такие как HTML и изображения.
  - `src/` — каталог, в котором находятся логика приложения и компоненты.
  - `package.json` определяет зависимости проекта и скрипты для управления фронтальной частью.

### 5. **nginx**
- **Назначение**: Nginx используется как обратный прокси-сервер, балансировщик нагрузки и HTTP-кэш.
- **Конфигурация**: Содержит конфигурационные файлы, которые определяют поведение сервера и настройки маршрутизации запросов к бэкенду, а также для обслуживания статических файлов.

### 6. **other**
- **Назначение**: Рабочая папка для дополнительных ресурсов, экспериментов и документации.
- **Содержимое**:
  - `diagrams/` — содержит архитектурные диаграммы.
  - `labs/` — включает экспериментальный код или лабораторные задания, связанные с проектом.

### 7. **docker-compose.yml**
Файл `docker-compose.yml` описывает развертывание различных сервисов приложения. Вот основные технологии, которые используются:

- **Сервисы**:
  - **backend**: Собирается на основе Dockerfile из каталога `backend`. Использует порт `5000`.
  - **frontend**: Собирается на основе Dockerfile из каталога `frontend`. Использует порт `3000`.
  - **db**: Использует образ `postgres:13` для работы с базой данных PostgreSQL. Доступен на порту `5432`.
  - **pgadmin**: Интерфейс для управления PostgreSQL. Доступен на порту `5050`.
  - **rabbitmq**: Используется для обработки сообщений. Доступен на порту `5672` и веб-интерфейсе на порту `15672`.
  - **redis**: Используется как кэш и хранилище данных. Доступен на порту `6379`.
  - **mongo**: Использует образ `mongo:latest` для работы с базой данных MongoDB. Доступен на порту `27017`.
  - **nginx**: Обратный прокси-сервер, доступный на порту `80`.
  - **minio**: Объектное хранилище. Доступно на порту `9000` (для хранилища) и `9001` (для консоли).
  - **swagger-ui**: Для визуализации документации API. Доступно на порту `8080`.
  - **swagger-editor**: Веб-интерфейс для редактирования документации API. Доступно на порту `8081`.

- **Volumes**: 
  - `postgres_data`: Для хранения данных PostgreSQL.
  - `mongo_data`: Для хранения данных MongoDB.
  - `minio_data`: Для хранения данных MinIO.

## Начало работы

Чтобы начать работу с проектом, выполните следующие шаги:

1. Клонируйте репозиторий:
   ```bash
   git clone <ссылка-на-репозиторий>
   cd <имя-репозитория>
   
