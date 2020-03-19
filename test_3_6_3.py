import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def driver():

    print("\n--- start browser for test ---")
    driver = webdriver.Chrome()
    yield driver
    print("\n--- quit browser ---")
    driver.quit()


@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_some_useful_text_here(driver, lesson):

    link = f"https://stepik.org/lesson/{lesson}/step/1"
    driver.get(link)

    # calculate an answer
    answer = math.log(int(time.time()))

    # wait until an input field is clickable, send calculated answer and submit
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ember68"))).send_keys(str(answer))
    driver.find_element_by_css_selector(".submit-submission").click()

    # wait until text is visible
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".smart-hints__hint"), "Correct!"))
    actual_text = driver.find_element_by_css_selector(".smart-hints__hint").text
    expected_text = "Correct!"

    secret_text = ""

    try:
        assert actual_text == expected_text, f"{actual_text} does not correspond to the {expected_text}"
    except:
        secret_text.join(actual_text)
        print(actual_text)


