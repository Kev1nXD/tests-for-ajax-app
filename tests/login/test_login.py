from logging import Logger

import pytest

from framework.sidebar import Sidebar
from framework.login_page import LoginPage


@pytest.mark.parametrize(
    "username, password, expected_result",
    [
        (
            "invalid_username",
            "invalid_password",
            False,
        ),
        (
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            True,
        ),
    ],
    ids=["invalid credentials", "valid credentials"],
)
def test_user_login(
        user_login_fixture: LoginPage,
        sidebar_fixture: Sidebar,
        setup_logging_fixture: Logger,
        username: str,
        password: str,
        expected_result: str,
        request
) -> None:
    """
    Test function to verify the user login functionality

    :param user_login_fixture: fixture that sets up the login page
    :param username: username to be entered in the login form
    :param password: password to be entered in the login form
    :param expected_result: expected result after login
    """
    logger = setup_logging_fixture
    logger.info(f"{request.node.name} start test login functionality")
    login_page = user_login_fixture
    sidebar = sidebar_fixture
    login_page.click_entrance_button()
    logger.info("test_user_login clicked entrance button")
    login_page.enter_username(username)
    logger.info("test_user_login filled username form")
    login_page.enter_password(password)
    logger.info("test_user_login filled password form")
    login_page.click_submit_button()
    logger.info("test_user_login clicked submit button")

    actual_result = sidebar.sidebar_is_visible()
    assert (
        actual_result == expected_result
    ), f"Expected {expected_result} but got {actual_result}"
    logger.info(
        "test_user_login ended test log in functionality"
        f" with username: {username} and password: {password}"
    )
