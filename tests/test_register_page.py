import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config.config import RegisterPageData, MainLink, InvalidRegisterData
from config.locators import LoginPageLocators, MainPageLocators


@allure.feature('user_register')
@allure.story('Entering valid email and password')
@allure.severity('blocker')
@pytest.mark.valid_signup
def test_valid_signup(browser):
    link = MainLink.link
    main_page = MainPage(browser, link)
    main_page.open()
    with allure.step('Go to register page'):
        main_page.go_to_register_page()
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot of register page",
                      attachment_type=allure.attachment_type.PNG)
    login_page = LoginPage(browser, link)
    with allure.step('Enter email'):
        login_page.go_to_email(RegisterPageData.valid_email)
    with allure.step('Enter password'):
        login_page.go_to_password(RegisterPageData.valid_password)
    with allure.step('Click login button'):
        login_page.go_to_button()
    with allure.step('Check URL'):
        wait = WebDriverWait(browser, 10)
        wait.until(ec.visibility_of_element_located(MainPageLocators.DROPDOWN))
        current_url = browser.current_url
        assert current_url == 'https://www.joompers.com/news-feed-page'
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot of current page",
                      attachment_type=allure.attachment_type.PNG)


@allure.feature('user_register')
@allure.severity('critical')
@pytest.mark.invalid_signup
class TestInvalidSignup:
    """Signup without filling"""
    @allure.story('SignUp without filling')
    def test_signup_without_filling(self, browser):
        link = MainLink.link
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_register_page()
        login_page = LoginPage(browser, link)
        login_page.go_to_button()
        button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        with allure.step('SignUp Error'):
            assert button.get_attribute("disabled")
            email_error = browser.find_element(*LoginPageLocators.SIGNUP_EMAIL_ERROR)
            assert email_error.text == 'No email provided.'
            password_error = browser.find_element(*LoginPageLocators.SIGNUP_PASSWORD_ERROR)
            assert password_error.text == 'No password provided.'
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot of 'SugnUp Error'",
                          attachment_type=allure.attachment_type.PNG)
        login_page.go_to_email(RegisterPageData.valid_email)
        login_page.go_to_button()
        with allure.step('No Password Provided Error'):
            button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
            assert button.get_attribute("disabled")
            assert password_error.text == 'No password provided.'
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot of 'No Password Provided Error'",
                          attachment_type=allure.attachment_type.PNG)

    """Signup with invalid emails"""
    @allure.story('SignUp with invalid email')
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
        with allure.step('Disabled submit button'):
            assert button.get_attribute("disabled")
        with allure.step('Email must be a valid email'):
            email_error = browser.find_element(*LoginPageLocators.SIGNUP_EMAIL_ERROR)
            assert email_error.text == 'Email must be a valid email' or 'No email provided.'

    """Signup with invalid emails, where local or domain > MAX value"""
    @allure.story('SignUp with invalid emails, where local or domain > MAX value')
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
        with allure.step('Request failed with status code 422'):
            request_failed = browser.find_element(*LoginPageLocators.REQUEST_FAILED)
            assert request_failed.text == 'Request failed with status code 422'

    """Signup with invalid passwords"""
    @allure.story('SignUp with invalid passwords')
    @pytest.mark.parametrize("password", InvalidRegisterData.invalid_passwords)
    def test_signup_with_invalid_passwords(self, browser, password):
        link = MainLink.link
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_register_page()
        login_page = LoginPage(browser, link)
        login_page.go_to_email(RegisterPageData.valid_email)
        login_page.go_to_password(password)
        with allure.step('Invalid password'):
            button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
            assert button.get_attribute("disabled")
