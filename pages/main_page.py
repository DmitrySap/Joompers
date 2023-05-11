from pages.base_page import BasePage
from config.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_button = self.browser.find_element(*MainPageLocators.LOG_IN_BTN)
        login_button.click()

    def go_to_register_page(self):
        register_button = self.browser.find_element(*MainPageLocators.SIGN_UP_BTN)
        register_button.click()

    def go_to_my_profile(self):
        profile_dropdown = self.browser.find_element(*MainPageLocators.DROPDOWN)
        profile_dropdown.click()
        my_profile = self.browser.find_element(*MainPageLocators.MY_PROFILE)
        my_profile.click()

    def go_to_settings(self):
        profile_dropdown = self.browser.find_element(*MainPageLocators.DROPDOWN)
        profile_dropdown.click()
        settings = self.browser.find_element(*MainPageLocators.SETTINGS)
        settings.click()

    def go_to_logout(self):
        profile_dropdown = self.browser.find_element(*MainPageLocators.DROPDOWN)
        profile_dropdown.click()
        logout = self.browser.find_element(*MainPageLocators.LOGOUT)
        logout.click()
