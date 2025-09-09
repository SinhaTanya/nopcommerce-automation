from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.homePage import HomePage
import os

class Test_030:

    def test_030(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.build_your_computer_compare_click():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_029.png")
            self.driver.close()