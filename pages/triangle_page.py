from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import triangle_page_locs as locs

class TrianglePage(BasePage):

    header_title = 'Triangle'
    page_url = '/triangle/'

    def check_h1_title(self):
        header = self.find(locs.header_loc)
        expect(header).to_have_text(self.header_title)

