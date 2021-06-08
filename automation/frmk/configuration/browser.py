"""Contains browser related configuration"""

import os


BROWSER_NAME = 'chrome'
BROWSER_MODE = 'with head'
BROWSER_DRIVER_BASE_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '..',
    '..',
    'deps'
)
BROWSER_WINDOW_SIZE = '1920,1080'

LOGIN_PAGE_URL = (
    'http://www.way2automation.com/angularjs-protractor/registeration/#/login')


KNOWN_BROWSERS = {
    'chrome': 'chromedriver'
}

