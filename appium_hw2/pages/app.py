import os

import yaml
from appium import webdriver
from appium_hw2.pages.base_page import BasePage
from appium_hw2.pages.main_page import MainPage


class App(BasePage):
    desired_caps = {}

    def start(self):
        if self._driver is None:
            with open('../pages/phone.yml')as f:
                self.desired_caps = yaml.safe_load(f)['mumu_wework']
                self.desired_caps['udid'] = os.getenv('udid', None)
            self._driver = webdriver.Remote('http://192.168.163.1:4444/wd/hub', self.desired_caps)
            self._driver.implicitly_wait(10)

        else:
            self._driver.launch_app()

        # 要注意返回自己不然调用不了下面的方法
        return self

    def close(self):
        self._driver.quit()

    def main(self):
        return MainPage(self._driver)
