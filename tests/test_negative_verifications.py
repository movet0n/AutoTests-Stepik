import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


@pytest.mark.xfail(reason="success message should be present after adding a book to the cart")
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


@pytest.mark.xfail(reason="success message shold not disappear")
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.verify_success_message_is_not_present_with_disappear_function()
