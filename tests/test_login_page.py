import pytest
import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config.config import LoginPageData, MainLink, InvalidLoginData
from config.locators import LoginPageLocators, MainPageLocators


# @allure.title
@allure.feature('user_login')
@allure.story('Entering valid email and password')
@allure.severity('blocker')
@pytest.mark.valid_login
def test_login_with_valid_email(browser):
    link = MainLink.link
    main_page = MainPage(browser, link)
    main_page.open()
    with allure.step('Go to login page'):
        main_page.go_to_login_page()
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot of login page",
                      attachment_type=allure.attachment_type.PNG)
    login_page = LoginPage(browser, link)
    with allure.step('Enter email'):
        login_page.go_to_email(LoginPageData.valid_email)
    with allure.step('Enter password'):
        login_page.go_to_password(LoginPageData.valid_password)
    with allure.step('Click login button'):
        login_page.go_to_button()
    with allure.step('Check URL'):
        wait = WebDriverWait(browser, 10)
        wait.until(ec.visibility_of_element_located(MainPageLocators.DROPDOWN))
        current_url = browser.current_url
        assert current_url == 'https://www.joompers.com/news-feed-page'
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot of current page",
                      attachment_type=allure.attachment_type.PNG)


@allure.feature('user_login')
@allure.severity('critical')
@pytest.mark.invalid_login
class TestInvalidLogin:
    """Login with invalid emails"""
    @allure.story('Entering invalid emails')
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
        with allure.step('User Not Found Error'):
            user_not_found = browser.find_element(*LoginPageLocators.USER_NOT_FOUND_ERROR)
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot of 'User Not Found Error'",
                          attachment_type=allure.attachment_type.PNG)
            assert user_not_found.text == 'User was not found'

    """Login with invalid passwords"""
    @allure.story('Entering invalid passwords')
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
        with allure.step('Incorrect Password Error'):
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot of 'Incorrect Password Error'",
                          attachment_type=allure.attachment_type.PNG)
            password_error = browser.find_element(*LoginPageLocators.USER_NOT_FOUND_ERROR)
            assert password_error.text == 'Incorrect password' or 'Password is too short: 8 chars minimum.'

    """Login without filling"""
    @allure.story('Entering without filling')
    def test_login_without_filling(self, browser):
        link = MainLink.link
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.go_to_button()
        button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        with allure.step('Authorization Error'):
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot of 'Authorization Error'",
                          attachment_type=allure.attachment_type.PNG)
            assert button.get_attribute("disabled")
            email_error = browser.find_element(*LoginPageLocators.LOGIN_EMAIL_ERROR)
            assert email_error.text == 'No email provided.'
            password_error = browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_ERROR)
            assert password_error.text == 'No password provided.'
        login_page.go_to_email(LoginPageData.valid_email)
        login_page.go_to_button()
        with allure.step('No Password Provided Error'):
            button = browser.find_element(*LoginPageLocators.SUBMIT_BTN)
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot of 'No Password Provided Error'",
                          attachment_type=allure.attachment_type.PNG)
            assert button.get_attribute("disabled")
            assert password_error.text == 'No password provided.'
