import os

import yaml
from appium import webdriver

from page_object_appium.pages.base_page import BasePage
from page_object_appium.pages.main_page import Main


class App(BasePage):

    def start(self):
        _package = 'com.xueqiu.android'
        _activity = '.view.WelcomeActivityAlias'

        if self._driver is None:
            with open('../pages/phone.yml')as f:
                desired_caps = yaml.safe_load(f)['mumu_xueqiu']
                desired_caps['udid'] = os.getenv('udid', None)
                # desired_caps['udid'] = 'emulator-5554'
            self._driver = webdriver.Remote('http://192.168.163.1:4444/wd/hub', desired_caps)
            # self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(_package, _activity)

        return self

    def main(self):
        return Main(self._driver)
