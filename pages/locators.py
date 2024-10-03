from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTERED_FORM = (By.CSS_SELECTOR, "#register_form_2")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form_4")

class BasketLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    TEXT_MESSAGE_WITH_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    TEXT_MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
