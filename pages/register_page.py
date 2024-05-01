from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
import random

class RegisterPage(BasePage):
    HOME_PAGE_URL = "https://carturesti.ro/?lang=en-US"
    ACCEPT_COOKIES_BTN = (By.CSS_SELECTOR, "a[aria-label='allow cookies'].cc-btn.cc-allow")
    LANGUANGE_BTN = (By.ID, 'carturestiLanguageDropdown')
    RO_ENG = (By.XPATH, "//*[@aria-labelledby='carturestiLanguageDropdown']//a[@class='dropdown-item']")
    REGISTER_LOGIN_BTN = (By.XPATH, '(//button[@type="button" and @data-target="#modalLogin"])[2]')
    NEW_USER_BTN = (By.XPATH, '//*[@id="signupTrigger"]')
    REG_EMAIL_INPUT = (By.XPATH, '//*[@id="signupform-email"]')
    REG_PWD_INPUT = (By.XPATH, '//*[@id="signupform-password"]')
    NOT_ROBOT_CHECKBOX = (By.XPATH, '//*[@id="signupform-recaptcha-recaptcha-modalSignupForm"]/div/div/iframe')
    SINGUP_BTN = (By.XPATH, '//*[@id="modalSignupForm"]/div/button')
    REGISTER_BOX = (By.XPATH, "//*[@class='fade modal in']")
    REG_EMAIL_MESSAGE_ERROR = (By.CSS_SELECTOR, '.field-signupform-email .help-block')
    REG_PWD_MESSAGE_ERROR = (By.CSS_SELECTOR, '.field-signupform-password .help-block')
    REG_CAPTCHA_MESSAGE_ERROR = (By.CSS_SELECTOR, '.field-signupform-recaptcha .help-block')
    HELLO_BTN = (By.XPATH, "//span[@class='ng-scope' and normalize-space()='Hello']")
    LOGOUT = (By.CSS_SELECTOR, "li:has(> a[href='/site/logout'][data-method='post'])")


    def navigate_to_home_page_log_out(self):
        self.driver.get(self.HOME_PAGE_URL)
        self.driver.maximize_window()
        self.click_if_present_by_selector(*self.ACCEPT_COOKIES_BTN)
        if 'ROMÂNĂ' in self.get_text(self.LANGUANGE_BTN):
            self.click(self.LANGUANGE_BTN)
            self.click_if_contains_text(self.RO_ENG, 'ENGLISH')
        if self.is_element_not_displayed(self.REGISTER_LOGIN_BTN):
            self.click(self.HELLO_BTN)
            self.click(self.LOGOUT)

    """Register1"""
    def open_reg_box(self):
        self.click(self.REGISTER_LOGIN_BTN)

    def new_user(self):
        self.click(self.NEW_USER_BTN)

    # def set_random_email(self): It is used to create a unique email by generating a random number
    # (between 100 and 999) in the email address.
    def set_random_email(self):
        random_number = random.randint(100, 999)
        andress_email = f'test_compari{random_number}@itfactory.ro'
        self.type(self.REG_EMAIL_INPUT, andress_email)

    def set_password(self, text):
        self.type(self.REG_PWD_INPUT, text)

    def click_not_robot_checkbox(self):
        self.click(self.NOT_ROBOT_CHECKBOX)

    def click_singup_button(self):
        self.click(self.SINGUP_BTN)
        sleep(2)

    def check_email_pwd_error_not_displayed(self):
        reg_email_err_msg = (By.CSS_SELECTOR, '.field-signupform-email.md-input-invalid')
        reg_pwd_err_msg = (By.CSS_SELECTOR, '.field-signupform-password.md-input-invalid')
        assert (self.is_element_not_displayed(reg_email_err_msg))
        assert (self.is_element_not_displayed(reg_pwd_err_msg))

    """Register2"""
    # first two steps are the same
    def invalid_email(self, text):
        self.type(self.REG_EMAIL_INPUT, text)

    # next two steps are the same

    def reg_email_error_message_is_displayed(self):
        assert self.is_element_displayed(self.REG_EMAIL_MESSAGE_ERROR)

    def reg_email_error_message_is_correct(self, text):
        assert text in self.get_text(self.REG_EMAIL_MESSAGE_ERROR)

    """Register3"""
    # first three steps are the same
    def invalid_password(self, text):
        self.type(self.REG_PWD_INPUT, text)

    # next step is the same

    def reg_pwd_error_message_is_displayed(self):
        assert self.is_element_displayed(self.REG_PWD_MESSAGE_ERROR)

    def reg_pwd_error_message_is_correct(self, text):
        assert text in self.get_text(self.REG_PWD_MESSAGE_ERROR)


    """Register4"""
    # first five steps are the same
    def reg_cpt_error_message_is_displayed(self):
        assert self.is_element_displayed(self.REG_CAPTCHA_MESSAGE_ERROR)

    def reg_cpt_error_message_is_correct(self, text):
        assert text in self.get_text(self.REG_CAPTCHA_MESSAGE_ERROR)
