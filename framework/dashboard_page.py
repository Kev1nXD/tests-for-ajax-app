from appium.webdriver.webdriver import WebDriver

from framework.page import Page


class DashboardPage(Page):
    def __init__(self, driver: WebDriver, sidebar: str):
        super().__init__(driver)
        self.sidebar = sidebar


