from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn")

class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")

class LoginPageLocators():
    REGISTERED_FORM = (By.CSS_SELECTOR, "#register_form_2")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form_4")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    TEXT_MESSAGE_WITH_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    TEXT_MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")