import pytest

from pages.add_computer_page import AddComputerPage
from pages.home_page import ComputerDatabaseHomePage


@pytest.mark.smoketest
def test_add_computer_navigation(browser):
    # Create an instance of ComputerDatabaseHomePage
    home_page = ComputerDatabaseHomePage(browser)
    # Create an instance of AddComputerPage
    add_page = AddComputerPage(browser)
    # Navigate to Computer Database App Home Page
    home_page.open_home_page()
    # Assert Home Page title
    home_page.assert_home_page_title()
    # Verify Add New Computer button is displayed
    home_page.add_button_is_displayed()
    # Click on Add New Computer button
    home_page.click_add_new_computer_button()
    # Assert user was navigated to the Add Computer page URL
    add_page.assert_add_page_url()
    # Assert "Add a computer" heading is displayed
    add_page.assert_page_heading_is_displayed()
