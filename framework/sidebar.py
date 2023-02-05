from appium.webdriver.webdriver import WebDriver

from framework.dashboard_page import DashboardPage


class Sidebar(DashboardPage):
    def __init__(
        self,
        driver: WebDriver,
        sidebar_button: str,
        add_hub_button: str,
        settings_button: str,
        help_button: str,
        problem_report_button: str,
        video_surveillance_button: str,
        documentation_text: str,
    ):
        """
        Sidebar constructor.

        :param driver: An instance of the WebDriver class.
        :param sidebar_button: The locator of the sidebar button.
        :param add_hub_button: The locator of the 'add hub' button.
        :param settings_button: The locator of the 'settings' button.
        :param help_button: The locator of the 'help' button.
        :param problem_report_button: The locator of the 'problem report' button.
        :param video_surveillance_button: The locator of the 'video surveillance' button.
        :param documentation_text: The locator of the 'd    ocumentation' text.
        """
        super().__init__(driver, sidebar_button)
        self.add_hub_button = add_hub_button
        self.settings_button = settings_button
        self.help_button = help_button
        self.problem_report_button = problem_report_button
        self.video_surveillance_button = video_surveillance_button
        self.documentation_text = documentation_text

    def add_hub_button_is_clickable(self) -> bool:
        """
        Determines if the 'add hub' button is clickable.

        :return: A boolean value indicating whether the button is clickable.
        """
        return self.check_element_enable(self.add_hub_button)

    def settings_button_is_clickable(self) -> bool:
        """
        Determines if the 'settings' button is clickable.

        :return: A boolean value indicating whether the button is clickable.
        """
        return self.check_element_enable(self.settings_button)

    def help_button_is_clickable(self) -> bool:
        """
        Determines if the 'help' button is clickable.

        :return: A boolean value indicating whether the button is clickable.
        """
        return self.check_element_enable(self.help_button)

    def problem_report_button_is_clickable(self) -> bool:
        """
        Determines if the 'problem report' button is clickable.

        :return: A boolean value indicating whether the button is clickable.
        """
        return self.check_element_enable(self.problem_report_button)

    def video_surveillance_button_is_clickable(self) -> bool:
        """
        Determines if the 'video surveillance' button is clickable.

        :return: A boolean value indicating whether the button is clickable.
        """
        return self.check_element_enable(self.video_surveillance_button)

    def documentation_text_button_is_clickable(self) -> bool:
        """
        Determines if the 'documentation text' button is clickable.

        :return: A boolean value indicating whether the button is clickable.
        """
        return self.check_element_enable(self.documentation_text)
