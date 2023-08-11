from pages.products_page import ProductsPage


def test_add_to_cart(logged_in_standard_user):
    products_page = ProductsPage(logged_in_standard_user.driver)
    products_page.click_add_to_cart()
    assert products_page.is_cart_updated()


def test_remove(logged_in_standard_user):
    products_page = ProductsPage(logged_in_standard_user.driver)
    products_page.click_add_to_cart()
    products_page.remove()
    assert not products_page.is_cart_updated()


def test_select_tshirt_red(logged_in_standard_user):
    products_page = ProductsPage(logged_in_standard_user.driver)
    products_page.select_tshirt_red()
    assert products_page.is_on_product_page()
