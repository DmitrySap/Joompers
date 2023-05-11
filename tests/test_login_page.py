import pytest
import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config.config import LoginPageData, MainLink, InvalidLoginData
from config.locators import LoginPageLocators


@pytest.mark.valid_login
def test_login_with_valid_email(browser):
    link = MainLink.link
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, link)
    page.go_to_email(LoginPageData.valid_email)
    page.go_to_password(LoginPageData.valid_password)
    page.go_to_button()
    time.sleep(1)
    current_url = browser.current_url
    assert current_url == 'https://www.joompers.com/news-feed-page'


@pytest.mark.invalid_login
class TestInvalidLogin:
    """Login with invalid emails"""
    @pytest.mark.parametrize("email", InvalidLoginData.invalid_emails)
    def test_login_with_invalid_email(self, browser, email):
        link = MainLink.link
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, link)
        page.go_to_email(email)
        page.go_to_password(LoginPageData.valid_password)
        page.go_to_button()
        current_url = browser.current_url
        assert current_url == 'https://www.joompers.com/auth'

    """Login with invalid passwords"""
    @pytest.mark.parametrize("password", InvalidLoginData.invalid_passwords)
    def test_login_with_invalid_password(self, browser, password):
        link = MainLink.link
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, link)
        page.go_to_email(LoginPageData.valid_email)
        page.go_to_password(password)
        page.go_to_button()
        current_url = browser.current_url
        assert current_url == 'https://www.joompers.com/auth'

    """Login without filling"""
    def test_login_without_filling(self, browser):
        link = MainLink.link
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, link)
        page.go_to_button()
        button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        assert button.get_attribute("disabled")
        current_url = browser.current_url
        assert current_url == 'https://www.joompers.com/auth'
