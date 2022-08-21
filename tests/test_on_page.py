import random
import time
import pytest
from selenium.webdriver import ActionChains
from pom.page_nav import PageNav
from base.utils import Utils
import logging
import log.project_log_conf
from log.decorators import log


CLIENT_LOG = logging.getLogger('project_log')


@pytest.mark.usefixtures('setup')
class TestOnPage:

    def test_page_nav(self):

        work_elems_xpath = {'Котировки': '//*[@id="navMenu"]/ul/li[1]/a',
                            'Акции': '//*[@id="navMenu"]/ul/li[1]/ul/li[4]/a',
                            'Россия': '//*[@id="navMenu"]/ul/li[1]/ul/li[4]/div/ul[1]/li[3]/a',
                            'Меню типы акций': '//*[@id="stocksFilter"]',
                            'Россия - все акции': '//*[@id="all"]'}

        CLIENT_LOG.info('Запуск теста "test_page_nav"')

        page_nav = PageNav(self.driver)
        CLIENT_LOG.info('Доступ к драверу получен')

        action = ActionChains(self.driver)
        CLIENT_LOG.info('Создан new ActionChains(дравера)')

        action.move_to_element(page_nav.get_nav_link_by_xpath(work_elems_xpath['Котировки'])).perform()
        CLIENT_LOG.info('Наведение на элемент "Котировки"')

        action.move_to_element(page_nav.get_nav_link_by_xpath(work_elems_xpath['Акции'])).perform()
        CLIENT_LOG.info('Наведение на элемент "Акции"')

        page_nav.get_nav_link_by_xpath(work_elems_xpath['Россия']).click()
        CLIENT_LOG.info('Нажатие на элемент "Россия"')

        page_nav.get_nav_link_by_xpath(work_elems_xpath['Меню типы акций']).click()
        CLIENT_LOG.info('Нажатие на элемент "Меню типы акций"')
        time.sleep(1)

        page_nav.get_nav_link_by_xpath(work_elems_xpath['Россия - все акции']).click()
        CLIENT_LOG.info('Выбор элемента "Россия - все акции"')
        time.sleep(1)

        shares = page_nav.get_share_links()
        CLIENT_LOG.info('Получение списка акций таблицы "Россия - все акции"')

        random_element = random.choice(shares)
        CLIENT_LOG.info('Выбор случаной акции списка акций таблицы "Россия - все акции"')
        time.sleep(1)

        expected_value = random_element.get_attribute('title')
        CLIENT_LOG.info('Получение значения expected_value (title элемента - акции)')

        random_element.click()
        CLIENT_LOG.info('Нажатие на выбраную акцию таблицы "Россия - все акции"')
        time.sleep(1)

        expected_result = \
            page_nav.get_nav_link_by_xpath('//*[@id="__next"]/div[2]/div/div/div[2]/main/div/div[1]/div[1]/h1').text
        CLIENT_LOG.info('Получение значения expected_result - название акции на странице ')

        assert expected_value == Utils.cat_str_end(expected_result.replace('\xa0', ' '))