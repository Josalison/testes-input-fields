from playwright.sync_api import sync_playwright, Page

class BasePages:
    def __init__(self, page:Page):
        self.page = page

    

