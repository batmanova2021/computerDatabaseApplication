import pytest

from pages.add_computer_page import AddComputerPage
from pages.home_page import ComputerDatabaseHomePage
from tests.test_utils import TestUtils


@pytest.mark.parametrize(["computer", "intro_dt", "disc_dt", "company"],
                         [
                             ("Anna K", "2018-01-01", "2021-01-01", "Apple Inc."),
                             ("Anna K", "0000-01-01", "2021-11-12", "IBM")
                         ])
@pytest.mark.regressiontest
def test_add_computer(browser, computer, intro_dt, disc_dt, company):
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
    # Enter value in the Computer Name field
    add_page.enter_value_in_input_field(add_page.COMPUTER_NAME, computer)
    # Enter value in the Introduced field
    add_page.enter_value_in_input_field(add_page.INTRODUCED, intro_dt)
    # Enter value in the Discontinued field
    add_page.enter_value_in_input_field(add_page.DISCONTINUED, disc_dt)
    # Select "Apple Inc." from drop down in Company field
    add_page.select_value_from_dropdown(company)
    # Click "Create this computer" button
    add_page.click_create_computer_button()
    # Assert "Done! Computer Anna K has been created" is displayed
    home_page.assert_success_message(home_page.SUCCESS_MESSAGE_TEXT)
    # cleanup. Delete computer "Anna K"
    TestUtils.delete_computer_by_name_and_verify(browser, computer)


@pytest.mark.skip(reason="waiting for the bug fix")
def test_add_page_submit_empty_form(browser):
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
    # Computer Name field is empty
    add_page.enter_value_in_input_field(add_page.COMPUTER_NAME, "")
    # Introduced field is empty
    add_page.enter_value_in_input_field(add_page.INTRODUCED, "")
    # Discontinued field is empty
    add_page.enter_value_in_input_field(add_page.DISCONTINUED, "")
    # Select default value from drop down in Company field
    add_page.select_value_from_dropdown("-- Choose a company --")
    # Click "Create this computer" button
    add_page.click_create_computer_button()
    # Computer was not added and user is still on Add Computer page
    add_page.assert_add_page_url()

