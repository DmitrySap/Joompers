from pages.base_page import BasePage
from config.locators import ProfileLocators


class ProfilePage(BasePage):
    def become_creator(self):
        become_creator = self.browser.find_element(*ProfileLocators.BECOME_CREATOR)
        become_creator.click()

    def go_to_edit_profile(self):
        edit_profile = self.browser.find_element(*ProfileLocators.EDIT_PROFILE)
        edit_profile.click()

    def edit_name(self, names):
        name = self.browser.find_element(*ProfileLocators.NAME_EDIT)
        name.clear()
        name.send_keys(names)

    def edit_nickname(self, nicknames):
        nickname = self.browser.find_element(*ProfileLocators.NICKNAME_EDIT)
        nickname.clear()
        nickname.send_keys(nicknames)

    def edit_profession(self):
        info_dropdown = self.browser.find_element(*ProfileLocators.INFO_DROPDOWN)
        info_dropdown.click()
        info_books = self.browser.find_element(*ProfileLocators.INFO_BOOKS)
        info_books.click()

    def edit_bio(self, bios):
        bio = self.browser.find_element(*ProfileLocators.BIO_EDIT)
        bio.clear()
        bio.send_keys(bios)

    def save_changes(self):
        save_btn = self.browser.find_element(*ProfileLocators.SAVE_BTN)
        save_btn.click()

    def go_back(self):
        go_back = self.browser.find_element(*ProfileLocators.BACK_BTN)
        go_back.click()

    # def go_to_followings(self):
    #     followings = self.browser.find_element(*ProfileLocators.FOLLOWINGS)
    #     followings.click()
    #
    # def go_to_avatar(self):
    #     avatar = self.browser.find_element(*ProfileLocators.AVATAR)
    #     avatar.click()

    def name(self):
        name = self.browser.find_element(*ProfileLocators.NAME)
        return name

    def nickname(self):
        nickname = self.browser.find_element(*ProfileLocators.NICKNAME)
        return nickname

    def bio(self):
        bio = self.browser.find_element(*ProfileLocators.BIO)
        return bio

    def profession(self):
        profession = self.browser.find_element(*ProfileLocators.PROFESSION)
        return profession

    # def copy_profile_link(self):
    #     dropdown = self.browser.find_element(*ProfileLocators.INFO_DROPDOWN)
    #     dropdown.click()
    #     link = self.browser.find_element(*ProfileLocators.COPY_LINK)
    #     link.click()
