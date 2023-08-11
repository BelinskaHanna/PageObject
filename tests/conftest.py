import pytest

from selenium import webdriver

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture
def start_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def navigate_to_url(start_driver):
    driver = start_driver
    driver.get("https://www.saucedemo.com/")
    yield driver


@pytest.fixture
def username_standard():
    return "standard_user"


@pytest.fixture
def password():
    return "secret_sauce"


@pytest.fixture
def username_performance():
    return "performance_glitch_user"


@pytest.fixture
def first_name():
    return "Hanna"


@pytest.fixture
def last_name():
    return "Belinska"


@pytest.fixture
def zip_code():
    return "65000"


@pytest.fixture
def logged_in_standard_user(start_driver, navigate_to_url, username_standard, password):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard(username_standard)
    login_page.enter_password(password)
    login_page.click_login()
    yield ProductsPage(start_driver)


@pytest.fixture
def logged_in_performance_user(start_driver, navigate_to_url, username_performance, password):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_performance(username_performance)
    login_page.enter_password(password)
    login_page.click_login()
    yield ProductsPage(start_driver)
