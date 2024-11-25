from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Шаг 1: Открытие страницы и выполнение входа
    driver.get("http://localhost:3000/")  # Путь к странице входа

    # Ожидание появления формы входа
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    # Заполнение полей формы входа
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("testuser")
    password_field.send_keys("testpassword")

    # Нажатие на кнопку "Войти"
    login_button = driver.find_element(By.CSS_SELECTOR, ".login__submit")
    login_button.click()

    # Шаг 2: Ожидание редиректа на страницу /main
    WebDriverWait(driver, 10).until(
        EC.url_contains("/main")  # Проверка, что URL содержит "/main"
    )
    print("Вход прошел успешно и вы перешли на страницу /main")

    # Шаг 3: Проверка доступных комнат на странице
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "room-card"))
    )
    print("Комнаты успешно загружены!")

    # Шаг 4: Поиск и переход в созданную комнату
    room_links = driver.find_elements(By.CLASS_NAME, "room-card")
    
    room_found = False
    for room in room_links:
        if "Test Room2" in room.text:  # Если название комнаты содержит "Test Room2"
            room.click()  # Переход в комнату
            room_found = True
            print("Вы перешли в комнату.")
            break
    
    if not room_found:
        print("Комната 'Test Room2' не найдена!")

    # Шаг 5: Нажатие на кнопку "СТАРТ" для начала викторины
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".start-button"))
    )
    start_button = driver.find_element(By.CSS_SELECTOR, ".start-button")
    start_button.click()

    # Ожидание начала викторины
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "quiz-section"))
    )
    print("Викторина началась!")

    # Шаг 6: Ответ на вопросы
    while True:
        try:
            # Поиск текста вопроса и опций для ответа
            question_text = driver.find_element(By.CLASS_NAME, "quiz-section").find_element(By.TAG_NAME, "p").text
            options = driver.find_elements(By.CSS_SELECTOR, ".option-button")
            
            # Логика выбора ответа (например, первый вариант)
            correct_answer = options[0].text

            # Нажатие на кнопку с правильным ответом
            for option in options:
                if option.text == correct_answer:
                    option.click()
                    break
            
            # Подтверждение ответа и ожидание появления следующего вопроса
            WebDriverWait(driver, 5).until(
                EC.staleness_of(options[0])  # Ожидание исчезновения предыдущих опций
            )

            # Ожидание появления новых опций (следующий вопрос)
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".option-button"))
            )

            print("Переход к следующему вопросу...")
            time.sleep(1)  # Небольшая задержка перед следующим вопросом

        except Exception as e:
            print(f"Викторина завершена {e}")
            time.sleep(5)  # Небольшая задержка перед следующим вопросом
            break

    # Шаг 8: Проверка редиректа на главную страницу
    WebDriverWait(driver, 10).until(
        EC.url_contains("/main")  # Проверка, что URL содержит "/main"
    )
    print("Вы успешно перешли на страницу /main")

finally:
    # Закрытие браузера
    driver.quit()
