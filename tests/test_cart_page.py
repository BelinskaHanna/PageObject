from pages.login_page import LoginPage

from pages.products_page import ProductsPage

from pages.cart_page import CartPage


def test_remove_from_cart(navigate_to_url, username_standard, password):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard(username_standard)
    login_page.enter_password(password)
    login_page.click_login()
    products_page = ProductsPage(navigate_to_url)
    products_page.click_add_to_cart()
    products_page.click_on_cart()
    cart_page = CartPage(navigate_to_url)
    cart_page.remove_from_cart()
    assert not products_page.is_cart_updated()


def test_continue_shopping(navigate_to_url, username_standard, password):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard(username_standard)
    login_page.enter_password(password)
    login_page.click_login()
    products_page = ProductsPage(navigate_to_url)
    products_page.click_add_to_cart()
    products_page.click_on_cart()
    cart_page = CartPage(navigate_to_url)
    cart_page.click_continue_shopping()
    assert cart_page.product_page_after_cart()


def test_checkout(navigate_to_url, username_standard, password):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard(username_standard)
    login_page.enter_password(password)
    login_page.click_login()
    products_page = ProductsPage(navigate_to_url)
    products_page.click_add_to_cart()
    products_page.click_on_cart()
    cart_page = CartPage(navigate_to_url)
    cart_page.click_checkout()
    assert cart_page.product_page_after_cart()
