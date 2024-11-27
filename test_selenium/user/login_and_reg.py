from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    print("login_and_reg.py")
    # Открытие страницы аутентификации
    driver.get("http://localhost:3000/")  # Убедитесь, что ваш путь к компоненту правильный

    # Проверка переключения на вкладку "Регистрация"
    register_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Регистрация']"))
    )
    register_tab.click()

    # Ожидание появления формы регистрации
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "form"))
    )

    # Заполнение полей формы регистрации
    username_field = driver.find_element(By.NAME, "username")
    email_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("testuser1")
    email_field.send_keys("testuser1@example.com")
    password_field.send_keys("testpassword1")

    # Нажатие на кнопку "Зарегистрироваться"
    register_button = driver.find_element(By.CSS_SELECTOR, ".login__submit")
    register_button.click()

    # Проверка успешного сообщения
    register_success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "message"))
    ).text
    assert "Успешно зарегистрированы!" in register_success_message, "Регистрация не удалась."

    print("Регистрация прошла успешно!")

    # Переключение на вкладку "Вход"
    login_tab = driver.find_element(By.XPATH, "//button[text()='Вход']")
    login_tab.click()

    # Ожидание появления формы входа
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "form"))
    )

    # Заполнение полей формы входа
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("testuser")
    password_field.send_keys("testpassword")

    # Нажатие на кнопку "Войти"
    login_button = driver.find_element(By.CSS_SELECTOR, ".login__submit")
    login_button.click()

    # Проверка успешного входа через редирект
    WebDriverWait(driver, 10).until(
        EC.url_contains("/main")  # Проверка, что URL содержит "/main"
    )
    print("Вход прошел успешно!")

finally:
    # Закрытие браузера
    driver.quit()
