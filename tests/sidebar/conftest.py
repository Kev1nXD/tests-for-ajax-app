import pytest
from appium.webdriver.webdriver import WebDriver

from framework.sidebar import Sidebar

# xpath of page elements
page_elements = {
    "sidebar": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
               ".widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android"
               ".view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout["
               "2]/android.view.ViewGroup/android.widget.FrameLayout",
    "add_hub": "",
    "app_options": "",
    "help": "",
    "problem_report": "",
    "video_surveillance": ""
}


@pytest.fixture(scope='function')
def user_login_fixture(driver: WebDriver):
    yield Sidebar(
        driver=driver,

    )
