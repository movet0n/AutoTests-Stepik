import unittest
import time
from selenium import webdriver


class FirstUnittest(unittest.TestCase):

    def test_login_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        driver = webdriver.Chrome()
        driver.get(link)

        driver.find_element_by_css_selector(".first_block .form-control.first").send_keys("Alex")
        driver.find_element_by_css_selector(".first_block .form-control.second").send_keys("Okrepkyi")
        driver.find_element_by_css_selector(".first_block .form-control.third").send_keys("some@email.com")

        button = driver.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)

        expected_result = driver.find_element_by_css_selector("h1").text
        actual_result = "Congratulations! You have successfully registered!"

        self.assertEqual(actual_result, expected_result, f"'{actual_result}' is not euqal to '{expected_result}'")

    def test_login_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        driver = webdriver.Chrome()
        driver.get(link)

        driver.find_element_by_css_selector(".first_block .form-control.first").send_keys("Alex")
        driver.find_element_by_css_selector(".first_block .form-control.second").send_keys("Okrepkyi")
        driver.find_element_by_css_selector(".first_block .form-control.third").send_keys("some@email.com")

        button = driver.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)

        expected_result = driver.find_element_by_css_selector("h1").text
        actual_result = "Congratulations! You have successfully registered!"

        self.assertEqual(actual_result, expected_result, f"'{actual_result}' is not euqal to '{expected_result}'")


if __name__ == "__main__":
    unittest.main()

