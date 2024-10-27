import psycopg2
from psycopg2 import OperationalError

def test_db_connection():
    try:
        # Настройки подключения должны соответствовать настройкам в settings.py
        connection = psycopg2.connect(
            database="django",      # Имя базы данных
            user="django",          # Пользователь
            password="django",       # Пароль
            host="db-1",            # Название контейнера или 'localhost' для локальной БД
            port="5432"             # Порт PostgreSQL
        )
        
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("Подключение успешно. Версия PostgreSQL:", db_version)
        
    except OperationalError as e:
        print("Ошибка подключения:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    test_db_connection()
