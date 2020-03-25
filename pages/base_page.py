from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import BasePageLocators


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def go_to_basket_page(self):
        self.driver.find_element(*BasePageLocators.BASKET_BUTTON).click()

    def go_to_login_page(self):
        self.driver.find_element(*BasePageLocators.LOGIN_LINK).click()  # asterisk symbol "*" means a pare is transferred

    def is_disappeared(self, how, what):
        try:
            WebDriverWait(self.driver, 4).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what):
        try:
            WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.driver.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK)



