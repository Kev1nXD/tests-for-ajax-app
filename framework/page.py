from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver


class Page:
    def __init__(self, driver: WebDriver):
        """
            Page constructor.

            :param driver: WebDriver instance
        """
        self.driver = driver

    def find_element(self, locator: str) -> WebElement:
        """
            Find a web element using its locator.

            :param locator: the locator string
            :return: the WebElement instance
        """
        return self.driver.find_element_by_xpath(locator)

    def click_element(self, locator: str):
        """
            Click a web element using its locator.

            :param locator: the locator string
        """
        self.find_element(locator).click()

    def send_keys_to_element(self, locator: str, keys: str):
        """
            Send keys to a web element using its locator.

            :param locator: the locator string
            :param keys: the keys string
        """
        self.find_element(locator).send_keys(keys)

    def check_activity(self) -> str:
        """
            Get the current activity of the driver.

            :return: the current activity string
        """
        return self.driver.current_activity
