from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.homePage import HomePage
import os

class Test_027:

    def test_027(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)
        # self.hp.build_your_computer_text()

        if self.hp.virtual_gift_card_text():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_027.png")
            self.driver.close()

