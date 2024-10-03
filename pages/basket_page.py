from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Product is present in the basket"