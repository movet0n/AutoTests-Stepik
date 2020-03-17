import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


link = "http://suninjuly.github.io/explicit_wait2.html"
driver = webdriver.Chrome()
driver.get(link)

price = WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

book = driver.find_element_by_id("book").click()

x = driver.find_element_by_id("input_value").text
equation = math.log(abs(12 * math.sin(int(x))))
answer_input = driver.find_element_by_id("answer").send_keys(str(equation))

submit = driver.find_element_by_css_selector("[type='submit'").click()