import pytest

from pages.add_computer_page import AddComputerPage
from pages.home_page import ComputerDatabaseHomePage


@pytest.mark.regressiontest
def test_add_computer_navigation(browser):
    # Create an instance of ComputerDatabaseHomePage
    home_page = ComputerDatabaseHomePage(browser)
    # Create an instance of AddComputerPage
    add_page = AddComputerPage(browser)
    # Navigate to Computer Database App Home Page
    home_page.open_home_page()
    # Assert Home Page title
    home_page.assert_home_page_title()
    # Assert Add New Computer button is displayed
    home_page.add_button_is_displayed()
    # Click on Add New Computer button
    home_page.click_add_new_computer_button()
    # Assert user was navigated to the Add Computer page URL
    add_page.assert_add_page_url()
    # Assert "Add a computer" heading is displayed
    add_page.assert_page_heading_is_displayed()

    # Enter "Anna K" in the Computer Name field
    add_page.enter_value_in_input_field(add_page.COMPUTER_NAME, "Anna K")
    # Enter "2018-01-01" in the Introduced field
    add_page.enter_value_in_input_field(add_page.INTRODUCED, "2018-01-01")
    # Enter "2021-01-01" in the Introduced field
    add_page.enter_value_in_input_field(add_page.DISCONTINUED, "2021-01-01")
    # Select "Apple Inc." from drop down in Company field
    add_page.select_value_from_dropdown("Apple Inc.")
    # Click "Cancel" button
    add_page.click_cancel_button()
    # Assert "Done! Computer Anna K has been updated" message is NOT displayed
    home_page.assert_message_is_not_displayed()
    # Search for computer name "Anna K"
    home_page.search_my_computer("Anna K")
    # Assert "No results to display" message is displayed
    home_page.assert_computer_does_not_exist()
