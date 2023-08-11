from selenium.webdriver.common.by import By

from tests.conftest import first_name, last_name, zip_code

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.XPATH, '//*[@id="first-name"]')
    LAST_NAME = (By.XPATH, '//*[@id="last-name"]')
    ZIP_CODE = (By.XPATH, '//*[@id="postal-code"]')
    CANCEL = (By.XPATH, '//*[@id="cancel"]')
    CONTINUE = (By.XPATH, '//*[@id="continue"]')
    FINISH = (By.XPATH, '//*[@id="finish"]')
    ERROR = (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3')
    CHECKOUT = (By.XPATH, '//*[@id="checkout"]')

    def fill_first_name(self, first_name):
        username_field = self.find(self.FIRST_NAME)
        username_field.clear()
        username_field.send_keys(first_name)

    def fill_last_name(self, last_name):
        username_field = self.find(self.LAST_NAME)
        username_field.clear()
        username_field.send_keys(last_name)

    def fill_zip_code(self, zip_code):
        username_field = self.find(self.ZIP_CODE)
        username_field.clear()
        username_field.send_keys(zip_code)

    def click_cancel(self):
        self.find(self.CANCEL).click()

    def click_continue(self):
        self.find(self.CONTINUE).click()

    def finish_is_on_the_page(self):
        return self.find(self.FINISH).is_displayed()

    def is_error_message_displayed(self):
        return self.find(self.ERROR).is_displayed()

    def checkout_on_the_page(self):
        return self.find(self.CHECKOUT).is_displayed()
