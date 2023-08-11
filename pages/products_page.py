from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC


class ProductsPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    REMOVE = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    BACKPACK = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    BIKE_LIGHT = (By.XPATH, '//*[@id="item_0_title_link"]/div')
    TSHIRT = (By.XPATH, '//*[@id="item_1_title_link"]/div')
    JACKET = (By.XPATH, '//*[@id="item_5_title_link"]/div')
    SAUCE = (By.XPATH, '//*[@id="item_2_title_link"]/div')
    TSHIRT_RED = (By.XPATH, '//*[@id="item_3_title_link"]/div')
    LOGOUT_VISIBLE = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
    LOGOUT = (By.XPATH, '//*[@id="logout_sidebar_link"]')
    BURGER_WINDOW = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
    CART_UPDATE = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    ON_PRODUCT = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    CART = (By.XPATH, '//*[@id="shopping_cart_container"]/a')

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_to_cart(self):
        self.find(self.ADD_TO_CART_BUTTON).click()

    def remove(self):
        self.find(self.REMOVE).click()

    def select_backpack(self):
        self.find(self.BACKPACK).click()

    def select_bike_light(self):
        self.find(self.BIKE_LIGHT).click()

    def select_tshirt(self):
        self.find(self.TSHIRT).click()

    def select_jacket(self):
        self.find(self.JACKET).click()

    def select_sauce(self):
        self.find(self.SAUCE).click()

    def select_tshirt_red(self):
        self.find(self.TSHIRT_RED).click()

    def logout_visible(self):
        self.find(self.LOGOUT_VISIBLE).is_displayed()

    def logout(self):
        self.find(self.LOGOUT).click()

    def burger_window_click(self):
        self.find(self.BURGER_WINDOW).click()

    def is_cart_updated(self):
        try:
            cart_update_element = self.driver.find_element(*self.CART_UPDATE)
            return cart_update_element.is_displayed()
        except NoSuchElementException:
            return False

    def is_on_product_page(self):
        return self.find(self.ON_PRODUCT).is_displayed()

    def click_on_cart(self):
        return self.find(self.CART).click()

    def wait_for_logout_button(self):
        wait = WebDriverWait(self.driver, 10)
        logout_button = wait.until(EC.element_to_be_clickable(ProductsPage.LOGOUT))
        return logout_button
