from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class LoginPage(BasePage):
    HOME_PAGE_URL = "https://carturesti.ro/?lang=en-US"
    ACCEPT_COOKIES_BTN = (By.CSS_SELECTOR, "a[aria-label='allow cookies'].cc-btn.cc-allow")
    COOKIES_NOT_DISPLAYED = (By.CLASS_NAME, 'cc-invisible')
    LANGUANGE_BTN = (By.ID, 'carturestiLanguageDropdown')
    RO_ENG = (By.XPATH, "//*[@aria-labelledby='carturestiLanguageDropdown']//a[@class='dropdown-item']")
    REGISTER_LOGIN_BTN = (By.XPATH, '(//button[@type="button" and @data-target="#modalLogin"])[2]')
    EXISTING_USER_BTN = (By.ID, 'loginTrigger')
    LOG_EMAIL_INPUT = (By.ID, 'loginform-email')
    LOG_PWD_INPUT = (By.ID, 'loginform-password')
    LOGIN_BTN = (By.CSS_SELECTOR, '[name="login-button"]')
    LOGIN_BOX = (By.XPATH, "//*[@class='fade modal in']")
    LOG_EMAIL_MESSAGE_ERROR = (By.XPATH, '//*[contains(text(), "Email cannot be blank.")]')
    LOG_PWD_MESSAGE_ERROR = (By.XPATH, '//*[contains(text(), "Password cannot be blank.")]')
    SECOND_LOG_MESSAGE_ERROR = (By.XPATH, '//*[contains(text(), "Incorrect email or password.")][contains(@class, "help-block")]')
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

    """Login1"""
    def open_login_box(self):
        self.click(self.REGISTER_LOGIN_BTN)

    def click_existing_user(self):
        self.click(self.EXISTING_USER_BTN)

    def set_login_email(self, text):
        sleep(1)
        self.type(self.LOG_EMAIL_INPUT, text)

    def set_login_password(self, text):
        sleep(1)
        self.type(self.LOG_PWD_INPUT, text)

    def click_login_button(self):
        self.click(self.LOGIN_BTN)
        sleep(1)

    def login_box_not_displayed(self):
        assert (self.is_element_not_displayed(self.LOGIN_BOX))

    """Login2"""
    # first five steps are the same
    def log_error_message_is_displayed(self):
        log_email_input = self.driver.find_element(By.XPATH, '//*[@id="loginform-email"]')
        log_email_input_classes = self.get_attribute(log_email_input, 'class')
        if 'ng-not-empty' in log_email_input_classes:
            assert self.is_element_displayed(self.LOG_PWD_MESSAGE_ERROR)
        else:
            assert self.is_element_displayed(self.LOG_EMAIL_MESSAGE_ERROR)

    def log_error_message_is_correct(self, text):
        log_email_input = self.driver.find_element(By.XPATH, '//*[@id="loginform-email"]')
        log_email_input_classes = self.get_attribute(log_email_input, 'class')

        if 'ng-not-empty' in log_email_input_classes:
            assert text in self.get_text(self.LOG_PWD_MESSAGE_ERROR)
        else:
            assert text in self.get_text(self.LOG_EMAIL_MESSAGE_ERROR)

    """Login3"""
    # first five steps are the same
    def second_log_error_message_is_displayed(self):
        sleep(1)
        assert self.is_element_displayed(self.SECOND_LOG_MESSAGE_ERROR)

    def second_log_error_message_is_correct(self, text):
        assert text in self.get_text(self.SECOND_LOG_MESSAGE_ERROR)
