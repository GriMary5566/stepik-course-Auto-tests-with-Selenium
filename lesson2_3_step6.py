from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button_begin = browser.find_element_by_tag_name("button")
    button_begin.click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    get_x = browser.find_element_by_id("input_value")
    x = get_x.text
    y = calc(x)
    y_input = browser.find_element_by_id("answer")
    y_input.send_keys(y)
    button_submit = browser.find_element_by_css_selector("button.btn")
    button_submit.click()
    print(browser.switch_to.alert.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
