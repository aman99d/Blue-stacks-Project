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
        except Exception as e:
            print(e+"Unable to lunch browser")

    def test_navigate_to_url(self):
        try:
            driver.get(self.locators.url)
        except Exception as e:
            print(e+"Unable to navigate to browser")

    def test_search_city(self):
        try:
            WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH, self.locators.search_box)))
            str_search_box=driver.find_element_by_xpath(self.locators.search_box)
            str_search_box.click()
            time.sleep(2)
            str_search_box.send_keys("Delhi")
        except Exception as e:
            print(e + "Unable to enter city in search box")

    def test_city(self):
        try:
            WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, self.locators.search_result)))
            driver.find_element_by_xpath(self.locators.search_result).click()
        except Exception as e:
            print(e + "Unable to select city")

    def test_tempature(self):
        try:
            global str_temp
            WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, self.locators.tempature)))
            str_temp=driver.find_element_by_xpath(self.locators.tempature).text
            str_temp=str(str_temp[0:2])
            print(str_temp)
        except Exception as e:
            print(e+ "Unable to fetch tempature from UI")

    def test_close(self):
        driver.close()

    def test_weather(self):
        try:
            int_weather=Weather.test_call_weather(self)
            print(int_weather)
            if str(int_weather)==str(str_temp):
                assert True
            else:
                assert False
        except Exception as e:
            print(e+ "Match the difference between UI and API")


class Weather():

    def test_call_weather(self):
        try:
            url="http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=f73015b328a72a967dbf893df339e54f"
            response=requests.get(url)
            dict_reponse=json.loads(response.content)
            int_temp=str(dict_reponse['main']['temp'])
            int_temp=int_temp[0:2]
            return int_temp
        except Exception as e:
            print(e + "Unable to call API request")

