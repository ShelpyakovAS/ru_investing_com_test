import os
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium import webdriver


BROWSER_DICT = {
    'chrome': {
        'option': chrome_options,
        'driver': webdriver.Chrome,
        'path': '/tests/chromedriver.exe'
    },
    'firefox': {
        'option': firefox_options,
        'driver': webdriver.Firefox,
        'path': '/tests/geckodriver.exe'
    }
}

selected_browser = 'chrome'   # Select browser 'firefox' or 'chrome'
run_type = 'headless'    # Use 'headless' for headless mode or ''


DRIVER_PATH = os.getcwd().replace('\\', '/') + BROWSER_DICT[selected_browser]['path']