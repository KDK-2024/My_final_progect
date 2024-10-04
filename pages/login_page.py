from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)                                    # Вводим email в поле регистрации

        password_field_1 = self.browser.find_element(*LoginPageLocators.FIRST_PASSWORD_FIELD)
        password_field_1.send_keys(password)                            # Вводим пароль в первое поле пароля

        password_field_2 = self.browser.find_element(*LoginPageLocators.SECOND_PASSWORD_FIELD)
        password_field_2.send_keys(password)                            # Вводим пароль во второе поле пароля

        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        register_button.click()                                         # Кликаем по кнопке регистрации

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