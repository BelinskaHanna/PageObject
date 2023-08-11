from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CompletePage(BasePage):
    BACK_HOME = (By.XPATH, '//*[@id="back-to-products"]')
    PRODUCTS_AFTER_BACKHOME = (By.XPATH, '//*[@id="header_container"]/div[2]/span')

    def click_back_home_button(self):
        self.find(self.BACK_HOME).click()

    def products_after_backhome(self):
        return self.find(self.PRODUCTS_AFTER_BACKHOME).is_displayed()
