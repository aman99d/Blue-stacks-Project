import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from project.locators import Locators
from test_ui_automation import TestAutomation
import datetime

class Test_cowin_ui:
    print("Book Vaccine slot")

    locators=Locators()
    browser=TestAutomation()

    def test_browser_launch(self):
        try:
            global driver
            driver=self.browser.test_start()
        except Exception as e:
            print(e+"Unable to lunch browser")

    def test_navigate_to_url(self):
        try:
            driver.get(self.locators.cowin_url)
        except Exception as e:
            print(e+"Unable to open cowin website")

    def test_sign_in(self):
        try:
            WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH, self.locators.cowin_signin_button)))
            str_signin_button=driver.find_element_by_xpath(self.locators.cowin_signin_button)
            str_signin_button.click()
            time.sleep(2)
        except Exception as e:
            print(e + "Unable to click sign in button")

    def test_send_mobile_no(self):
        try:
            tab_list = driver.window_handles
            driver.switch_to_window(tab_list[1])
            driver.find_element_by_xpath(self.locators.mobile_no).click()
            driver.find_element_by_xpath(self.locators.mobile_no).send_keys("9873499095")
            driver.find_element_by_xpath(self.locators.otp).click()
        except Exception as e:
            print(e + "Unable to click OTP button")

    def test_search_button(self):
        try:
            print("Search Method started")
            start_time = datetime.datetime.now()
            print(start_time)
            for item in range(2000):
                driver.find_element_by_xpath(self.locators.search_button).click()
                time.sleep(0.03)
                driver.find_element_by_xpath(self.locators.filter_18.replace("<text_replace>","Covaxin")).click()
                time.sleep(0.03)
                print(item)
            end_time = datetime.datetime.now()
            time_elapsed = end_time - start_time
            print(end_time)
            print(time_elapsed)
        except Exception as e:
            print(e + "Unable to search button")