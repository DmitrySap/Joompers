import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config.config import RegisterPageData, MainLink, InvalidRegisterData
from config.locators import LoginPageLocators


@pytest.mark.valid_signup
def test_valid_signup(browser):
    link = MainLink.link
    page = MainPage(browser, link)
    page.open()
    page.go_to_register_page()
    page = LoginPage(browser, link)
    page.go_to_email(RegisterPageData.valid_email)
    page.go_to_password(RegisterPageData.valid_password)
    page.go_to_button()
    current_url = browser.current_url
    assert current_url == 'https://www.joompers.com/news-feed-page'


@pytest.mark.invalid_signup
class TestInvalidSignup:
    """Signup without filling"""
    def test_signup_without_filling(self, browser):
        link = MainLink.link
        page = MainPage(browser, link)
        page.open()
        page.go_to_register_page()
        page = LoginPage(browser, link)
        page.go_to_button()
        button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        assert button.get_attribute("disabled")
        current_url = browser.current_url
        assert current_url == 'https://www.joompers.com/register'

    """Signup with invalid emails"""
    @pytest.mark.parametrize("email", InvalidRegisterData.invalid_emails_1)
    def test_signup_with_invalid_emails_1(self, browser, email):
        link = MainLink.link
        page = MainPage(browser, link)
        page.open()
        page.go_to_register_page()
        page = LoginPage(browser, link)
        page.go_to_email(email)
        page.go_to_password(RegisterPageData.valid_password)
        button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        assert button.get_attribute("disabled")

    """Signup with invalid emails, where local or domain > MAX value"""
    @pytest.mark.parametrize("email", InvalidRegisterData.invalid_emails_2)
    def test_signup_with_invalid_emails_2(self, browser, email):
        link = MainLink.link
        page = MainPage(browser, link)
        page.open()
        page.go_to_register_page()
        page = LoginPage(browser, link)
        page.go_to_email(email)
        page.go_to_password(RegisterPageData.valid_password)
        page.go_to_button()
        current_url = browser.current_url
        assert current_url == 'https://www.joompers.com/register'

    """Signup with invalid passwords"""
    @pytest.mark.parametrize("password", InvalidRegisterData.invalid_passwords)
    def test_signup_with_invalid_passwords(self, browser, password):
        link = MainLink.link
        page = MainPage(browser, link)
        page.open()
        page.go_to_register_page()
        page = LoginPage(browser, link)
        page.go_to_email(RegisterPageData.valid_email)
        page.go_to_password(password)
        button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        assert button.get_attribute("disabled")
