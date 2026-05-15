from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.locators import login_page_locs as loc

class CustomerLogin(BasePage):
    page_url = '/simulated-login/'


    def login_and_password(self, username, password):
        username_field = self.find(loc.username_loc)
        username_field.fill(username)
        password_field = self.find(loc.password_loc)
        password_field.fill(password)
        self.find(loc.login_button_loc).click()

    def check_error_message(self, error_message):
        message = self.find(loc.message_loc)
        expect(message).to_have_text('Login Details Incorrect')

