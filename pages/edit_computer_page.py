"""
Computer Database Application class for the Edit Computer Page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class EditComputerPage:

    def __init__(self, browser):
        self.browser = browser

    # CONSTANTS
    EDIT_PAGE_URL = "http://computer-database.herokuapp.com/computers/"
    EDIT_PAGE_TITLE = "Computers database"

    # Locators
    PAGE_HEADING = (By.XPATH, "//h1[text()='Edit computer']")
    COMPUTER_NAME = (By.ID, "name")
    INTRODUCED = (By.ID, "introduced")
    DISCONTINUED = (By.ID, "discontinued")
    SAVE_BUTTON = (By.XPATH, "//input[@value='Save this computer']")
    COMPANY_DROPDOWN = (By.ID, "company")
    CANCEL_BUTTON = (By.LINK_TEXT, "Cancel")
    UPDATE_MESSAGE = (By.XPATH, "//div[@class='alert-message warning']")
    DELETE_BUTTON = (By.XPATH, "//input[@value='Delete this computer']")

    # Methods

    # Assert Edit Page URL
    def assert_edit_page_url(self):
        assert self.browser.current_url == self.EDIT_PAGE_URL

    # Assert Edit Computer heading is displayed
    def assert_page_heading_is_displayed(self):
        page_heading = self.browser.find_element(*self.PAGE_HEADING)
        assert page_heading.is_displayed()

    # Enter value in the input field for specific element
    def enter_value_in_input_field(self, element, text):
        input_field = self.browser.find_element(*element)
        input_field.clear()
        input_field.send_keys(text)

    # Select value from the company dropdown by text
    def select_value_from_dropdown(self, company_name):
        company_dropdown = Select(self.browser.find_element(*self.COMPANY_DROPDOWN))
        company_dropdown.select_by_visible_text(company_name)

    # Click Save This Computer button
    def click_save_this_computer_button(self):
        save_this_computer_button = self.browser.find_element(*self.SAVE_BUTTON)
        save_this_computer_button.click()

    # Click Delete This Computer button
    def click_delete_button(self):
        click_delete_button = self.browser.find_element(*self.DELETE_BUTTON)
        click_delete_button.click()
