import pytest

from pages.product_page import ProductPage

@pytest.mark.parametrize('promo_number', ["0", "1", "2", "3", "4", "5",
                                          "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}"
    page = ProductPage(browser, link)       # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    product_name = page.get_product_name()
    print("Получили имя")
    product_price = page.get_product_price()
    print("Получили цену")
    page.adding_a_book_to_basket()
    print("Добавили товар в корзину")
    page.solve_quiz_and_get_code()
    print("Решили задачу")
    page.should_be_correct_product(product_name)
    print("Сравнили имя товара")
    page.should_be_correct_price(product_price)
    print("Сравнили цену товара")