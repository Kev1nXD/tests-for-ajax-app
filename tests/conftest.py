import logging
import subprocess

import pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from framework.login_page import LoginPage
from framework.sidebar import Sidebar
from tests.elements_path.dashboard_elements_path import dashboard_elements
from tests.elements_path.login_page_elements_path import login_elements
from tests.elements_path.sidebar_elements_path import sidebar_elements
from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope="session")
def setup_logging_fixture():
    """
    A fixture to set up the 'logger' for the test module
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


@pytest.fixture(scope="session")
def run_appium_server(setup_logging_fixture) -> None:
    """
q    This fixture is used to run the 'Appium server' at the start of the test session.

    :param setup_logging_fixture: fixture for setup 'logger'
    """
    logger = setup_logging_fixture
    subprocess.Popen(
        ["appium", "-a", "0.0.0.0", "-p", "4723", "--allow-insecure", "adb_shell"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True,
    )
    logger.info("Appium server has been run")


@pytest.fixture(scope='function')
def sidebar_fixture(driver_fixture: WebDriver, setup_logging_fixture):
    """
    This fixture provides an instance of the 'Sidebar' class.
    It accepts a WebDriver instance as a parameter and returns
    a 'Sidebar' instance with the driver, and the element locators for
    various sidebar buttons.

    :param setup_logging_fixture: fixture for setup logger
    :param driver_fixture: WebDriver instance
    :return: 'Sidebar' instance
    """
    sidebar_elements_dict = sidebar_elements()
    dashboard_elements_dict = dashboard_elements()
    logger = setup_logging_fixture
    try:
        yield Sidebar(
            driver=driver_fixture,
            sidebar_button=dashboard_elements_dict["sidebar"],
            add_hub_button=sidebar_elements_dict["add_hub"],
            settings_button=sidebar_elements_dict["settings"],
            help_button=sidebar_elements_dict["help"],
            problem_report_button=sidebar_elements_dict["problem_report"],
            video_surveillance_button=sidebar_elements_dict["video_surveillance"],
            documentation_text=sidebar_elements_dict["documentation_text"]
        )
        logger.info("Sidebar instance created")
    except KeyError:
        logger.error("key error occurred in sidebar_fixture", exc_info=True)


@pytest.fixture(scope='function')
def user_login_fixture(driver_fixture: WebDriver, setup_logging_fixture):
    """
    This fixture provides an instance of the 'LoginPage' class.
    It accepts a WebDriver instance as a parameter and returns a
    'LoginPage' instance with the driver, and the element locators
    for various login page elements.


    :param driver_fixture: WebDriver instance
    :param setup_logging_fixture: fixture for setup logger
    :return: 'LoginPage' instance
    """
    page_elements_dict = login_elements()
    logger = setup_logging_fixture
    try:
        yield LoginPage(
            driver=driver_fixture,
            login_label=page_elements_dict["login_label"],
            password_label=page_elements_dict["password_label"],
            submit_button=page_elements_dict["submit_button"],
            entrance_button=page_elements_dict["entrance_button"]
        )
        logger.info("LoginPage instance created")
    except KeyError:
        logger.error("key error occurred in user_login_fixture", exc_info=True)


counter = 0


@pytest.fixture(scope="function", autouse=True)
def reset_driver(request, driver_fixture: WebDriver, setup_logging_fixture):
    """
    This fixture resets the driver after each
    test function is executed except last.


    :param setup_logging_fixture: fixture for setup logger
    :param request: fixture provided by pytest framework,
    which holds information about the current test session
    :param driver_fixture: WebDriver instance
    """
    logger = setup_logging_fixture
    global counter

    total_tests = request.session.testscollected

    counter += 1
    yield
    if counter < total_tests:
        driver_fixture.reset()
        logger.info("driver was reset")


@pytest.fixture(scope="session")
def driver_fixture(run_appium_server, setup_logging_fixture):
    """
    This fixture creates an instance of the Android WebDriver and
    returns it. It makes use of the run_appium_server fixture to run
    the Appium server and android_get_desired_capabilities function to get the
    desired capabilities for the Android device.

    :param setup_logging_fixture: fixture for setup logger
    :param run_appium_server: fixture that runs the 'Appium server'.
    :return: driver (WebDriver instance)
    """
    logger = setup_logging_fixture
    driver = webdriver.Remote(
        "http://localhost:4723/wd/hub", android_get_desired_capabilities()
    )
    logger.info("driver started")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    logger.info("driver ended")
