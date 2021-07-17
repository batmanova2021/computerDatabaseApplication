import pytest

from pages.add_computer_page import AddComputerPage
from pages.edit_computer_page import EditComputerPage
from pages.home_page import ComputerDatabaseHomePage
from tests.test_utils import TestUtils


@pytest.mark.regressiontest
def test_update_computer(browser):
    # Create an instance of ComputerDatabaseHomePage
    home_page = ComputerDatabaseHomePage(browser)
    # Create an instance of AddComputerPage
    add_page = AddComputerPage(browser)
    # Create an instance of EditComputerPage
    edit_page = EditComputerPage(browser)
    # create computer and verify using TestUtils
    TestUtils.create_computer_and_verify(browser, "Anna K", "2018-01-01", "2021-01-01", "Apple Inc.")

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

    # Search for Computer with name "Anna K2"
    home_page.search_my_computer("Anna K2")
    # Click on "Anna K2" computer
    home_page.click_computer_name("Anna K2")
    # Click "Delete this computer" button
    edit_page.click_delete_button()
    # Assert "Done! Computer has been deleted" is displayed
    home_page.assert_success_message(home_page.DELETE_MESSAGE_TEXT)
    # Search for computer name "Anna K2"
    home_page.search_my_computer("Anna K2")
    # Assert "No results to display" message is displayed
    home_page.assert_computer_does_not_exist()
