from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.homePage import HomePage
import os

class Test_020:

    def test_020(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.apple_macbook_pro_compare_click():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_019.png")
            self.driver.close()