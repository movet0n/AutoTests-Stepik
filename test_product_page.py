import time
import pytest
from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail(reason="word 'book' is present")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_alert_equation_solution(driver, link):
    page = ProductPage(driver, link)
    page.open()
    page.is_present_add_to_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.verify_book_titles_are_similar()
    page.verify_success_message_is_present()
    page.verify_deferred_benefit_offer_is_present()
    page.verify_book_prices_are_similar()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(driver):
    link = ProductPageLocators.THE_CITY_AND_THE_STARS_LINK
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = ProductPageLocators.THE_CITY_AND_THE_STARS_LINK
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(driver, link)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(driver, url=driver.current_url)
    basket_page.verify_basket_is_empty()
