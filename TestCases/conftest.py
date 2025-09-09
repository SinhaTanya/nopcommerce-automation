import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
    location=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=location)
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()
    return driver
