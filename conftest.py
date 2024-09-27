import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                    help="Choose user_language, e.g., 'ru', 'en-gb', etc.")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    # Создаем экземпляр браузера
    browser = webdriver.Chrome()

    # Открытие базового URL
    base_url = "http://selenium1py.pythonanywhere.com/"

    # Добавляем язык в URL, используя значение, переданное через параметр
    full_url = f"{base_url}{user_language}/catalogue/coders-at-work_207/"

    browser.get(full_url)

    yield browser
    print("\nClosing browser..")
    browser.quit()