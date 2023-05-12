import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config.config import RegisterPageData, MainLink, InvalidRegisterData
from config.locators import LoginPageLocators


@pytest.mark.valid_signup
def test_valid_signup(browser):
    link = MainLink.link
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_register_page()
    login_page = LoginPage(browser, link)
    login_page.go_to_email(RegisterPageData.valid_email)
    login_page.go_to_password(RegisterPageData.valid_password)
    login_page.go_to_button()
    current_url = browser.current_url
    assert current_url == 'https://www.joompers.com/news-feed-page'


@pytest.mark.invalid_signup
class TestInvalidSignup:
    """Signup without filling"""
    def test_signup_without_filling(self, browser):
        link = MainLink.link
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_register_page()
        login_page = LoginPage(browser, link)
        login_page.go_to_button()
        button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        assert button.get_attribute("disabled")
        email_error = browser.find_element(*LoginPageLocators.SIGNUP_EMAIL_ERROR)
        assert email_error.text == 'No email provided.'
        password_error = browser.find_element(*LoginPageLocators.SIGNUP_PASSWORD_ERROR)
        assert password_error.text == 'No password provided.'
        login_page.go_to_email(RegisterPageData.valid_email)
        login_page.go_to_button()
        button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        assert button.get_attribute("disabled")
        assert password_error.text == 'No password provided.'

    """Signup with invalid emails"""
    @pytest.mark.parametrize("email", InvalidRegisterData.invalid_emails_1)
    def test_signup_with_invalid_emails_1(self, browser, email):
        link = MainLink.link
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_register_page()
        login_page = LoginPage(browser, link)
        login_page.go_to_email(email)
        login_page.go_to_password(RegisterPageData.valid_password)
        button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        assert button.get_attribute("disabled")
        email_error = browser.find_element(*LoginPageLocators.SIGNUP_EMAIL_ERROR)
        assert email_error.text == 'Email must be a valid email' or 'No email provided.'

    """Signup with invalid emails, where local or domain > MAX value"""
    @pytest.mark.parametrize("email", InvalidRegisterData.invalid_emails_2)
    def test_signup_with_invalid_emails_2(self, browser, email):
        link = MainLink.link
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_register_page()
        login_page = LoginPage(browser, link)
        login_page.go_to_email(email)
        login_page.go_to_password(RegisterPageData.valid_password)
        login_page.go_to_button()
        request_failed = browser.find_element(*LoginPageLocators.REQUEST_FAILED)
        assert request_failed.text == 'Request failed with status code 422'

    """Signup with invalid passwords"""
    @pytest.mark.parametrize("password", InvalidRegisterData.invalid_passwords)
    def test_signup_with_invalid_passwords(self, browser, password):
        link = MainLink.link
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_register_page()
        login_page = LoginPage(browser, link)
        login_page.go_to_email(RegisterPageData.valid_email)
        login_page.go_to_password(password)
        button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        assert button.get_attribute("disabled")
