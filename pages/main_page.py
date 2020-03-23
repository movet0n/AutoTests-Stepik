from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        self.driver.find_element(*MainPageLocators.LOGIN_LINK).click()  # asterix "*" means a pare is transferred
        # return LoginPage(driver=self.driver, url=self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
