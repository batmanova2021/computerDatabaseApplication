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

    # Methods

    def open_home_page(self):
        self.browser.get(self.HOME_PAGE_URL)

    def assert_home_page_title(self):
        assert self.browser.title == self.HOME_PAGE_TITLE

    def add_button_is_displayed(self):
        add_button = self.browser.find_element(*self.NEW_COMPUTER_BUTTON)
        assert add_button.is_displayed()

    def click_add_new_computer_button(self):
        new_computer_button = self.browser.find_element(*self.NEW_COMPUTER_BUTTON)
        new_computer_button.click()

    def assert_success_message(self, message):
        validation_message = self.browser.find_element(*self.MESSAGE)
        assert validation_message.text == message

    def search_my_computer(self, item):
        search_field = self.browser.find_element(*self.SEARCH_FIELD)
        search_field.send_keys(item)
        filter_button = self.browser.find_element(*self.FILTER_BUTTON)
        filter_button.click()

    def click_computer_name(self, link_text):
        computer_link = self.browser.find_element(By.LINK_TEXT, link_text)
        computer_link.click()

    def assert_message_is_not_displayed(self):
        try:
            validation_message = self.browser.find_element(*self.MESSAGE)
        except NoSuchElementException:
            return True

    def assert_computer_does_not_exist(self):
        results_message = self.browser.find_element(*self.NO_RESULTS_MESSAGE)
        assert results_message.text == self.NO_RESULTS_TEXT
