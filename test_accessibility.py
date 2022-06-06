from project.locators import Locators
from axe_selenium_python import Axe
from test_ui_automation import TestAutomation

class Test_accessibility:
    print("Testing accessibility")

    locators=Locators()
    browser=TestAutomation()

    def test_browser_launch(self):
        try:
            global driver
            driver=self.browser.test_start()
        except Exception as e:
            print(e+"Unable to lunch browser")

    def test_accessibility_checks(self):
        try:
            driver.get(self.locators.cowin_url)
            axe = Axe (driver)
            axe.inject()   # Injects axe-core Javascript into page
            results = axe.run()    # Runs axe accessibility checks
            axe.write_results(results,"Accessibility_report.json")  # Wrtie accessibility results in file
            driver.close()

        except Exception as e:
            print(e+"Unable to perform accessibility testing on "+ self.locators.cowin_url)