from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class Page:
    def __init__(self, driver: WebDriver):
        """
        Page constructor.

        :param driver: WebDriver instance
        """
        self.driver = driver

    def __find_element(self, locator: str) -> WebElement:
        """
        Find a web element using its locator.

        :param locator: the locator string
        :return: the WebElement instance
        """
        return self.driver.find_element_by_xpath(locator)

    def _element_is_visible(self, locator) -> bool:
        """
        Check if element is on page

        :return: if element was found return True in otherwise False
        """
        try:
            self.__find_element(locator)
            return True
        except NoSuchElementException:
            return False

    def _click_element(self, locator: str):
        """
        Click a web element using its locator.

        :param locator: the locator string
        """
        self.__find_element(locator).click()

    def _send_keys_to_element(self, locator: str, keys: str):
        """
        Send keys to a web element using its locator.

        :param locator: the locator string
        :param keys: the keys string
        """
        self.__find_element(locator).send_keys(keys)

    def _check_activity(self) -> str:
        """
        Get the current activity of the driver.

        :return: the current activity string
        """
        return self.driver.current_activity

    def _check_element_enable(self, locator) -> bool:
        """
        Check if element is enabled.

        :return: True if element is enabled and False if unable
        """
        return self.__find_element(locator).is_enabled()
