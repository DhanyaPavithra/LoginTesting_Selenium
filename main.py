"""
main.py

"""
# importing from Data and Locator files
from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# importing exceptions
from selenium.common.exceptions import NoSuchElementException

class Login:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def quit(self):
        self.driver.quit()

    def loginPage(self):
        try:

            self.boot()
            # username - column 4
            # password - column 5
            # test result - column 6

            for row in range(2, data.WebData().rowCount()+1):
                username = data.WebData().readData(row,4)
                password = data.WebData().readData(row, 5)

                locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, username)
                locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, password)
                locator.WebLocators().clickBtn(self.driver, locator.WebLocators().loginBtnLocator)

                self.driver.implicitly_wait(15)
                if self.driver.current_url == data.WebData().dashboardURL:
                    print("Successfully Logged In")
                    locator.WebLocators().clickBtn(self.driver, locator.WebLocators().burgerMenuLocator)
                    locator.WebLocators().clickBtn(self.driver, locator.WebLocators().logoutLocator)

                    data.WebData().writeData(row,6, "Passed")
                else:
                    print("Login Unsuccessful")
                    data.WebData().writeData(row,6, "Failed")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.quit()


obj = Login()
obj.loginPage()

