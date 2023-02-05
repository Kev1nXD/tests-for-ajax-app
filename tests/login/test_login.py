from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.elements_path.dashboard_elements_path import dashboard_elements


@pytest.mark.parametrize(
    "username, password, expected_result",
    [
        (
            "invalid_username",
            "invalid_password",
            ".auth.presentation.login.LoginActivity",
        ),
        (
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            ".ui.activity.DashboardActivity",
        ),
    ],
    ids=["invalid credentials", "valid credentials"],
)
def test_user_login(
        user_login_fixture,
        setup_logging_fixture,
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
    login_page.click_entrance_button()
    logger.info("test_user_login clicked entrance button")
    login_page.enter_username(username)
    logger.info("test_user_login filled username form")
    login_page.enter_password(password)
    logger.info("test_user_login filled password form")
    login_page.click_submit_button()
    logger.info("test_user_login clicked submit button")
    if request.node.name == "test_user_login[valid credentials]":
        wait = WebDriverWait(login_page.driver, 5)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, dashboard_elements()["sidebar"])
        ))
    else:
        wait = WebDriverWait(login_page.driver, 5)
        wait.until(EC.invisibility_of_element_located(
            (By.XPATH, dashboard_elements()["sidebar"])
        ))

    actual_result = login_page.check_activity()
    assert (
        actual_result == expected_result
    ), f"Expected {expected_result} but got {actual_result}"
    logger.info(
        "test_user_login ended test log in functionality"
        f" with username: {username} and password: {password}"
    )
