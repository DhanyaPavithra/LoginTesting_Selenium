"""
locator.py
"""
from selenium.webdriver.common.by import By

class WebLocators:
    def __init__(self):
        self.usernameLocator ='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
        self.passwordLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        self.loginBtnLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
        self.burgerMenuLocator = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]'
        self.logoutLocator = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'

    def enterText(self, driver, locator, textvalue):
        element = driver.find_element(by=By.XPATH, value=locator)
        element.clear()
        element.send_keys(textvalue)

    def clickBtn(self,driver,locator):
        driver.find_element(by=By.XPATH, value=locator).click()




