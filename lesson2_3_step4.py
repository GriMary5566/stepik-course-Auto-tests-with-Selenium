from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button_begin = browser.find_element_by_tag_name("button")
    button_begin.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    get_x = browser.find_element_by_id("input_value")
    x = get_x.text
    y = calc(x)
    y_input = browser.find_element_by_id("answer")
    y_input.send_keys(y)
    button_submit = browser.find_element_by_css_selector("button.btn")
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    