from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.driver.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL)
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL)
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD)
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_2)
