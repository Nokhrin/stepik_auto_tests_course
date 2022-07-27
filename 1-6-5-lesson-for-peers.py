from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) # динамическое ожидание загрузки элементов с максимальным временем ожидания 10 секунд

    # url = 'http://suninjuly.github.io/registration1.html'
    url = 'http://suninjuly.github.io/registration2.html'

    driver.get(url)

    input1 = driver.find_element(By.CSS_SELECTOR, '.first_block .first')
    input1.send_keys('FirstName')
    input2 = driver.find_element(By.CSS_SELECTOR, '.first_block .second')
    input2.send_keys('LastName')
    input3 = driver.find_element(By.CSS_SELECTOR, '.first_block .third')
    input3.send_keys('FirstName@LastName.an')

    submit_button = driver.find_element(By.CSS_SELECTOR, '.btn-default')
    submit_button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    driver.quit()
