import time
from selenium import webdriver


link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    input1 = driver.find_element_by_css_selector("[name='first_name']")
    input1.send_keys("Alex")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Okrepkyi")
    input3 = driver.find_element_by_css_selector("[name='firstname']")
    input3.send_keys("Kyiv")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Ukraine")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    driver.quit()