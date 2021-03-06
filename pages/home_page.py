"""
Computer Database Application class for the Home Page
"""
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ComputerDatabaseHomePage:

    def __init__(self, browser):
        self.browser = browser

    # CONSTANTS
    HOME_PAGE_URL = "http://computer-database.herokuapp.com/computers"
    HOME_PAGE_TITLE = "Computers database"
    SUCCESS_MESSAGE_TEXT = "Done! Computer Anna K has been created"
    UPDATE_MESSAGE_TEXT = "Done! Computer Anna K2 has been updated"
    DELETE_MESSAGE_TEXT = "Done! Computer has been deleted"
    NO_RESULTS_TEXT = "Nothing to display"

    # Locators
    NEW_COMPUTER_BUTTON = (By.ID, "add")
    MESSAGE = (By.XPATH, "//div[@class='alert-message warning']")
    SEARCH_FIELD = (By.ID, "searchbox")
    FILTER_BUTTON = (By.ID, "searchsubmit")
    NO_RESULTS_MESSAGE = (By.XPATH, "//div/em[text()='Nothing to display']")
    TOTAL_NUMBER = (By.XPATH, "//section[@id='main']/h1")

    # Methods

    # Navigate to Home Page
    def open_home_page(self):
        self.browser.get(self.HOME_PAGE_URL)

    # Assert Home Page title
    def assert_home_page_title(self):
        assert self.browser.title == self.HOME_PAGE_TITLE

    # Assert that "Add computer" button is displayed
    def add_button_is_displayed(self):
        add_button = self.browser.find_element(*self.NEW_COMPUTER_BUTTON)
        assert add_button.is_displayed()

    # Click on "Add new computer" button
    def click_add_new_computer_button(self):
        new_computer_button = self.browser.find_element(*self.NEW_COMPUTER_BUTTON)
        new_computer_button.click()

    # Assert success message is displayed and take a screenshot
    def assert_success_message(self, message):
        validation_message = self.browser.find_element(*self.MESSAGE)
        assert validation_message.text == message
        allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    # Search for specific computer and click on "Filter by name" button
    def search_my_computer(self, item):
        search_field = self.browser.find_element(*self.SEARCH_FIELD)
        search_field.send_keys(item)
        filter_button = self.browser.find_element(*self.FILTER_BUTTON)
        filter_button.click()

    # Click on computer name from the table
    def click_computer_name(self, link_text):
        computer_link = self.browser.find_element(By.LINK_TEXT, link_text)
        computer_link.click()

    # Assert that message is not displayed on the screen
    def assert_message_is_not_displayed(self):
        try:
            validation_message = self.browser.find_element(*self.MESSAGE)
        except NoSuchElementException:
            return True

    # Assert that computer with this name does not exist and "No results" is displayed.
    def assert_computer_does_not_exist(self):
        results_message = self.browser.find_element(*self.NO_RESULTS_MESSAGE)
        assert results_message.text == self.NO_RESULTS_TEXT

    # Get total number of computers from the home page heading
    def get_total_number_of_computers(self):
        total_number = self.browser.find_element(*self.TOTAL_NUMBER)
        number = total_number.text.split(' ')
        count = int(number[0])
        return count
