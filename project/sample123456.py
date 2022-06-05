import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from project.locators import Locators
import requests
import json

class TestAutomation():

    locators = Locators()

    def test_start(self):
        try:
            global driver
            options = webdriver.ChromeOptions()
            options.binary_location = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            chrome_driver_path = r"C:\\seleniumdriver\\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
            driver.maximize_window()
            return driver
        except Exception as e:
            print(e+"Unable to lunch browser")

    def test_url (self):
        try:
            print("url method")
            driver.get(self.locators.url)
        except Exception as e:
            print(0)

    def test_scroll(self):
        try:
            WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, self.locators.search_box)))

        except Exception as e:
            print("scroll")
    def test_button(self):
        try:
            driver.find_element_by_xpath(self.locators.button).click()
        except Exception as e:
            print("button")



