import pytest
from settings import DRIVER_PATH
from settings import BROWSER_DICT
from settings import selected_browser
from settings import run_type


@pytest.fixture
def get_options():
    optoins = BROWSER_DICT[selected_browser]['option']()
    if selected_browser == 'firefox' and run_type == 'headless':
        optoins.headless = True
    if selected_browser == 'chrome' and run_type == 'headless':
        optoins.add_argument('headless')  # Use headless if you do not need a browser UI
    return optoins


@pytest.fixture
def get_webdriver(get_options):
    options = get_options
    driver = BROWSER_DICT[selected_browser]['driver'](options=options, executable_path=DRIVER_PATH)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://ru.investing.com'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.save_screenshot('end_screenshot.jpg')
    driver.quit()


if __name__ == "__main__":
    print ("Executed when invoked directly")
else:
    print ("Executed when imported")