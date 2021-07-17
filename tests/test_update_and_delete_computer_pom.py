import pytest

from pages.add_computer_page import AddComputerPage
from pages.edit_computer_page import EditComputerPage
from pages.home_page import ComputerDatabaseHomePage


# base_url = "http://computer-database.herokuapp.com/computers"
# add_computer_url = "http://computer-database.herokuapp.com/computers/new"
# home_page_title = "Computers database"
# expected_success_message = "Done! Computer Anna K has been created"


@pytest.mark.regressiontest6
def test_update_computer(browser):
    # Create an instance of ComputerDatabaseHomePage
    home_page = ComputerDatabaseHomePage(browser)
    # Create an instance of AddComputerPage
    add_page = AddComputerPage(browser)
    edit_page = EditComputerPage(browser)
    # Navigate to Computer Database App Home Page
    home_page.open_home_page()
    # Verify Home Page title
    home_page.assert_home_page_title()
    # Verify Add New Computer button is displayed
    home_page.add_button_is_displayed()
    # Click on Add New Computer button
    home_page.click_add_new_computer_button()
    # Verify user was navigated to the Add Computer page URL
    add_page.assert_add_page_url()
    # Verify "Add a computer" heading is displayed
    add_page.assert_page_heading_is_displayed()

    # Enter "Anna K" in the Computer Name field
    add_page.enter_value_in_input_field(add_page.COMPUTER_NAME, "Anna K")
    # Enter "2021-01-01" in the Introduced field
    add_page.enter_value_in_input_field(add_page.INTRODUCED, "2021-01-01")
    # Enter "2021-01-01" in the Discontinued field
    add_page.enter_value_in_input_field(add_page.DISCONTINUED, "2021-01-01")
    # Select "Apple Inc." from drop down in Company field
    add_page.select_value_from_dropdown("Apple Inc.")
    # Click "Create this computer" button
    add_page.click_create_computer_button()
    # Assert "Done! Computer Anna K has been created" is displayed
    home_page.assert_success_message(home_page.SUCCESS_MESSAGE_TEXT)
    # Search for Computer with name "Anna K"
    home_page.search_my_computer("Anna K")
    # Click on "Anna K" computer
    home_page.click_computer_name("Anna K")
    # Change the value in Computer name field to "Anna K2"
    edit_page.enter_value_in_input_field(edit_page.COMPUTER_NAME, "Anna K2")
    # Change the value in Introduced date field to "1999-01-01"
    edit_page.enter_value_in_input_field(edit_page.INTRODUCED, "1999-01-01")
    # Change the value in Discontinued date field to "1999-01-01"
    edit_page.enter_value_in_input_field(edit_page.DISCONTINUED, "1999-02-02")
    # Select "Apple Inc." from drop down in Company field
    edit_page.select_value_from_dropdown("Thinking Machines")
    # Click "Save this computer" button
    edit_page.click_save_this_computer_button()
    # Assert "Done! Computer Anna K has been updated" is displayed
    home_page.assert_success_message(home_page.UPDATE_MESSAGE_TEXT)

    # Search for Computer with name "Anna K"
    home_page.search_my_computer("Anna K2")
    # Click on "Anna K2" computer
    home_page.click_computer_name("Anna K2")
    # Click "Delete this computer" button
    edit_page.click_delete_button()
    # Assert "Done! Computer has been deleted" is displayed
    home_page.assert_success_message(home_page.DELETE_MESSAGE_TEXT)



