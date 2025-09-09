from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from PageObjects.homePage import HomePage
import os

class Test_018:

    def test_018(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.build_your_own_computer_url()=="https://demo.nopcommerce.com/apple-macbook-pro":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_013.png")
            self.driver.close()