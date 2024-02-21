from selenium import webdriver
from Elements.locators import LOGIN_LOCATORS
class LoginPage:
    def __init__(self, driver):
        self.driver = driver


    def setUserName(self, username):
        self.driver.find_element(*LOGIN_LOCATORS.USERNAME_INPUT).clear()
        self.driver.find_element(*LOGIN_LOCATORS.USERNAME_INPUT).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*LOGIN_LOCATORS.PASSWORD_INPUT).clear()
        self.driver.find_element(*LOGIN_LOCATORS.PASSWORD_INPUT).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*LOGIN_LOCATORS.LOGIN_BUTTON).click()



