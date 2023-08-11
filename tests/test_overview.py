from pages.checkout_page import CheckoutPage

from pages.login_page import LoginPage

from pages.overview_page import OverviewPage

from pages.products_page import ProductsPage

from pages.cart_page import CartPage


def test_finish_button(navigate_to_url, username_standard, password, first_name, last_name, zip_code):
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
    overview_page = OverviewPage(navigate_to_url)
    overview_page.click_finish_button()
    assert overview_page.backhome_on_the_page()


def test_cancel_button(navigate_to_url, username_standard, password, first_name, last_name, zip_code):
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
    overview_page = OverviewPage(navigate_to_url)
    overview_page.click_cancel_button()
    assert overview_page.product_page_after_cancel()


def test_verify_first_item_description_match(navigate_to_url, username_standard, password, first_name, last_name, zip_code):
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
    overview_page = OverviewPage(navigate_to_url)
    expected_description = "Sauce Labs Backpack"
    overview_page.verify_first_item_description_match(expected_description)