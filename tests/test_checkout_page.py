import pytest

from pages.checkout_page import CheckoutPage

from pages.login_page import LoginPage

from pages.products_page import ProductsPage

from pages.cart_page import CartPage


def test_valid_checkout_data(navigate_to_url, username_standard, password, first_name, last_name, zip_code):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard(username_standard)
    login_page.enter_password(password)
    login_page.click_login()
    products_page = ProductsPage(navigate_to_url)
    products_page.click_add_to_cart()
    products_page.click_on_cart()
    cart_page = CartPage(navigate_to_url)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(navigate_to_url)
    checkout_page.fill_first_name(first_name)
    checkout_page.fill_last_name(last_name)
    checkout_page.fill_zip_code(zip_code)
    checkout_page.click_continue()
    assert checkout_page.finish_is_on_the_page()


@pytest.mark.parametrize("first_name", [""])
def test_empty_first_name(navigate_to_url, username_standard, password, first_name, last_name, zip_code):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard(username_standard)
    login_page.enter_password(password)
    login_page.click_login()
    products_page = ProductsPage(navigate_to_url)
    products_page.click_add_to_cart()
    products_page.click_on_cart()
    cart_page = CartPage(navigate_to_url)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(navigate_to_url)
    checkout_page.fill_first_name(first_name)
    checkout_page.fill_last_name(last_name)
    checkout_page.fill_zip_code(zip_code)
    checkout_page.click_continue()
    if first_name == "":
        assert checkout_page.is_error_message_displayed()
    else:
        assert checkout_page.finish_is_on_the_page()


def test_cancel_shopping(navigate_to_url, username_standard, password, first_name, last_name, zip_code):
    login_page = LoginPage(navigate_to_url)
    login_page.enter_username_standard(username_standard)
    login_page.enter_password(password)
    login_page.click_login()
    products_page = ProductsPage(navigate_to_url)
    products_page.click_add_to_cart()
    products_page.click_on_cart()
    cart_page = CartPage(navigate_to_url)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(navigate_to_url)
    checkout_page.fill_first_name(first_name)
    checkout_page.fill_last_name(last_name)
    checkout_page.fill_zip_code(zip_code)
    checkout_page.click_cancel()
    assert checkout_page.checkout_on_the_page()
