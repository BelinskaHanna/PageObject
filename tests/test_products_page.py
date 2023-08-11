from pages.login_page import LoginPage

from pages.products_page import ProductsPage


def test_add_to_cart(navigate_to_url, username_standard, password):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard(username_standard)
    login_page.enter_password(password)
    login_page.click_login()
    products_page = ProductsPage(navigate_to_url)
    products_page.click_add_to_cart()
    assert products_page.is_cart_updated()


def test_remove(navigate_to_url, username_standard, password):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard(username_standard)
    login_page.enter_password(password)
    login_page.click_login()
    products_page = ProductsPage(navigate_to_url)
    products_page.click_add_to_cart()
    products_page.remove()
    assert not products_page.is_cart_updated()


def test_select_tshirt_red(navigate_to_url, username_standard, password):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard(username_standard)
    login_page.enter_password(password)
    login_page.click_login()
    products_page = ProductsPage(navigate_to_url)
    products_page.select_tshirt_red()
    assert products_page.is_on_product_page()
