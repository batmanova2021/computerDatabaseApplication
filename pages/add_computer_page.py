from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddComputerPage:

    def __init__(self, browser):
        self.browser = browser

    # CONSTANTS
    ADD_PAGE_URL = "http://computer-database.herokuapp.com/computers/new"
    ADD_PAGE_TITLE = "Computers database"

    #Locators
    PAGE_HEADING = (By.XPATH, "//h1[text()='Add a computer']")
    COMPUTER_NAME = (By.ID, "name")
    INTRODUCED = (By.ID, "introduced")
    DISCONTINUED = (By.ID, "discontinued")
    CREATE_BUTTON = (By.XPATH, "//input[@value='Create this computer']")
    COMPANY_DROPDOWN = (By.ID, "company")

    # Methods
    def assert_add_page_url(self):
        assert self.browser.current_url == self.ADD_PAGE_URL

    def assert_page_heading_is_displayed(self):
        page_heading = self.browser.find_element(*self.PAGE_HEADING)
        assert page_heading.is_displayed()

    def enter_value_in_input_field(self, element, text):
        input_field = self.browser.find_element(*element)
        input_field.send_keys(text)

    def select_value_from_dropdown(self, company_name):
        company_dropdown = Select(self.browser.find_element(*self.COMPANY_DROPDOWN))
        company_dropdown.select_by_visible_text(company_name)

    def click_create_computer_button(self):
        create_computer_button = self.browser.find_element(*self.CREATE_BUTTON)
        create_computer_button.click()
