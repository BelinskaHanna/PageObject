from pages.login_page import LoginPage

from pages.products_page import ProductsPage


def test_login_standard_user(navigate_to_url, username_standard, password):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard(username_standard)
    login_page.enter_password(password)
    login_page.click_login()
    products_page = ProductsPage(navigate_to_url)
    assert products_page.is_login_visible


def test_login_performance_user(navigate_to_url, username_performance, password):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_performance(username_performance)
    login_page.enter_password(password)
    login_page.click_login()
    products_page = ProductsPage(navigate_to_url)
    assert products_page.is_login_visible


def test_log_out_standard_user(navigate_to_url, username_standard, password):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard(username_standard)
    login_page.enter_password(password)
    login_page.click_login()
    products_page = ProductsPage(navigate_to_url)
    products_page.burger_window_click()
    products_page.logout_visible()
    products_page.logout()
    assert login_page.is_login_visible


def test_log_out_performance(navigate_to_url, username_performance, password):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_performance(username_performance)
    login_page.enter_password(password)
    login_page.click_login()
    products_page = ProductsPage(navigate_to_url)
    products_page.burger_window_click()
    products_page.logout_visible()
    products_page.logout()
    assert login_page.is_login_visible


def test_invalid_login(navigate_to_url):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard("Test")
    login_page.enter_password("Test123")
    login_page.click_login()
    assert login_page.is_error_message_displayed
