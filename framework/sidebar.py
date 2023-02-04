from appium.webdriver.webdriver import WebDriver

from framework.dashboard_page import DashboardPage


class Sidebar(DashboardPage):
    def __init__(self, driver: WebDriver, sidebar: str):
        super().__init__(driver, sidebar)
