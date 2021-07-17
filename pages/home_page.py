from selenium.webdriver.common.by import By


class ComputerDatabaseHomePage:

    def __init__(self, browser):
        self.browser = browser

    # CONSTANTS
    HOME_PAGE_URL = "http://computer-database.herokuapp.com/computers"
    HOME_PAGE_TITLE = "Computers database"
    SUCCESS_MESSAGE = "Done! Computer Anna K has been created"

    # Locators
    NEW_COMPUTER_BUTTON = (By.ID, "add")
    MESSAGE = (By.XPATH, "//div[@class='alert-message warning']")


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

    def assert_success_message(self):
        validation_message = self.browser.find_element(*self.MESSAGE)
        assert validation_message.text == self.SUCCESS_MESSAGE
