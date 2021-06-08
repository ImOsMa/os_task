import time

from robot.api.deco import keyword, library
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as Chrome_options
from frmk.configuration.browser import (
    BROWSER_NAME, BROWSER_DRIVER_BASE_PATH, BROWSER_WINDOW_SIZE, LOGIN_PAGE_URL,
    KNOWN_BROWSERS, BROWSER_MODE)
import os


class Singleton(type):
    """Singleton metaclass
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        return cls._instances[cls]

    @classmethod
    def clear_cache(cls):
        """Clears instances cache
        """
        cls._instances = {}


class Browser(metaclass=Singleton):  # pylint: disable=R0903
    """Browser singleton
    """

    def __init__(self):
        if BROWSER_NAME not in KNOWN_BROWSERS:
            raise Exception(f'Not supported browser: {BROWSER_NAME}')
        self.driver = self._get_driver(BROWSER_NAME)

    def _get_driver(self, name):
        driver_path = os.path.join(BROWSER_DRIVER_BASE_PATH,
                                   KNOWN_BROWSERS[name])
        if name == 'chrome':
            chrome_options = Chrome_options()
            chrome_options.add_argument("--window-size=" + BROWSER_WINDOW_SIZE)
            chrome_options.add_argument("enable-automation")
            if BROWSER_MODE == 'headless':
                chrome_options.add_argument("--headless")
            return Chrome(options=chrome_options, executable_path=driver_path)
        else:
            assert False


def get_browser():
    """Returns browser instance defined in config
    """
    browser = Browser()
    return browser.driver


def destroy_browser():
    """Destroys all cached browser instances
    """
    Singleton.clear_cache()


def close_page():
    """Closes site and browser
    """
    browser = get_browser()
    browser.quit()
    destroy_browser()


def open_page(url):
    """Opens site
    """
    browser = get_browser()
    browser.get(url)


@library
class Conf:
    """
    This class is to setup tests configuration
    """

    @staticmethod
    @keyword
    def setup_action():
        """Setup for tests
        """
        open_page(LOGIN_PAGE_URL)
        browser = get_browser()
        for _ in range(0, 150):
            time.sleep(0.1)
            if browser.execute_script(
                    'return document.readyState') == 'complete':
                break

    @staticmethod
    @keyword
    def teardown_action():
        """Teardown for tests
        """
        browser = get_browser()
        for _ in range(0, 150):
            time.sleep(0.1)
            if browser.execute_script(
                    'return document.readyState') == 'complete':
                break
        close_page()
