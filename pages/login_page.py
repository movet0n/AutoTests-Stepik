from pages.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        self.driver.find_element(*LoginPageLocators.REG_EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*LoginPageLocators.REG_PASSWORD_1_FIELD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REG_PASSWORD_2_FIELD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.driver.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FIELD), "'login email' field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), "'login password' field is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_FIELD), "'reg email' field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_1_FIELD), "'reg password' field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_2_FIELD), "'reg confirm password' field is not presented"
