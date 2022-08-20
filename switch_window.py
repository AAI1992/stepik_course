from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # submit
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # switch to another window
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # find element
    x_element = browser.find_element(By.ID, "input_value").text
    x = int(x_element)

    # counting result
    result = str(math.log(abs(12 * math.sin(int(x)))))

    # input result
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(result)

    # submit
    button1 = browser.find_element(By.TAG_NAME, "button")
    button1.click()

finally:
    # 10 seconds to copy code
    time.sleep(10)

    # closing browser
    browser.quit()
