from time import sleep

import yaml
from appium import webdriver


class TestWeWork:

    def setup(self):
        with open('phone.yml')as f:
            desired_caps = yaml.safe_load(f)['mumu_xueqiu']
        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self._driver.implicitly_wait(10)
        self.driver=webdriver.Remote()

    def teardown(self):
        pass

    def test_add_member(self):
        sleep(3)