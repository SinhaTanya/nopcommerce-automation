from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from PageObjects.homePage import HomePage

class Test_013:

    def test_013(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.build_your_own_computer_url()=="https://demo.nopcommerce.com/build-your-own-computer":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_013.png")
            self.driver.close()