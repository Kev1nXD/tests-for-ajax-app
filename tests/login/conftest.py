import pytest
from appium.webdriver.webdriver import WebDriver

from framework.login_page import LoginPage

# xpath of page elements
page_elements = {
    "login_label":
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
        ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
        "/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.EditText[1]",

    "password_label":
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
        ".widget.FrameLayout/android.widget.LinearLayout/android.widget"
        ".FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.EditText[2]",

    "submit_button":
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
        ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view"
        ".ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.TextView",

    "entrance_button":
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
        "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
        ".widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]"
}


@pytest.fixture(scope='function')
def user_login_fixture(driver: WebDriver):
    yield LoginPage(
        driver=driver,
        login_label=page_elements["login_label"],
        password_label=page_elements["password_label"],
        submit_button=page_elements["submit_button"],
        entrance_button=page_elements["entrance_button"]
    )
