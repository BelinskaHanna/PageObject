from pages.login_page import LoginPage

from pages.products_page import ProductsPage


def test_login_standard_user(logged_in_standard_user):
    products_page = ProductsPage(logged_in_standard_user)
    assert products_page.is_login_visible


def test_login_performance_user(logged_in_performance_user):
    products_page = ProductsPage(logged_in_performance_user)
    assert products_page.is_login_visible


def test_log_out_standard_user(logged_in_standard_user):
    products_page = logged_in_standard_user
    products_page.burger_window_click()
    logout_button = products_page.find(products_page.LOGOUT_VISIBLE)
    assert logout_button.is_displayed()


def test_log_out_performance(logged_in_performance_user, username_performance, password):
    products_page = logged_in_performance_user
    products_page.burger_window_click()
    logout_button = products_page.find(products_page.LOGOUT_VISIBLE)
    assert logout_button.is_displayed()


def test_invalid_login(navigate_to_url):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard("Test")
    login_page.enter_password("Test123")
    login_page.click_login()
    assert login_page.is_error_message_displayed
