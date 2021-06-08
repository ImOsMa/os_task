"""
This file is to do the basic functionality of selenium
"""

import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException, StaleElementReferenceException)
from frmk.core.browsers import get_browser


class CommonActions:
    """
    This class contains functions for executing work with all pages
    """
    @staticmethod
    def scroll_page_until_element(element):
        """This function is to scroll down till web-element will seen
        """
        browser = get_browser()
        browser.execute_script("arguments[0].scrollIntoView(true);", element)

    @staticmethod
    def wait_for_page_load(seconds):
        """This function waits for the page to finish loading
        """
        browser = get_browser()
        for _ in range(0, seconds * 10):
            time.sleep(0.1)
            if (browser.execute_script('return document.readyState')
                    == 'complete'):
                break

    @staticmethod
    def find_an_element(locator, timeout=30):
        """This function is to find an element by locator
        """
        driver = get_browser()
        CommonActions.wait_for_page_load(1)
        try:
            element = WebDriverWait(
                driver, timeout).until(ec.presence_of_element_located(locator))
            CommonActions.scroll_page_until_element(element)
        except (TimeoutException, NoSuchElementException,
                StaleElementReferenceException):
            return None
        return element

    @staticmethod
    def get_text_of_one_web_element(locator):
        """This function is to get text of web element
        @locator - locator for the needed element
        """
        element = CommonActions.find_an_element(locator)
        assert element is not None, "Element not found"
        CommonActions.scroll_page_until_element(element)
        return element.text

    @staticmethod
    def clear_and_add_text(locator, text):
        """Function to add text in to field
        @locator - locator for the needed field
        @text - text that should be written
        """
        element = CommonActions.find_an_element(locator)
        assert element is not None, "Element not found"
        element.clear()
        return element.send_keys(text)

    @staticmethod
    def click_to_the_element(locator, timeout=30):
        """This function is to click to the element
        @locator - locator for the needed web element
        """
        element = CommonActions.find_an_element(locator, timeout)
        assert element is not None, "Element not found"
        CommonActions.wait_for_page_load()
        try:
            element = WebDriverWait(
                get_browser(), timeout).until(ec.
                                              element_to_be_clickable(locator))
        except TimeoutException as element_not_clickable:
            raise TimeoutException("Element is not clickable") \
                  from element_not_clickable
        try:
            element.click()
            click = True
        except StaleElementReferenceException:
            click = None
        assert_text_error = (
                             "Web_element is not clickable or it "
                             "is not attached to the page document")
        assert click is not None, assert_text_error
        return element

    @staticmethod
    def check_clickable_element(locator, timeout=30):
        """
        This function is to check, that element is clickable or not
        If it is clickable return True, else False
        @locator - locator for the needed web element
        """
        element = CommonActions.find_an_element(locator, timeout)
        assert element is not None, "Element not found"
        CommonActions.wait_for_page_load(1)
        if element.is_displayed() and element.is_enabled():
            return True
        else:
            return False


