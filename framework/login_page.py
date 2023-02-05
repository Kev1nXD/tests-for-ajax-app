from appium.webdriver.webdriver import WebDriver

from .page import Page


class LoginPage(Page):
    def __init__(
        self,
        driver: WebDriver,
        login_label: str,
        password_label: str,
        submit_button: str,
        entrance_button: str,
    ):
        """
        LoginPage constructor.

        :param driver: WebDriver instance
        :param login_label: locator for the 'login' label element
        :param password_label: locator for the 'password' label element
        :param submit_button: locator for the 'submit' button element
        :param entrance_button: locator for the 'entrance' button element
        """
        super().__init__(driver)
        self.login_label = login_label
        self.password_label = password_label
        self.submit_button = submit_button
        self.entrance_button = entrance_button

    def click_entrance_button(self) -> None:
        """
        Click the entrance button to login page.
        """
        self._click_element(locator=self.entrance_button)

    def enter_username(self, key: str) -> None:
        """
        Enter the username on 'login' page.

        :param key: the username string
        """
        self._send_keys_to_element(locator=self.login_label, keys=key)

    def enter_password(self, key: str) -> None:
        """
        Enter the password on 'login' page.

        :param key: the password string
        """
        self._send_keys_to_element(locator=self.password_label, keys=key)

    def click_submit_button(self) -> None:
        """
        Click the 'submit' button on 'login' page.
        """
        self._click_element(locator=self.submit_button)
