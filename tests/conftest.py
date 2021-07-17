"""
This is conftest.py file which has configuration for launching Chrome Driver
and managing corresponding chromdriver for the specific Chrome Browser version installed on
your computer.
Implicit Wait is set to 10 seconds.
Browser will open in a full screen.
Screenshot will be taken before closing the browser using Allure
"""
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# Shared setup and cleanup for all tests
@pytest.fixture()
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # wait 10 seconds until page will load
    browser.implicitly_wait(10)
    # maximize browser window to full screen
    browser.maximize_window()
    yield browser
    # make a screenshot before closing the browser
    allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    # when test is done, close ALL windows of the browser / browser instance
    browser.quit()

