from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

    # if browser == 'chrome':
    #     driver = webdriver.Chrome()
    #     print("Launching chrome browser.........")
    # elif browser == 'firefox':
    #     driver = webdriver.Firefox()
    #     print("Launching firefox browser.........")
    # return driver


# def pytest_addoption(parser):  # This will get the value from CLI /hooks
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):  # This will return the Browser value to setup method
#     return request.config.getoption("--browser")
