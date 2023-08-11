import pytest

from pages.checkout_page import CheckoutPage

from pages.products_page import ProductsPage

from pages.cart_page import CartPage


def test_valid_checkout_data(logged_in_standard_user, first_name, last_name, zip_code):
    products_page = ProductsPage(logged_in_standard_user.driver)
    products_page.click_add_to_cart()
    products_page.click_on_cart()
    cart_page = CartPage(logged_in_standard_user.driver)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(logged_in_standard_user.driver)
    checkout_page.fill_first_name(first_name)
    checkout_page.fill_last_name(last_name)
    checkout_page.fill_zip_code(zip_code)
    checkout_page.click_continue()
    assert checkout_page.is_finish_is_on_the_page()


@pytest.mark.parametrize("first_name", [""])
def test_empty_first_name(logged_in_standard_user, first_name, last_name, zip_code):
    products_page = ProductsPage(logged_in_standard_user.driver)
    products_page.click_add_to_cart()
    products_page.click_on_cart()
    cart_page = CartPage(logged_in_standard_user.driver)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(logged_in_standard_user.driver)
    checkout_page.fill_first_name(first_name)
    checkout_page.fill_last_name(last_name)
    checkout_page.fill_zip_code(zip_code)
    checkout_page.click_continue()
    if first_name == "":
        assert checkout_page.is_error_message_displayed()
    else:
        assert checkout_page.is_finish_is_on_the_page()


def test_cancel_shopping(logged_in_standard_user, first_name, last_name, zip_code):
    products_page = ProductsPage(logged_in_standard_user.driver)
    products_page.click_add_to_cart()
    products_page.click_on_cart()
    cart_page = CartPage(logged_in_standard_user.driver)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(logged_in_standard_user.driver)
    checkout_page.fill_first_name(first_name)
    checkout_page.fill_last_name(last_name)
    checkout_page.fill_zip_code(zip_code)
    checkout_page.click_cancel()
    assert checkout_page.is_checkout_on_the_page()
