from pages.base_page import BasePage
from config.locators import SettingsLocators


class SettingsPage(BasePage):
    def male_gender(self):
        male = self.browser.find_element(*SettingsLocators.MALE)
        male.click()

    def female_gender(self):
        female = self.browser.find_element(*SettingsLocators.FEMALE)
        female.click()

    def other_gender(self):
        other_gender = self.browser.find_element(*SettingsLocators.OTHER)
        other_gender.click()

    def choose_country(self):
        choose_country = self.browser.find_element(*SettingsLocators.COUNTRY)
        choose_country.click()
        canada = self.browser.find_element(*SettingsLocators.COUNTRY_CANADA)
        canada.click()

    def save_settings(self):
        save_settings = self.browser.find_element(*SettingsLocators.SAVE_SETTINGS)
        save_settings.click()