import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(num1+num2))

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(20)
    browser.quit()
