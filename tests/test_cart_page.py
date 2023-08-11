from pages.products_page import ProductsPage

from pages.cart_page import CartPage


def test_remove_from_cart(logged_in_standard_user):
    products_page = ProductsPage(logged_in_standard_user.driver)
    products_page.click_add_to_cart()
    products_page.click_on_cart()
    cart_page = CartPage(logged_in_standard_user.driver)
    cart_page.remove_from_cart()
    assert not products_page.is_cart_updated()


def test_continue_shopping(logged_in_standard_user):
    products_page = ProductsPage(logged_in_standard_user.driver)
    products_page.click_add_to_cart()
    products_page.click_on_cart()
    cart_page = CartPage(logged_in_standard_user.driver)
    cart_page.click_continue_shopping()
    assert cart_page.is_product_page_displayed()


def test_checkout(logged_in_standard_user):
    products_page = ProductsPage(logged_in_standard_user.driver)
    products_page.click_add_to_cart()
    products_page.click_on_cart()
    cart_page = CartPage(logged_in_standard_user.driver)
    cart_page.click_checkout()
    assert cart_page.is_product_page_displayed()
