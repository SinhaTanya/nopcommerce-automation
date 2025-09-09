from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.homePage import HomePage
import os

class Test_022:

    def test_022(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)
        # self.hp.build_your_computer_text()

        if self.hp.htc_smartphone_text():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_022.png")
            self.driver.close()

