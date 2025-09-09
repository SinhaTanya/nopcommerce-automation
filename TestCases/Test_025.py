from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.homePage import HomePage
import os

class Test_025:

    def test_025(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.htc_smartphone_compare_click():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_024.png")
            self.driver.close()