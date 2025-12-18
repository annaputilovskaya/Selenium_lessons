import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'filename.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("John")
    browser.find_element(By.NAME, "lastname").send_keys("Doe")
    browser.find_element(By.NAME, "email").send_keys("11@vv.ru")
    browser.find_element(By.ID, "file").send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(20)
    browser.quit()
