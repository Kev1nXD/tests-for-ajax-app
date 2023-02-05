def test_sidebar_buttons(
        user_login_fixture,
        sidebar_fixture,
        setup_logging_fixture
) -> None:
    """
    This test verifies that all buttons in the 'sidebar' are clickable.

    :param user_login_fixture: fixture to perform user login
    :param setup_logging_fixture: fixture for setup logger
    :param sidebar_fixture: fixture to access sidebar elements
    """
    logger = setup_logging_fixture
    logger.info("'test_sidebar_buttons' start test sidebar elements")
    sidebar = user_login_fixture
    sidebar.click_entrance_button()

    sidebar.enter_username("qa.ajax.app.automation@gmail.com")
    sidebar.enter_password("qa_automation_password")
    sidebar.click_submit_button()
    logger.info("'test_sidebar_buttons' logged in app")

    sidebar_fixture.click_sidebar_button()
    logger.info("'test_sidebar_buttons' clicked sidebar button")
    assert (
        sidebar_fixture.add_hub_button_is_clickable() is True
    ), "add hub button is unable"

    assert (
        sidebar_fixture.settings_button_is_clickable() is True
    ), "settings button is unable"

    assert (
        sidebar_fixture.help_button_is_clickable() is True
    ), "help button is unable"

    assert (
        sidebar_fixture.problem_report_button_is_clickable() is True
    ), "problem report button is unable"

    assert (
        sidebar_fixture.video_surveillance_button_is_clickable() is True
    ), "video surveillance button is unable"

    assert (
         sidebar_fixture.documentation_text_button_is_clickable() is True
    ), "video documentation text button is unable"
    logger.info("'test_sidebar_buttons' ended test sidebar elements")
