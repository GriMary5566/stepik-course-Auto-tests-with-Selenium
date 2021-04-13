from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    button_book = browser.find_element_by_id("book")
    button_book.click()
    get_x = browser.find_element_by_id("input_value")
    x = get_x.text
    y = calc(x)
    y_input = browser.find_element_by_id("answer")
    y_input.send_keys(y)
    button_submit = browser.find_element_by_id("solve")
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    