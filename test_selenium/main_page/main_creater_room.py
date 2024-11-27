from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    print("main_creater_room.py")
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
        EC.presence_of_element_located((By.CLASS_NAME, "room-card"))
    )
    print("Комнаты успешно загружены!")

    # Шаг 4: Создание новой комнаты
    create_room_button = driver.find_element(By.CLASS_NAME, "create-room-button")
    create_room_button.click()

    # Ожидание появления формы для создания комнаты
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "form"))
    )

    # Заполнение формы для создания комнаты
    room_name_field = driver.find_element(By.NAME, "name")
    player_count_field = driver.find_element(By.NAME, "playerCount")
    theme_select = driver.find_element(By.NAME, "theme")

    room_name_field.send_keys("Test Room5")
    player_count_field.send_keys("10")
    theme_select.send_keys("Спорт")  # Выбор темы

    # Нажатие на кнопку "Создать комнату"
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ожидание подтверждения создания комнаты
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "toast"))
    )
    print("Комната успешно создана!")

finally:
    # Закрытие браузера
    driver.quit()
