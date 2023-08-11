from pages.checkout_page import CheckoutPage

from pages.overview_page import OverviewPage

from pages.products_page import ProductsPage

from pages.cart_page import CartPage


def test_finish_button(logged_in_standard_user, first_name, last_name, zip_code):
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
    overview_page = OverviewPage(logged_in_standard_user.driver)
    overview_page.click_finish_button()
    assert overview_page.is_backhome_on_the_page()


def test_cancel_button(logged_in_standard_user, first_name, last_name, zip_code):
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
    overview_page = OverviewPage(logged_in_standard_user.driver)
    overview_page.click_cancel_button()
    assert overview_page.is_product_page_displayed_after_cancel()


def test_verify_first_item_description_match(logged_in_standard_user, first_name, last_name, zip_code):
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
    overview_page = OverviewPage(logged_in_standard_user.driver)
    expected_description = "Sauce Labs Backpack"
    overview_page.verify_first_item_description_match(expected_description)
