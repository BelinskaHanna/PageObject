from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    FIRST_ITEM_DESCRIPTION = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[1]')
    SECOND_ITEM_DESCRIPTION = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[1]')
    THIRD_ITEM_DESCRIPTION = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[5]/div[2]/div[1]')
    FOURTH_ITEM_DESCRIPTION = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[6]/div[2]/div[1]')
    FIFTH_ITEM_DESCRIPTION = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[7]/div[2]/div[1]')
    SIXTH_ITEM_DESCRIPTION = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[8]/div[2]/div[1]')
    CONTINUE_SHOPPING = (By.XPATH, '//*[@id="continue-shopping"]')
    CHECKOUT = (By.XPATH, '//*[@id="checkout"]')
    REMOVE_FROM = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    ON_PRODUCT_PAGE = (By.XPATH, '//*[@id="header_container"]/div[2]/span')

    def verify_first_item_description_match(self, expected_description):
        assert self.find(self.FIRST_ITEM_DESCRIPTION).text == expected_description

    def verify_second_item_description_match(self, expected_description):
        assert self.find(self.SECOND_ITEM_DESCRIPTION).text == expected_description

    def verify_third_item_description_match(self, expected_description):
        assert self.find(self.THIRD_ITEM_DESCRIPTION).text == expected_description

    def verify_fourth_item_description_match(self, expected_description):
        assert self.find(self.FOURTH_ITEM_DESCRIPTION).text == expected_description

    def verify_fifth_item_description_match(self, expected_description):
        assert self.find(self.FIFTH_ITEM_DESCRIPTION).text == expected_description

    def verify_sixth_item_description_match(self, expected_description):
        assert self.find(self.SIXTH_ITEM_DESCRIPTION).text == expected_description

    def click_continue_shopping(self):
        self.find(self.CONTINUE_SHOPPING).click()

    def click_checkout(self):
        self.find(self.CHECKOUT).click()

    def remove_from_cart(self):
        self.find(self.REMOVE_FROM).click()

    def product_page_after_cart(self):
        return self.find(self.ON_PRODUCT_PAGE).is_displayed()
