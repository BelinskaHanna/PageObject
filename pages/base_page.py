from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    LOGIN = (By.LINK_TEXT, "Login")

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, 5)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def click_login(self):
        self.find(self.LOGIN).click()

    def is_login_visible(self):
        return self.find(self.LOGIN).is_displayed()
