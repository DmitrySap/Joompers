import pytest
import allure
from selenium.common import NoSuchElementException
from pages.profile_page import ProfilePage
from pages.settings_page import SettingsPage
from pages.main_page import MainPage
from config.config import EditProfile


@allure.feature('edit profile')
@allure.severity('critical')
@pytest.mark.edit_profile
class TestEditProfile:
    """Valid names"""
    @allure.story('change name to valid')
    @pytest.mark.parametrize("names", EditProfile.valid_names)
    @pytest.mark.edit_profile_valid_names
    def test_valid_names(self, browser, go_to_login, names):
        main_page = MainPage(browser, self)
        with allure.step('Go to my profile'):
            main_page.go_to_my_profile()
        profile_page = ProfilePage(browser, self)
        try:
            profile_page.become_creator()
            main_page.go_to_my_profile()
            with allure.step('Go to edit profile'):
                profile_page.go_to_edit_profile()
        except NoSuchElementException:
            with allure.step('Go to edit profile'):
                profile_page.go_to_edit_profile()
        with allure.step('Edit name'):
            profile_page.edit_name(names)
        with allure.step('Save changes'):
            profile_page.save_changes()
        main_page.go_to_my_profile()
        with allure.step('Changes'):
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot of 'Saved Changes'",
                          attachment_type=allure.attachment_type.PNG)
        try:
            with allure.step('Assert changes'):
                assert profile_page.name().text == names
        except AssertionError:
            with allure.step('Logout'):
                main_page.go_to_logout()
        finally:
            with allure.step('Logout'):
                main_page.go_to_logout()

    """Invalid names"""
    @allure.story('change name to invalid')
    @pytest.mark.parametrize("invalid_names", EditProfile.invalid_names)
    @pytest.mark.edit_profile_invalid_names
    def test_invalid_names(self, browser, go_to_login, invalid_names):
        main_page = MainPage(browser, self)
        with allure.step('Go to my profile'):
            main_page.go_to_my_profile()
        profile_page = ProfilePage(browser, self)
        try:
            profile_page.become_creator()
            main_page.go_to_my_profile()
            with allure.step('Go to edit profile'):
                profile_page.go_to_edit_profile()
        except NoSuchElementException:
            with allure.step('Go to edit profile'):
                profile_page.go_to_edit_profile()
        with allure.step('Edit name'):
            profile_page.edit_name(invalid_names)
        with allure.step('Save changes'):
            profile_page.save_changes()
        main_page.go_to_my_profile()
        with allure.step('Changes'):
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot of 'Saved Changes'",
                          attachment_type=allure.attachment_type.PNG)
        try:
            with allure.step('Assert changes'):
                assert profile_page.name().text != invalid_names
        except AssertionError:
            with allure.step('Logout'):
                main_page.go_to_logout()
        finally:
            with allure.step('Logout'):
                main_page.go_to_logout()

    """Valid nicknames"""
    @allure.story('change nickname to valid')
    @pytest.mark.parametrize("nicknames", EditProfile.valid_nicknames)
    @pytest.mark.edit_profile_valid_nicknames
    def test_valid_nicknames(self, browser, go_to_login, nicknames):
        main_page = MainPage(browser, self)
        with allure.step('Go to my profile'):
            main_page.go_to_my_profile()
        profile_page = ProfilePage(browser, self)
        try:
            profile_page.become_creator()
            main_page.go_to_my_profile()
            with allure.step('Go to edit profile'):
                profile_page.go_to_edit_profile()
        except NoSuchElementException:
            with allure.step('Go to edit profile'):
                profile_page.go_to_edit_profile()
        with allure.step('Edit nickname'):
            profile_page.edit_nickname(nicknames)
        with allure.step('Save changes'):
            profile_page.save_changes()
        main_page.go_to_my_profile()
        with allure.step('Changes'):
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot of 'Saved Changes'",
                          attachment_type=allure.attachment_type.PNG)
        try:
            with allure.step('Assert changes'):
                assert profile_page.nickname().text == nicknames
        except AssertionError:
            with allure.step('Logout'):
                main_page.go_to_logout()
        finally:
            with allure.step('Logout'):
                main_page.go_to_logout()

    """Invalid nicknames"""
    @allure.story('change nickname to invalid')
    @pytest.mark.parametrize("invalid_nicknames", EditProfile.invalid_nicknames)
    @pytest.mark.edit_profile_invalid_nicknames
    def test_invalid_nicknames(self, browser, go_to_login, invalid_nicknames):
        main_page = MainPage(browser, self)
        with allure.step('Go to my profile'):
            main_page.go_to_my_profile()
        profile_page = ProfilePage(browser, self)
        try:
            profile_page.become_creator()
            main_page.go_to_my_profile()
            with allure.step('Go to edit profile'):
                profile_page.go_to_edit_profile()
        except NoSuchElementException:
            with allure.step('Go to edit profile'):
                profile_page.go_to_edit_profile()
        with allure.step('Edit nickname'):
            profile_page.edit_nickname(invalid_nicknames)
        with allure.step('Save changes'):
            profile_page.save_changes()
        main_page.go_to_my_profile()
        with allure.step('Changes'):
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot of 'Saved Changes'",
                          attachment_type=allure.attachment_type.PNG)
        try:
            with allure.step('Assert changes'):
                assert profile_page.nickname().text != invalid_nicknames
        except AssertionError:
            with allure.step('Logout'):
                main_page.go_to_logout()
        finally:
            with allure.step('Logout'):
                main_page.go_to_logout()

    """Valid bios"""
    @allure.story('change bios to valid')
    @pytest.mark.parametrize("bios", EditProfile.valid_bio)
    @pytest.mark.edit_profile_valid_bios
    def test_valid_bios(self, browser, go_to_login, bios):
        main_page = MainPage(browser, self)
        with allure.step('Go to my profile'):
            main_page.go_to_my_profile()
        profile_page = ProfilePage(browser, self)
        try:
            profile_page.become_creator()
            main_page.go_to_my_profile()
            with allure.step('Go to edit profile'):
                profile_page.go_to_edit_profile()
        except NoSuchElementException:
            with allure.step('Go to edit profile'):
                profile_page.go_to_edit_profile()
        with allure.step('Edit bios'):
            profile_page.edit_bio(bios)
        with allure.step('Save changes'):
            profile_page.save_changes()
        main_page.go_to_my_profile()
        with allure.step('Changes'):
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot of 'Saved Changes'",
                          attachment_type=allure.attachment_type.PNG)
        try:
            with allure.step('Assert changes'):
                assert profile_page.bio().text == bios
        except AssertionError:
            with allure.step('Logout'):
                main_page.go_to_logout()
        finally:
            with allure.step('Logout'):
                main_page.go_to_logout()

    """Invalid bios"""
    @allure.story('change bios to invalid')
    @pytest.mark.parametrize("invalid_bios", EditProfile.invalid_bio)
    @pytest.mark.edit_profile_invalid_bios
    def test_invalid_bios(self, browser, go_to_login, invalid_bios):
        main_page = MainPage(browser, self)
        with allure.step('Go to my profile'):
            main_page.go_to_my_profile()
        profile_page = ProfilePage(browser, self)
        try:
            profile_page.become_creator()
            main_page.go_to_my_profile()
            with allure.step('Go to edit profile'):
                profile_page.go_to_edit_profile()
        except NoSuchElementException:
            with allure.step('Go to edit profile'):
                profile_page.go_to_edit_profile()
        with allure.step('Edit bios and proseffion'):
            profile_page.edit_profession()
            profile_page.edit_bio(invalid_bios)
        with allure.step('Save changes'):
            profile_page.save_changes()
        main_page.go_to_my_profile()
        with allure.step('Changes'):
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot of 'Saved Changes'",
                          attachment_type=allure.attachment_type.PNG)
        try:
            with allure.step('Assert changes'):
                assert profile_page.bio().text != invalid_bios
                assert profile_page.profession().text == 'Books'
        except AssertionError:
            with allure.step('Logout'):
                main_page.go_to_logout()
        finally:
            with allure.step('Logout'):
                main_page.go_to_logout()

    """Choose Canada, Aruba country, gender"""
    @allure.story('change country, gender')
    @pytest.mark.edit_profile_settings
    def test_edit_settings(self, browser, go_to_login):
        main_page = MainPage(browser, self)
        with allure.step('Go to settings'):
            main_page.go_to_settings()
        settings_page = SettingsPage(browser, self)
        with allure.step('Choose country and gender'):
            settings_page.choose_country_canada()
            settings_page.male_gender()
            settings_page.female_gender()
            settings_page.other_gender()
            settings_page.choose_country_aruba()
        with allure.step('Save settings'):
            settings_page.save_settings()
        with allure.step('Changes'):
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot of 'Saved Changes'",
                          attachment_type=allure.attachment_type.PNG)
