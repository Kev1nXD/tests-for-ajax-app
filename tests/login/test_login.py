import time

import pytest


@pytest.mark.parametrize(
    "username, password, expected_result",
    [
        (
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            ".ui.activity.DashboardActivity",
        ),
        (
            "invalid_username",
            "invalid_password",
            ".auth.presentation.login.LoginActivity",
        ),
    ],
)
def test_user_login(
    user_login_fixture, username: str, password: str, expected_result: str
):
    login_page = user_login_fixture
    login_page.click_entrance_button()
    time.sleep(1)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_submit_button()
    time.sleep(4)
    actual_result = login_page.check_activity()
    assert (actual_result == expected_result), f"Expected {expected_result} but got {actual_result}"
    if actual_result == ".ui.activity.DashboardActivity":
        login_page.driver.reset()
    elif actual_result == ".auth.presentation.login.LoginActivity":
        login_page.driver.quit()
