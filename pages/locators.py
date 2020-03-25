from selenium.webdriver.common.by import By


class BasePageLocators:
    BASE_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")


class BasketPageLocators:
    BASKET_IS_EMPTY_TEXT = "Your basket is empty"


class LoginPageLocators:

    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators:

    PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    THE_CITY_AND_THE_STARS_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    BOOK_TITLE = (By.CSS_SELECTOR, ".row h1")
    BOOK_TITLE_SUCCESS = (By.CSS_SELECTOR, ".alert:first-child .alertinner strong")
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_PRICE = (By.CSS_SELECTOR, ".row p.price_color")
    BOOK_PRICE_NAVBAR = (By.CSS_SELECTOR, ".alert:nth-child(3) .alertinner strong")
    DEF_BEN_OFFER = (By.CSS_SELECTOR, ".alert:nth-child(2) .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(2) .alertinner strong")
