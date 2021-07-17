import time

import pytest

from pages.add_computer_page import AddComputerPage
from pages.home_page import ComputerDatabaseHomePage


# base_url = "http://computer-database.herokuapp.com/computers"
# add_computer_url = "http://computer-database.herokuapp.com/computers/new"
# home_page_title = "Computers database"
# expected_success_message = "Done! Computer Anna K has been created"


@pytest.mark.regressiontest5
def test_add_computer_navigation(browser):
    # Create an instance of ComputerDatabaseHomePage
    home_page = ComputerDatabaseHomePage(browser)
    # Create an instance of AddComputerPage
    add_page = AddComputerPage(browser)
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

    #
    add_page.enter_value_in_input_field(add_page.COMPUTER_NAME, "Anna K")
    add_page.enter_value_in_input_field(add_page.INTRODUCED, "2021-01-01")
    add_page.enter_value_in_input_field(add_page.DISCONTINUED, "2021-01-01")
    add_page.select_value_from_dropdown("Apple Inc.")
    time.sleep(5)
    add_page.click_create_computer_button()
    home_page.assert_success_message()

    # company_dropdown = Select(browser.find_element_by_id("company"))
    # company_dropdown.select_by_visible_text("Apple Inc.")
    # success_message = browser.find_element_by_xpath("//div[@class='alert-message warning']")
    # assert success_message.text == expected_success_message
    # print(success_message.text)
