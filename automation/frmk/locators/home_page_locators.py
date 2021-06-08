"""
This file is to describe locators of the home page
"""
from selenium.webdriver.common.by import By


class HomePageLocators:
    """Contains a list of all locators shared by home page
    """
    # Texts
    home_text = (By.XPATH, "//h1[text()='Home']")
    logged_in_text = (By.XPATH, '//p[text()="You\'re logged in!!"]')

    # Buttons
    logout_button = (By.XPATH, "//a[text()='Logout']")
