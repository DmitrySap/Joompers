from pages.base_page import BasePage
from config.locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_email(self, email):
        register_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        register_email.send_keys(email)

    def go_to_password(self, password):
        register_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        register_password.send_keys(password)

    def go_to_button(self):
        register_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        register_button.click()
