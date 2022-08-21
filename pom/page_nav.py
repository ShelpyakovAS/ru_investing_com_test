from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base.utils import Utils
from typing import List
from log.decorators import log


class PageNav(SeleniumBase, Utils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__share_links: str = '#cross_rate_markets_stocks_1>tbody>tr>td>a'

    @log
    def get_nav_link_by_xpath(self, xpath) -> WebElement:
        return self.is_presence('xpath', xpath)

    @log
    def get_share_links(self) -> List[WebElement]:
        return self.are_present('css', self.__share_links)