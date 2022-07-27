from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
import time
import math
import os

chrome_service = ChromeService(
    # executable_path=ChromeDriverManager().install()
    executable_path='../drivers/chromedriver'
)
chrome_options = webdriver.ChromeOptions()
# chrome_options.headless = True


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    driver = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )
    # driver.implicitly_wait(10)

    link = 'http://suninjuly.github.io/explicit_wait2.html'
    driver.get(link)


    price = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()

    x_value = driver.find_element(By.ID, 'input_value').text
    y_value = calc(x=int(x_value))

    # answer_input
    driver.find_element(By.ID, 'answer').send_keys(str(y_value))

    # submit
    driver.find_element(By.ID, 'solve').click()

    # copy answer
    alert_text = driver.switch_to.alert.text.split(' ')
    print(alert_text[len(alert_text) - 1])

finally:
    time.sleep(60)
    driver.quit()
