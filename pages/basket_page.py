from pages.locators import BasketPageLocators
from pages.base_page import BasePage


class BasketPage(BasePage):

    def verify_basket_is_empty(self):
        assert BasketPageLocators.BASKET_IS_EMPTY_TEXT in self.driver.page_source, "\n Basket is not empty"
