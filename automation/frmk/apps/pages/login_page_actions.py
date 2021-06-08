
from frmk.apps.common.common_actions import CommonActions
from frmk.locators.login_page_locators import LoginPageLocators
from frmk.locators.home_page_locators import HomePageLocators


def sign_in(username, password, description, data_type='correct'):
    """
    Types given text into username, password, description inputs and precess
    Login
    data_type - (correct, short_username, short_password, empty_password,
                 empty_username)
    """
    if data_type != 'empty_password' and data_type != 'empty_username':
        CommonActions.clear_and_add_text(username,
                                         LoginPageLocators.username_field)
        CommonActions.clear_and_add_text(password,
                                         LoginPageLocators.password_field)
        CommonActions.clear_and_add_text(
            description,
            LoginPageLocators.username_description_field)
    else:
        CommonActions.clear_and_add_text(
            description,
            LoginPageLocators.username_description_field)
        if data_type == 'empty_password':
            CommonActions.clear_and_add_text(username,
                                             LoginPageLocators.username_field)
        elif data_type == 'empty_username':
            CommonActions.clear_and_add_text(password,
                                             LoginPageLocators.password_field)

    if data_type == 'correct':
        CommonActions.click_to_the_element(LoginPageLocators.login_button)
        CommonActions.find_an_element(HomePageLocators.home_text)
        home_text = CommonActions.get_text_of_one_web_element(
                    HomePageLocators.home_text)
        assert_text_error = ("Login failed! Home text has not found. "
                             "User still on login page")
        logged_in_text = CommonActions.get_text_of_one_web_element(
                         HomePageLocators.logged_in_text)
        assert home_text == "Home", assert_text_error
        assert_text_error = "Logged in text has not found"
        assert logged_in_text == "You're logged in!!", assert_text_error
    else:
        CommonActions.find_an_element(LoginPageLocators.error_message)
        error_text = CommonActions.get_text_of_one_web_element(
            LoginPageLocators.error_message)
        assert_text_error = "Incorrect error text"
        if data_type == 'short_username':
            assert error_text == ((
                   "Your username must be between 3 and 50 characters long"),
                   assert_text_error)
        elif data_type == 'short_password':
            assert error_text == ((
                   "Your password must be between 3 and 50 characters long"),
                    assert_text_error)
        elif data_type == 'empty_password':
            assert error_text == ((
                   "You did not enter a password"), assert_text_error)
        elif data_type == 'empty_username':
            assert error_text == ((
                   "You did not enter a username"), assert_text_error)
        CommonActions.find_an_element(
            LoginPageLocators.enabled_login_button)
