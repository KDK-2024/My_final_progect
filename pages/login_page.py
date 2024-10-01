from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        except NoSuchElementException:
            return False
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        try:
            self.browser.find_element(*LoginPageLocators.REGISTERED_FORM)
        except NoSuchElementException:
            return False
        assert True