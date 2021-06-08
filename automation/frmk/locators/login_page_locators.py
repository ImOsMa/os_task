"""
This file is to describe locators of the login page
"""
from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Contains a list of all locators shared by login page
    """
    # Fields
    username_field = (By.ID, "username")
    password_field = (By.ID, "password")
    username_description_field = (By.ID, "formly_3_input_username_0")

    # Buttons
    login_button = (By.CLASS_NAME, "btn btn-danger")
    enabled_login_button = (By.XPATH, "//button[@disabled='disabled']")

    # Error messages
    username_empty_error_message = (
        By.XPATH,
        "//div[text()='You did not enter a username']")
    error_message = (By.XPATH, "//div[@class='help-block ng-active']")
    description_error = (By.XPATH,
                         "//div[@class='form-group ng-scope has-error']")
