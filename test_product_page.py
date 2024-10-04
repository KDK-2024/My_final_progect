import pytest
import time
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

@pytest.mark.need_review
@pytest.mark.parametrize('promo_number', ["0", "1", "2", "3", "4", "5",
                                          "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}"
    page = ProductPage(browser, link)       # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.adding_a_book_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_product(product_name)
    page.should_be_correct_price(product_price)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.adding_a_book_to_basket()
    page.should_not_be_success_message()            # проверка, что сообщение об успехе не отображается после добавления товара

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()            # проверка, что сообщение об успехе не отображается до добавления товара

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.adding_a_book_to_basket()
    page.should_disappeared()                       # проверка, что сообщение об успехе исчезает после добавления товара

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()                                     #Открываем страницу
    page.should_be_login_link()                     #Проверка наличия кнопки для перехода на страницу логина

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()                                     # Открываем страницу
    page.should_be_login_link()                     # Проверка наличия кнопки для перехода на страницу логина
    page.go_to_login_page()                         # Переход на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()               # Проверка, перешли на страницу логина

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()                                                     # Открываем страницу
    page.go_to_basket()                                             # Переход на страницу корзины
    basket_page = BasketPage(browser, browser.current_url)          # Создание экземпляра BasketPage
    basket_page.should_be_empty_basket()                            # Проверяем, что корзина пустая
    basket_page.should_not_be_product_in_basket()                   # Проверяем, что в корзине нет товара

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser,link)
        page.open()                                                 # открываем страницу
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "12345!"
        page.register_new_user(email, password)                     # Регистрируем нового пользователя
        page.should_be_authorized_user()                            # Проверяем, что пользователь авторизован
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)                   # Создаем объект ProductPage
        page.open()                                         # Открываем страницу товара
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.adding_a_book_to_basket()
        page.should_be_correct_product(product_name)
        page.should_be_correct_price(product_price)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()                # проверка, что сообщение об успехе не отображается до добавления товара