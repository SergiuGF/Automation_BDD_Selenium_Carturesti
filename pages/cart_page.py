from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import re
from time import sleep


class CartPage(BasePage):
    HOME_PAGE_URL = "https://carturesti.ro/?lang=en-US"
    ACCEPT_COOKIES_BTN = (By.CSS_SELECTOR, "a[aria-label='allow cookies'].cc-btn.cc-allow")
    LANGUAGE_BTN = (By.CSS_SELECTOR, '#carturestiLanguageDropdown > .ng-scope:first-child')
    RO_ENG = (By.XPATH, "//*[@aria-labelledby='carturestiLanguageDropdown']//a[@class='dropdown-item']")
    REGISTER_LOGIN_BTN = (By.XPATH, '(//button[@type="button" and @data-target="#modalLogin"])[2]')
    HELLO_BTN = (By.XPATH, "//span[@class='ng-scope' and normalize-space()='Hello']")
    EXISTING_USER_BTN = (By.ID, 'loginTrigger')
    LOG_EMAIL_INPUT = (By.ID, 'loginform-email')
    LOG_PWD_INPUT = (By.ID, 'loginform-password')
    LOGIN_BTN = (By.CSS_SELECTOR, '[name="login-button"]')
    SEARCH_BAR = (By.ID, 'search-input')
    ADD_TO_CART = (By.CSS_SELECTOR, '[title="Add to cart"]')
    ADD_TO_WISHLIST = (By.CLASS_NAME, 'addToWishList')
    CART_BTN = (By.CLASS_NAME, 'checkout__icon')
    WISHLIST = (By.XPATH, "//a[text()='Wishlists']")
    PRODUCT_INOVATIA = (By.XPATH, "//*[contains(@data-ng-bind, 'p.name') and contains(text(), 'Inovatia')]")
    WISHLIST_PRODUCT = ((By.XPATH, "//*[contains(@class, 'md-headline') and contains(text(), 'Neuroplasticitatea')]"))
    MENIU = (By.CLASS_NAME, 'coco')
    MUSIC_TAB = (By.XPATH, '//*[@id="mm-produse"]//*[contains(@class, "ng-scope") and contains(text(), "Music")]')


    def navigate_to_home_page_and_login(self):
        self.driver.get(self.HOME_PAGE_URL)
        self.driver.maximize_window()

        self.click_if_present_by_selector(*self.ACCEPT_COOKIES_BTN)
        sleep(2)
        if 'ROMÂNĂ' in self.get_text(self.LANGUAGE_BTN):
            self.click(self.LANGUAGE_BTN)
            self.click_if_contains_text(self.RO_ENG, 'ENGLISH')
        try:
            self.click(self.REGISTER_LOGIN_BTN)
            self.click(self.EXISTING_USER_BTN)
            self.type(self.LOG_EMAIL_INPUT, 'testingemail2352@gmail.com')
            self.type(self.LOG_PWD_INPUT, 'Passfortesting2352#')
            self.click(self.LOGIN_BTN)
            sleep(1)
        except:
            pass

    """Cart"""
    def search_product(self, text):
        self.search_and_enter(self.SEARCH_BAR, text)
        product_inovatia = ((By.XPATH, f"//*[contains(@class, 'md-title') and contains(text(), '{text}')]"))
        self.click(product_inovatia)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def click_cart_btn(self):
        self.click(self.CART_BTN)
        sleep(1)

    def cart_product_is_displayed(self):
        assert self.is_element_displayed(self.PRODUCT_INOVATIA)

    def cart_product_contains_text(self, text):
        assert text in self.get_text(self.PRODUCT_INOVATIA)


    """@Wishlist"""
    # first step is the same
    def click_add_to_wishlist(self):
        self.click(self.ADD_TO_WISHLIST)

    def click_wishlist_btn(self):
        self.click(self.HELLO_BTN)
        self.click(self.WISHLIST)

    def wish_product_is_displayed(self):
        assert self.is_element_displayed(self.WISHLIST_PRODUCT)

    def wish_product_contains_text(self, text):
        assert text in self.get_text(self.WISHLIST_PRODUCT)


    """@CartPrices"""
    def search_and_add_to_cart(self):
        self.click(self.MENIU)
        self.click(self.MUSIC_TAB)
        first_product = (By.XPATH, "//*[@id='coloana-produse']//*[contains(@class, 'cartu-grid-tile')][1]")
        second_product = (By.XPATH, "//*[@id='coloana-produse']//*[contains(@class, 'cartu-grid-tile')][3]")
        thirtd_product = (By.XPATH, "//*[@id='coloana-produse']//*[contains(@class, 'cartu-grid-tile')][4]")
        self.click(first_product)
        self.click(self.ADD_TO_CART)
        self.go_back()
        self.click(second_product)
        self.click(self.ADD_TO_CART)
        self.go_back()
        self.click(thirtd_product)
        self.click(self.ADD_TO_CART)

    # next step is the same

    def total_price_is_correct(self):
        total_price = (By.CSS_SELECTOR, "span[data-ng-bind='numberFormat(cart.total)'].ng-binding")
        sleep(1)
        total_price_text = self.get_text(total_price)
        total_price_text = total_price_text.replace(',', '')
        total_price_int = int(total_price_text)
        products_prices = (By.CSS_SELECTOR, "span[data-ng-bind='numberFormat(p.price)'].ng-binding")
        products_prices_text = [price.text for price in self.find_multiple(products_prices)]
        products_prices_list = [re.sub(r'[^\d,]', '', item) for item in products_prices_text if item.strip()]
        products_prices_list_int = [int(item.replace(',', '')) for item in products_prices_list]
        products_prices_sum = sum(products_prices_list_int)
        assert products_prices_sum == total_price_int
