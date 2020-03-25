import time
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import BasePageLocators


@pytest.mark.skip
def test_guest_can_go_to_login_page(driver):
    link = BasePageLocators.BASE_PAGE_LINK
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(driver, url=driver.current_url)
    login_page.should_be_login_page()


@pytest.mark.skip
def test_guest_should_see_login_link(driver):
    link = BasePageLocators.BASE_PAGE_LINK
    page = MainPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    link = BasePageLocators.BASE_PAGE_LINK
    page = MainPage(driver, link)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(driver, url=driver.current_url)
    basket_page.verify_basket_is_empty()
