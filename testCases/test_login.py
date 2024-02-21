import pytest
import time
from selenium import webdriver
from pageOjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import allure
from utilities.customLogger import LogGen
from Elements.locators import LOGIN_LOCATORS



class Test_001_Login:
    baseURL = ReadConfig.getAplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title =="Your store. Login":
            self.logger.info("**** Home page title test passed ****")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("/Users/nfqasia/PycharmProjects/Digiflow/Screenshots/test_homepage_title.png")
            self.logger.error("**** Home page title test failed****")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("/Users/nfqasia/PycharmProjects/Digiflow/Screenshots/test_login.png")
            self.logger.error('***** Login Test fail *****')
            self.driver.close()
            assert False












