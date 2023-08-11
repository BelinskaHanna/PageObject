from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OverviewPage(BasePage):
    ITEM_DESCRIPTION = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    PRICE_TOTAL = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]')
    CANCEL = (By.XPATH, '//*[@id="cancel"]')
    FINISH = (By.XPATH, '//*[@id="finish"]')
    BACKHOME = (By.XPATH, '//*[@id="back-to-products"]')
    PRODUCT_PAGE = (By.XPATH, '//*[@id="header_container"]/div[2]/span')

    def verify_first_item_description_match(self, expected_description):
        assert self.find(self.ITEM_DESCRIPTION).text == expected_description

    def is_visible_price_total(self):
        return self.find(self.PRICE_TOTAL).is_visible()

    def click_cancel_button(self):
        return self.find(self.CANCEL).click()

    def click_finish_button(self):
        return self.find(self.FINISH).click()

    def is_backhome_on_the_page(self):
        return self.find(self.BACKHOME).is_displayed()

    def is_product_page_displayed_after_cancel(self):
        return self.find(self.PRODUCT_PAGE).is_displayed()
