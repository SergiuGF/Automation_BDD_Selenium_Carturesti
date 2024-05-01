from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import unittest

class Driver(unittest.TestCase):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)  # wait until elements are loaded
    driver.set_page_load_timeout(20)  # wait until DOM is loaded

    def close(self):
        sleep(3)
        self.driver.quit()
