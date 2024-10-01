from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTERED_FORM = (By.CSS_SELECTOR, "#register_form_2")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form_4")