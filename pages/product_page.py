from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def adding_a_book_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_name_book_in_message(self):
        return self.browser.find_element(*ProductPageLocators.TEXT_MESSAGE_WITH_NAME).text

    def get_price_book_in_message(self):
        return self.browser.find_element(*ProductPageLocators.TEXT_MESSAGE_WITH_PRICE).text

    def should_be_correct_product(self, expected_name):
        real_name = self.get_name_book_in_message()
        assert real_name == expected_name, f"Expected product name '{expected_name}', but got '{real_name}'"

    def should_be_correct_price(self, expected_price):
        real_price = self.get_price_book_in_message()
        assert real_price == expected_price, f"Expected product price '{expected_price}', but got '{real_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"