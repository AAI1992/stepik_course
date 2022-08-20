from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # enter required data
    input1 = browser.find_element(By.XPATH, '//input[@placeholder="Enter first name"]')
    input1.send_keys("Alina")
    input2 = browser.find_element(By.XPATH, '//input[@placeholder="Enter last name"]')
    input2.send_keys("Malina")
    input3 = browser.find_element(By.XPATH, '//input[@placeholder="Enter email"]')
    input3.send_keys("ai@mail.com")

    # attach file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')

    input4 = browser.find_element(By.ID, "file")
    input4.send_keys(file_path)

    # submit
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # 30 seconds to copy code
    time.sleep(30)
    
    # closing browser
    browser.quit()
