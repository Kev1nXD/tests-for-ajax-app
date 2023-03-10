from appium.webdriver.webdriver import WebDriver

from framework.page import Page


class DashboardPage(Page):
    def __init__(self, driver: WebDriver, sidebar_button: str):
        """
        DashboardPage constructor.

        :param driver: WebDriver instance
        :param sidebar_button: locator for the 'sidebar' button element
        """
        super().__init__(driver)
        self.sidebar_button = sidebar_button

    def sidebar_is_visible(self) -> bool:
        """
        Determines if the 'sidebar' button is clickable.

        :return: A boolean value indicating whether the 'sidebar' button is clickable.
        """
        return self._element_is_visible(self.sidebar_button)

    def click_sidebar_button(self) -> None:
        """
        Click 'sidebar' button.
        """
        self._click_element(self.sidebar_button)
