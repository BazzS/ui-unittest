from selenium.common.exceptions import TimeoutException

from byclass_attr import SearchHelpClassAttr
from click_page import SearchClick
from client_delay import SearchHelpClientDelay
from dinamic_table import SearchDynamicTable
from hidden_layers import SearchHiddenLayers
from mouse_over import SearchMouseOver
from sample_app import SearchSampleApp
from verify_text import SearchVerifyText

import time
import unittest
from selenium import webdriver

class PlayGround(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_classattr(self):
        resource = "classattr"
        browser = self.driver
        page = SearchHelpClassAttr(browser)
        page.go_to_site(resource)

        page.click_button()
        page.switch_to_alert_accept()
        button = page.test_button()
        self.assertTrue(button)

    def test_click(self):
        resource = "click"
        browser = self.driver
        page = SearchClick(browser)
        page.go_to_site(resource)

        page.click_button()
        button = page.click_button()
        self.assertTrue(button)

    def test_clientdelay(self):
        resource = "clientdelay"
        browser = self.driver
        page = SearchHelpClientDelay(browser)
        page.go_to_site(resource)

        page.click_button()
        button = page.wait_to_text()
        self.assertTrue(button)

    def test_dinamictable(self):
        resource = "dynamictable"
        browser = self.driver
        page = SearchDynamicTable(browser)
        page.go_to_site(resource)

        chrome_cpu = page.chrome_cpu()
        tasks = page.tasks()
        list_task = tasks.text.split("\n")
        chrome_task = [chrome for chrome in list_task if chrome.startswith("Chrome")]
        chrome_detail_list = chrome_task[0].split()
        cpu = [cpu for cpu in chrome_detail_list if '%' in cpu]
        self.assertEqual(chrome_cpu, f'{chrome_detail_list[0]} CPU: {cpu[0]}')

    def test_hiddenlayers(self):
        resource = "hiddenlayers"
        browser = self.driver
        page = SearchHiddenLayers(browser)
        page.go_to_site(resource)

        first = page.click_button()
        self.assertTrue(first)
        second = page.click_button()
        self.assertFalse(second)

    def test_mouseover(self):
        resource = "mouseover"
        browser = self.driver
        page = SearchMouseOver(browser)
        page.go_to_site(resource)

        first_count = page.find_click_count()
        page.double_click_link()
        second_count = page.find_click_count()
        self.assertEqual(int(second_count) - int(first_count), 2)

    def test_sampleapp(self):
        resource = "sampleapp"
        browser = self.driver
        page = SearchSampleApp(browser)
        page.go_to_site(resource)

        login_status = page.login_status()
        self.assertEqual(login_status, 'User logged out.')

    def test_verifytext(self):
        resource = "verifytext"
        browser = self.driver
        page = SearchVerifyText(browser)
        page.go_to_site(resource)

        text = page.search_text()
        self.assertEqual(text, "Welcome UserName!")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
