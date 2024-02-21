# test_screenshot.py
import pytest
from selenium import webdriver
import allure

@pytest.fixture
def browser(request):
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_example(browser):
    browser.get("https://youtube.com")
    assert "Example" in browser.title

def test_another_example(browser):
    browser.get("https://youtube.com")
    assert "Another Example" in browser.title

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        try:
            driver = item.funcargs["browser"]
        except KeyError:
            return
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
