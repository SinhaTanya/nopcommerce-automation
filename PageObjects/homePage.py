from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver

class HomePage:

    build_your_computer=(By.XPATH,"//a[text()='Build your own computer']")
    apple_macbook_pro=(By.XPATH,"//a[text()='Apple MacBook Pro']")
    htc_smartphone=(By.XPATH,"//a[text()='HTC smartphone']")
    virtual_gift_card=(By.XPATH,"//a[text()='$25 Virtual Gift Card']")
    build_your_computer_compare_button=( By.XPATH,"//div[@data-productid='1']//button[@title='Add to compare list']")
    apple_macbook_pro_compare_button=(By.XPATH,"//div[@data-productid='4']//button[@title='Add to compare list']")
    htc_smartphone_compare_button=(By.XPATH,"//div[@data-productid='18']//button[@title='Add to compare list']")
    virtual_gift_card_compare_button=(By.XPATH,"//div[@data-productid='45']//button[@title='Add to compare list']")
    # build_your_computer_compare_message=(By.XPATH,"")
    # apple_macbook_pro_compare_message=(By.XPATH,"")
    # htc_smartphone_compare_message=(By.XPATH,"")
    # virtual_gift_card_compare_message=(By.XPATH,"")
    successful_compare_message=(By.XPATH,"//div[@class='bar-notification success']")

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def build_your_computer_text(self):
        # text=self.driver.find_element(*self.build_your_computer).text
        return self.driver.find_element(*self.build_your_computer).is_displayed()

    def apple_macbook_pro_text(self):
        return self.driver.find_element(*self.apple_macbook_pro).is_displayed()

    def htc_smartphone_text(self):
        return self.driver.find_element(*self.htc_smartphone).is_displayed()

    def virtual_gift_card_text(self):
        return self.driver.find_element(*self.virtual_gift_card).is_displayed()

    def build_your_computer_click(self):
        self.driver.find_element(*self.build_your_computer).click()

    def apple_macbook_pro_click(self):
        self.driver.find_element(*self.apple_macbook_pro).click()

    def htc_smartphone_click(self):
        self.driver.find_element(*self.htc_smartphone).click()

    def virtual_gift_card_click(self):
        self.driver.find_element(*self.virtual_gift_card).click()

    def build_your_own_computer_url(self):
        self.build_your_computer_click()
        return self.driver.current_url

    def apple_macbook_pro_url(self):
        self.apple_macbook_pro_click()
        return self.driver.current_url

    def htc_smartphone_url(self):
        self.htc_smartphone_click()
        return self.driver.current_url

    def virtual_gift_card_url(self):
        self.virtual_gift_card_click()
        return self.driver.current_url

    def compare_message(self):
        wait=WebDriverWait(self.driver,10)
        message=wait.until(EC.presence_of_element_located(self.successful_compare_message))
        # return self.driver.find_element(*self.successful_compare_message).is_displayed()
        return message.is_displayed()

    def build_your_computer_compare_click(self):
        self.driver.find_element(*self.build_your_computer_compare_button).click()
        # return self.driver.find_element(*self.successful_compare_message).is_displayed()
        return self.compare_message()

    def apple_macbook_pro_compare_click(self):
        self.driver.find_element(*self.apple_macbook_pro_compare_button).click()
        # return self.driver.find_element(*self.successful_compare_message).is_displayed()
        return self.compare_message()

    def htc_smartphone_compare_click(self):
        self.driver.find_element(*self.htc_smartphone_compare_button).click()
        # return self.driver.find_element(*self.successful_compare_message).is_displayed()
        return self.compare_message()

    def virtual_gift_card_compare_click(self):
        self.driver.find_element(*self.virtual_gift_card_compare_button).click()
        # return self.driver.find_element(*self.successful_compare_message).is_displayed()
        return self.compare_message()

