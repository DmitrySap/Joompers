import pytest
import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config.config import LoginPageData, MainLink, InvalidLoginData
from config.locators import LoginPageLocators


@pytest.mark.valid_login
def test_login_with_valid_email(browser):
    link = MainLink.link
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.go_to_email(LoginPageData.valid_email)
    login_page.go_to_password(LoginPageData.valid_password)
    login_page.go_to_button()
    time.sleep(1)
    current_url = browser.current_url
    assert current_url == 'https://www.joompers.com/news-feed-page'


@pytest.mark.invalid_login
class TestInvalidLogin:
    """Login with invalid emails"""
    @pytest.mark.parametrize("email", InvalidLoginData.invalid_emails)
    def test_login_with_invalid_email(self, browser, email):
        link = MainLink.link
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.go_to_email(email)
        login_page.go_to_password(LoginPageData.valid_password)
        login_page.go_to_button()
        user_not_found = browser.find_element(*LoginPageLocators.USER_NOT_FOUND_ERROR)
        assert user_not_found.text == 'User was not found'

    """Login with invalid passwords"""
    @pytest.mark.parametrize("password", InvalidLoginData.invalid_passwords)
    def test_login_with_invalid_password(self, browser, password):
        link = MainLink.link
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.go_to_email(LoginPageData.valid_email)
        login_page.go_to_password(password)
        login_page.go_to_button()
        password_error = browser.find_element(*LoginPageLocators.USER_NOT_FOUND_ERROR)
        assert password_error.text == 'Incorrect password' or 'Password is too short: 8 chars minimum.'

    """Login without filling"""
    def test_login_without_filling(self, browser):
        link = MainLink.link
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.go_to_button()
        button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        assert button.get_attribute("disabled")
        email_error = browser.find_element(*LoginPageLocators.LOGIN_EMAIL_ERROR)
        assert email_error.text == 'No email provided.'
        password_error = browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_ERROR)
        assert password_error.text == 'No password provided.'
        login_page.go_to_email(LoginPageData.valid_email)
        login_page.go_to_button()
        button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        assert button.get_attribute("disabled")
        assert password_error.text == 'No password provided.'
