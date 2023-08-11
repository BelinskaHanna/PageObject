import pytest

from selenium import webdriver


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
