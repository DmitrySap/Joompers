import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config.config import LoginPageData, MainLink


@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def go_to_login(browser):
    link = MainLink.link
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.go_to_email(LoginPageData.valid_email)
    login_page.go_to_password(LoginPageData.valid_password)
    login_page.go_to_button()
