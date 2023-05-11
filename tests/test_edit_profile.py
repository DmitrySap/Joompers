import pytest
import time
from selenium.common import NoSuchElementException
from pages.profile_page import ProfilePage
from pages.settings_page import SettingsPage
from pages.main_page import MainPage
from config.locators import ProfileLocators
from config.config import EditProfile


@pytest.mark.edit_profile
class TestEditProfile:
    """Valid names"""
    @pytest.mark.parametrize("names", EditProfile.valid_names)
    def test_valid_names(self, browser, go_to_login, names):
        main_page = MainPage(browser, self)
        main_page.go_to_my_profile()
        profile_page = ProfilePage(browser, self)
        try:
            profile_page.become_creator()
            main_page.go_to_my_profile()
            profile_page.go_to_edit_profile()
        except NoSuchElementException:
            profile_page.go_to_edit_profile()
        profile_page.edit_name(names)
        profile_page.edit_nickname(EditProfile.valid_nicknames[0])
        profile_page.edit_profession()
        profile_page.edit_bio(EditProfile.valid_bio[0])
        profile_page.save_changes()
        main_page.go_to_my_profile()
        try:
            assert profile_page.name().text == names
            assert profile_page.nickname().text == EditProfile.valid_nicknames[0]
            assert profile_page.bio().text == EditProfile.valid_bio[0]
            assert profile_page.profession().text == 'Books'
        except AssertionError:
            main_page.go_to_logout()
        finally:
            main_page.go_to_logout()

    """Invalid names"""
    @pytest.mark.parametrize("invalid_names", EditProfile.invalid_names)
    def test_invalid_names(self, browser, go_to_login, invalid_names):
        main_page = MainPage(browser, self)
        main_page.go_to_my_profile()
        profile_page = ProfilePage(browser, self)
        try:
            profile_page.become_creator()
            main_page.go_to_my_profile()
            profile_page.go_to_edit_profile()
        except NoSuchElementException:
            profile_page.go_to_edit_profile()
        profile_page.edit_name(invalid_names)
        profile_page.edit_nickname(EditProfile.valid_nicknames[0])
        profile_page.edit_profession()
        profile_page.edit_bio(EditProfile.valid_bio[0])
        profile_page.save_changes()
        main_page.go_to_my_profile()
        try:
            assert profile_page.name().text != invalid_names
            assert profile_page.nickname().text == EditProfile.valid_nicknames[0]
            assert profile_page.bio().text == EditProfile.valid_bio[0]
            assert profile_page.profession().text == 'Books'
        except AssertionError:
            main_page.go_to_logout()
        finally:
            main_page.go_to_logout()

    """Valid nicknames"""
    @pytest.mark.parametrize("nicknames", EditProfile.valid_nicknames)
    def test_valid_nicknames(self, browser, go_to_login, nicknames):
        main_page = MainPage(browser, self)
        main_page.go_to_my_profile()
        profile_page = ProfilePage(browser, self)
        try:
            profile_page.become_creator()
            main_page.go_to_my_profile()
            profile_page.go_to_edit_profile()
        except NoSuchElementException:
            profile_page.go_to_edit_profile()
        profile_page.edit_name(EditProfile.valid_names[0])
        profile_page.edit_nickname(nicknames)
        profile_page.edit_profession()
        profile_page.edit_bio(EditProfile.valid_bio[0])
        profile_page.save_changes()
        main_page.go_to_my_profile()
        try:
            assert profile_page.name().text == EditProfile.valid_names[0]
            assert profile_page.nickname().text == nicknames
            assert profile_page.bio().text == EditProfile.valid_bio[0]
            assert profile_page.profession().text == 'Books'
        except AssertionError:
            main_page.go_to_logout()
        finally:
            main_page.go_to_logout()

    """Invalid nicknames"""
    @pytest.mark.parametrize("invalid_nicknames", EditProfile.invalid_nicknames)
    def test_invalid_nicknames(self, browser, go_to_login, invalid_nicknames):
        main_page = MainPage(browser, self)
        main_page.go_to_my_profile()
        profile_page = ProfilePage(browser, self)
        try:
            profile_page.become_creator()
            main_page.go_to_my_profile()
            profile_page.go_to_edit_profile()
        except NoSuchElementException:
            profile_page.go_to_edit_profile()
        profile_page.edit_name(EditProfile.valid_names[0])
        profile_page.edit_nickname(invalid_nicknames)
        profile_page.edit_profession()
        profile_page.edit_bio(EditProfile.valid_bio[0])
        profile_page.save_changes()
        main_page.go_to_my_profile()
        try:
            assert profile_page.name().text == EditProfile.valid_names[0]
            assert profile_page.nickname().text != invalid_nicknames
            assert profile_page.bio().text == EditProfile.valid_bio[0]
            assert profile_page.profession().text == 'Books'
        except AssertionError:
            main_page.go_to_logout()
        finally:
            main_page.go_to_logout()

    """Valid bios"""
    @pytest.mark.parametrize("bios", EditProfile.valid_bio)
    def test_valid_bios(self, browser, go_to_login, bios):
        main_page = MainPage(browser, self)
        main_page.go_to_my_profile()
        profile_page = ProfilePage(browser, self)
        try:
            profile_page.become_creator()
            main_page.go_to_my_profile()
            profile_page.go_to_edit_profile()
        except NoSuchElementException:
            profile_page.go_to_edit_profile()
        profile_page.edit_name(EditProfile.valid_names[0])
        profile_page.edit_nickname(EditProfile.valid_nicknames[0])
        profile_page.edit_profession()
        profile_page.edit_bio(bios)
        profile_page.save_changes()
        main_page.go_to_my_profile()
        try:
            assert profile_page.name().text == EditProfile.valid_names[0]
            assert profile_page.nickname().text == EditProfile.valid_nicknames[0]
            assert profile_page.bio().text == bios
            assert profile_page.profession().text == 'Books'
        except AssertionError:
            main_page.go_to_logout()
        finally:
            main_page.go_to_logout()

    """Invalid bios"""
    @pytest.mark.parametrize("invalid_bios", EditProfile.invalid_bio)
    def test_invalid_bios(self, browser, go_to_login, invalid_bios):
        main_page = MainPage(browser, self)
        main_page.go_to_my_profile()
        profile_page = ProfilePage(browser, self)
        try:
            profile_page.become_creator()
            main_page.go_to_my_profile()
            profile_page.go_to_edit_profile()
        except NoSuchElementException:
            profile_page.go_to_edit_profile()
        profile_page.edit_name(EditProfile.valid_names[0])
        profile_page.edit_nickname(EditProfile.valid_nicknames[0])
        profile_page.edit_profession()
        profile_page.edit_bio(invalid_bios)
        profile_page.save_changes()
        main_page.go_to_my_profile()
        try:
            assert profile_page.name().text == EditProfile.valid_names[0]
            assert profile_page.nickname().text == EditProfile.valid_nicknames[0]
            assert profile_page.bio().text != invalid_bios
            assert profile_page.profession().text == 'Books'
        except AssertionError:
            main_page.go_to_logout()
        finally:
            main_page.go_to_logout()

    """Choose Canada country, male gender"""
    def test_edit_settings(self, browser, go_to_login):
        main_page = MainPage(browser, self)
        main_page.go_to_settings()
        settings_page = SettingsPage(browser, self)
        settings_page.choose_country()
        settings_page.male_gender()
        settings_page.save_settings()
