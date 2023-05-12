from selenium.webdriver.common.by import By


class MainPageLocators:
    SIGN_UP_BTN = (By.CSS_SELECTOR, '.Navbar_signUpBtn__nudEF')
    LOG_IN_BTN = (By.CSS_SELECTOR, '.Navbar_login__cvMwa > span')
    SEARCH = (By.CSS_SELECTOR, '.Navbar_searchInput__LTmUb')
    LOGO = (By.CSS_SELECTOR, '.Navbar_logo__MK0b0')
    DROPDOWN = (By.CSS_SELECTOR, '.DropdownForNavMenu_avatar__H3RHe')
    MY_PROFILE = (By.CSS_SELECTOR, 'div:nth-child(1) > a')
    SETTINGS = (By.CSS_SELECTOR, 'div:nth-child(2) > a')
    LOGOUT = (By.CSS_SELECTOR, '.DropdownForNavMenu_logout__7RC-T')


class LoginPageLocators:
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    SUBMIT_BTN = (By.CSS_SELECTOR, '.CustomButton_btn_big__VBcwJ')
    STATUS = (By.CSS_SELECTOR, '.SignUpBlock_errorNetwork__mUmJj')
    SIGNUP_EMAIL_ERROR = (By.CSS_SELECTOR, 'p.SignUpBlock_errorValidation__R5R4a:nth-child(2)')
    LOGIN_EMAIL_ERROR = (By.CSS_SELECTOR, 'p.SignInBlock_errorValidation__pws18:nth-child(2)')
    SIGNUP_PASSWORD_ERROR = (By.CSS_SELECTOR, 'p.SignUpBlock_errorValidation__R5R4a:nth-child(4)')
    LOGIN_PASSWORD_ERROR = (By.CSS_SELECTOR, 'p.SignInBlock_errorValidation__pws18:nth-child(4)')
    USER_NOT_FOUND_ERROR = (By.CSS_SELECTOR, '.SignInBlock_errorNetwork__jXtg5')
    REQUEST_FAILED = (By.CSS_SELECTOR, '.SignUpBlock_errorNetwork__mUmJj')
    TERMS_OF_USE = ()
    PRIVACY_POLICY = ()
    REGISTER_WITH_GOOGLE = ()
    FORGOT_PASSWORD = ()
    LOGIN_WITH_GOOGLE = ()


class DeleteProfileLocators:
    DELETE = (By.CSS_SELECTOR, 'a:nth-child(2)')
    DELETE_CODE = (By.ID, 'code')
    DELETE_BTN = (By.NAME, 'delete')
    DELETE_SUBMIT = (By.CSS_SELECTOR, '.false:nth-child(2)')


class ProfileLocators:
    BECOME_CREATOR = (By.CSS_SELECTOR, '.CustomButton_btn_color_white__6zlHF')
    EDIT_PROFILE = (By.CSS_SELECTOR, '.false')
    NAME_EDIT = (By.XPATH, '/html/body/div/div/main/div[1]/form/div[1]/div[1]/input')
    NICKNAME_EDIT = (By.XPATH, '/html/body/div/div/main/div[1]/form/div[1]/div[2]/input')
    SAVE_BTN = (By.CSS_SELECTOR, '.ProfileCreatorEdit_save__Ec7zZ > button:nth-child(1)')
    INFO_DROPDOWN = (By.CSS_SELECTOR, '.css-8mmkcg')
    INFO_BOOKS = (By.ID, 'react-select-2-option-2')
    BIO_EDIT = (By.NAME, 'bio')
    BACK_BTN = (By.XPATH, '/html/body/div/div/main/div[1]/div/div[1]/button')
    NAME = (By.CSS_SELECTOR, '.MyProfileCreatorPage_name__d51fW')
    NICKNAME = (By.XPATH, '/html/body/div/div/main/div/div[2]/h4[1]')
    PROFESSION = (By.CSS_SELECTOR, '.MyProfileCreatorPage_profession__E7UY6')
    BIO = (By.CSS_SELECTOR, '.MyProfileCreatorPage_description__TidFe')
    # DROPDOWN = (By.CSS_SELECTOR, 'div.Dropdown_body__W9LmE:nth-child(1) > button:nth-child(1) > img:nth-child(1)')
    # COPY_LINK = (By.CSS_SELECTOR, '.CopyLink_text__wfJ6J')


class SettingsLocators:
    MALE = (By.NAME, 'Male')
    FEMALE = (By.NAME, 'Female')
    OTHER = (By.NAME, 'Other')
    COUNTRY = (By.CSS_SELECTOR, '.css-8mmkcg')
    COUNTRY_CANADA = (By.ID, 'react-select-3-option-39')
    COUNTRY_ARUBA = (By.ID, 'react-select-3-option-0')
    SAVE_BTN = (By.CSS_SELECTOR, '.ProfileSettingsPage_btnGroup__JPkH5 > button:nth-child(2)')
    SAVE_SETTINGS = (By.CSS_SELECTOR, '.ProfileSettingsPage_btnGroup__JPkH5 > .CustomButton_btn__tVfG5:nth-child(2)')
