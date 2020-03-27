import random
from selenium.webdriver.common.by import By


class BasePageLocators:

    # links
    BASE_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"

    # selectors
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:

    # selectors
    BASKET_IS_EMPTY_TEXT = "Your basket is empty"


class LoginPageLocators:

    # links
    LOGIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"

    # selectors
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > .btn")

    # registration data
    REG_EMAIL = str(random.random()) + "@email.com"
    REG_PASSWORD = "password_"


class ProductPageLocators:

    # links
    PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    PRODUCT_LINK_PROMO = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    THE_CITY_AND_THE_STARS_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    # selectors
    BOOK_TITLE = (By.CSS_SELECTOR, ".row h1")
    BOOK_TITLE_SUCCESS = (By.CSS_SELECTOR, ".alert:first-child .alertinner strong")
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_PRICE = (By.CSS_SELECTOR, ".row p.price_color")
    BOOK_PRICE_NAVBAR = (By.CSS_SELECTOR, ".alert:nth-child(3) .alertinner strong")
    DEF_BEN_OFFER = (By.CSS_SELECTOR, ".alert:nth-child(2) .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(2) .alertinner strong")
