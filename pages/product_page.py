import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def is_present_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "'Add to basket' button is not present"

    def print_secret_code(self):
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            secret_code = alert_text.split()[-1]
            print(secret_code)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def solve_quiz_and_get_code(self):
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            x = int(alert_text.split()[2])
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
        except NoAlertPresentException:
            print("No first alert presented")

    def verify_deferred_benefit_offer_is_present(self):
        def_ben_offer = self.driver.find_element(*ProductPageLocators.DEF_BEN_OFFER).text
        assert def_ben_offer in self.driver.page_source, f"{def_ben_offer} has not been found in the source page"

    def verify_book_titles_are_similar(self):
        book_title = self.driver.find_element(*ProductPageLocators.BOOK_TITLE).text
        book_title_success = self.driver.find_element(*ProductPageLocators.BOOK_TITLE_SUCCESS).text
        assert book_title == book_title_success, f"{book_title} is not similar to the {book_title_success}"

    def verify_success_message_is_present(self):
        success_text = "has been added to your basket"
        assert success_text in self.driver.page_source, f"'{success_text}' text has not been found in the source page"

    def verify_book_prices_are_similar(self):
        book_price = self.driver.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price_navbar = self.driver.find_element(*ProductPageLocators.BOOK_PRICE_NAVBAR).text
        assert book_price == book_price_navbar, f"{book_price} is not similar to the {book_price_navbar}"

    def verify_success_message_is_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "success message should not be present"

    def verify_success_message_is_not_present_with_disappear_function(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "looks like success message should not be present?"
