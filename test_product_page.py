import time
import pytest
from pages.locators import ProductPageLocators
from pages.locators import LoginPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


@pytest.mark.user_login
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        link = ProductPageLocators.PRODUCT_LINK
        page = ProductPage(driver, link)
        page.open()
        page.go_to_login_page()

        login_page = LoginPage(driver, url=driver.current_url)
        login_page.register_new_user(LoginPageLocators.REG_EMAIL, LoginPageLocators.REG_PASSWORD)

        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, driver):
        link = ProductPageLocators.PRODUCT_LINK
        page = ProductPage(driver, link)
        page.open()
        page.verify_success_message_is_not_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        link = ProductPageLocators.PRODUCT_LINK
        page = ProductPage(driver, link)
        page.open()
        page.is_present_add_to_basket_button()
        page.add_to_basket()
        page.verify_book_titles_are_similar()
        page.verify_success_message_is_present()
        page.verify_deferred_benefit_offer_is_present()
        page.verify_book_prices_are_similar()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(driver):
    link = ProductPageLocators.PRODUCT_LINK_PROMO
    page = ProductPage(driver, link)
    page.open()
    page.is_present_add_to_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.verify_book_titles_are_similar()
    page.verify_success_message_is_present()
    page.verify_deferred_benefit_offer_is_present()
    page.verify_book_prices_are_similar()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = ProductPageLocators.THE_CITY_AND_THE_STARS_LINK
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(driver, link)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(driver, url=driver.current_url)
    basket_page.verify_basket_is_empty()


def test_guest_should_see_login_link_on_product_page(driver):
    link = ProductPageLocators.THE_CITY_AND_THE_STARS_LINK
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail(reason="success message should be present after adding a book to the basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.verify_success_message_is_not_present()


def test_guest_cant_see_success_message(driver):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(driver, link)
    page.open()
    page.verify_success_message_is_not_present()


@pytest.mark.xfail(reason="success message should not disappear")
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.verify_success_message_is_not_present_with_disappear_function()
