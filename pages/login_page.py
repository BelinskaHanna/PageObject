from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_STANDARD = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
    ERROR_MESSAGE = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3/text()')
    USERNAME_PERFORMANCE = (By.XPATH, '//*[@id="user-name"]')

    def enter_username_standard(self, username_standard):
        username_field = self.find(self.USERNAME_STANDARD)
        username_field.clear()
        username_field.send_keys(username_standard)

    def enter_username_performance(self, username_performance):
        username_field = self.find(self.USERNAME_PERFORMANCE)
        username_field.clear()
        username_field.send_keys(username_performance)

    def enter_password(self, password):
        password_field = self.find(self.PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.find(self.LOGIN_BUTTON).click()

    def is_visible(self):
        self.find(self.LOGIN_BUTTON).is_visible()

    def is_error_message_displayed(self):
        try:
            error_message = self.find(self.ERROR_MESSAGE)
            return error_message.is_displayed()
        except NoSuchElementException:
            return False
