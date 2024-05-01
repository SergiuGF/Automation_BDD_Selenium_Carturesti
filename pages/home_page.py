from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import re
from time import sleep


class HomePage(BasePage):
    HOME_PAGE_URL = "https://carturesti.ro/?lang=en-US"
    ACCEPT_COOKIES_BTN = (By.CSS_SELECTOR, "a[aria-label='allow cookies'].cc-btn.cc-allow")
    LANGUANGE_BTN = (By.ID, 'carturestiLanguageDropdown')
    RO_ENG = (By.XPATH, "//*[@aria-labelledby='carturestiLanguageDropdown']//a[@class='dropdown-item']")
    SEARCH_BAR = (By.ID, 'search-input')
    PRODUCTS = (By.CLASS_NAME, 'cartu-grid-tile')
    MENIU = (By.CLASS_NAME, 'coco')
    BOOKS_TAB = (By.CSS_SELECTOR, 'a[data-ng-href="/raft/carte-109"][href="/raft/carte-109"]')
    IN_STOCK_FILTER = (By.XPATH, "//*[contains(@class, 'md-container')][following-sibling::*[contains(@class, 'md-label')]//descendant::*[contains(text(), 'In stock')]]")
    IN_STOCK_MSG = (By.XPATH, '//*[contains(text(), "In stock")]')
    IN_STOCK_PRODUCTS = (By.CSS_SELECTOR, '#coloana-produse .cartu-grid-tile')
    PRICE_FILTER = (By.XPATH, "//*[contains(@class, 'md-container')][following-sibling::*[contains(@class, 'md-label')]//descendant::*[contains(text(), '100 - 200')]]")
    PRODUCTS_PRICES = (By.CSS_SELECTOR, '#coloana-produse .suma')
    HYPERLINK_BTNS = {
        "STORES_BTN": (By.XPATH, '//a[contains(text(), "Stores")]'),
        "ASSISTANCE_BTN": (By.XPATH, '//a[contains(text(), "Assistance")]'),
        "FB_FOLLOW_BTN": (By.XPATH, '//a[contains(@href, "facebook.com")]')
        }
    ASSISTANT_BTN = (By.ID, 'druidContainerTooltip')
    ASSISTANT_CLOSE_BTN = (By.CLASS_NAME, 'fa-angle-down')

    def navigate_to_home_page(self):
        self.driver.get(self.HOME_PAGE_URL)
        self.driver.maximize_window()
        self.click_if_present_by_selector(*self.ACCEPT_COOKIES_BTN)
        if 'ROMÂNĂ' in self.get_text(self.LANGUANGE_BTN):
            self.click(self.LANGUANGE_BTN)
            self.click_if_contains_text(self.RO_ENG, 'ENGLISH')

    """Search"""
    def click_search_bar(self):
        self.click(self.SEARCH_BAR)

    def search_for_products(self, product_name):
        self.search_and_enter(self.SEARCH_BAR, product_name)

    def check_product_quantity(self):
        found_products = self.find_multiple(self.PRODUCTS)
        assert len(found_products) >=3

    """Filter1"""
    def click_meniu(self):
        self.click(self.MENIU)

    def click_books_tab(self):
        self.click(self.BOOKS_TAB)
        sleep(1)

    def apply_in_stock_filter(self):
        self.click(self.IN_STOCK_FILTER)

    def in_stock_msg_is_displayed(self):
        assert self.is_element_displayed(self.IN_STOCK_MSG)

    def in_stock_msg_is_correct(self, text):
        assert text in self.get_text(self.IN_STOCK_PRODUCTS)

    """Filter2"""
    # first two steps are the same
    def apply_price_filter(self):
        sleep(1)
        self.click(self.PRICE_FILTER)

    def check_products_prices(self, min_price, max_price):
        self.min_price = min_price
        self.max_price = max_price
        min_price = 100
        max_price = 200
        sleep(1)
        product_prices_text = [price.text for price in self.find_multiple(self.PRODUCTS_PRICES)]
        prices_list = [re.sub(r'[^\d.]', '', item) for item in product_prices_text if item.strip()]
        prices_list_int = [int(float(item)) for item in prices_list]
        for price in prices_list_int:
            assert price >= min_price and price <= max_price

    """@Test_URL"""
    def click_hyperlink_button(self, button_name):
        self.click(self.HYPERLINK_BTNS[button_name])

    def check_url(self, expected_URL):
        acc = (By.XPATH, '//*[@id="facebook"]/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/span/span')
        # if self.is_element_displayed(acc):
        #     sleep(2)
        #     self.click(acc)
        sleep(2)
        self.click(acc)
        current_url = self.current_url()
        assert current_url == expected_URL
        sleep(2)

    """Language"""
    def set_to_romanian(self):
        if 'ENGLISH' in self.get_text(self.LANGUANGE_BTN):
            self.click(self.LANGUANGE_BTN)
            self.click_if_contains_text(self.RO_ENG, 'ROMÂNĂ')

    def set_to_english(self):
        if 'ROMÂNĂ' in self.get_text(self.LANGUANGE_BTN):
            self.click(self.LANGUANGE_BTN)
            self.click_if_contains_text(self.RO_ENG, 'ENGLISH')

    def check_language(self, text):
        assert text in self.get_text(self.LANGUANGE_BTN)

    """Assistant"""
    def open_assistant(self):
        if self.is_element_not_displayed(self.ASSISTANT_CLOSE_BTN):
            self.click(self.ASSISTANT_BTN)

    def check_assistant_tab_displayed(self):
        assert self.is_element_displayed(self.ASSISTANT_CLOSE_BTN)

    def close_assistant(self):
        sleep(1)
        self.click(self.ASSISTANT_CLOSE_BTN)

    def check_assistant_tab_not_displayed(self):
        assert self.is_element_not_displayed(self.ASSISTANT_CLOSE_BTN)
