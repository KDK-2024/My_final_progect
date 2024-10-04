import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                    help="Choose user_language, e.g., 'ru', 'en', etc.")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # Создаем экземпляр браузера
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nClosing browser..")
    browser.quit()