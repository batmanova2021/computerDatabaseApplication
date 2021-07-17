from pages.add_computer_page import AddComputerPage
from pages.edit_computer_page import EditComputerPage
from pages.home_page import ComputerDatabaseHomePage


class TestUtils:

    def __init__(self, browser):
        self.browser = browser

    @staticmethod
    def create_computer(browser, computer_name, date_intro, date_disc, company_name):
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
        add_page.enter_value_in_input_field(add_page.COMPUTER_NAME, computer_name)
        # Enter "2018-01-01" in the Introduced field
        add_page.enter_value_in_input_field(add_page.INTRODUCED, date_intro)
        # Enter "2021-01-01" in the Discontinued field
        add_page.enter_value_in_input_field(add_page.DISCONTINUED, date_disc)
        # Select "Apple Inc." from drop down in Company field
        add_page.select_value_from_dropdown(company_name)
        # Click "Create this computer" button
        add_page.click_create_computer_button()
        # Assert "Done! Computer Anna K has been created" is displayed
        home_page.assert_success_message(home_page.SUCCESS_MESSAGE_TEXT)

    @staticmethod
    def delete_computer_by_name(browser, computer_name):
        # Create an instance of ComputerDatabaseHomePage
        home_page = ComputerDatabaseHomePage(browser)
        # Create an instance of AddComputerPage
        add_page = AddComputerPage(browser)
        # Create an instance of EditComputerPage
        edit_page = EditComputerPage(browser)
        # Search for Computer with specific name
        home_page.search_my_computer(computer_name)
        # Click on specific computer
        home_page.click_computer_name(computer_name)
        # Click "Delete this computer" button
        edit_page.click_delete_button()
        # Assert "Done! Computer has been deleted" is displayed
        home_page.assert_success_message(home_page.DELETE_MESSAGE_TEXT)
        # Search for computer with specific
        home_page.search_my_computer(computer_name)
        # Assert "No results to display" message is displayed
        home_page.assert_computer_does_not_exist()
