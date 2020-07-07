import yaml
from appium import webdriver
from appium_hw2.pages.base_page import BasePage
from appium_hw2.pages.main_page import MainPage


class App(BasePage):

    def start(self):
        if self._driver is None:
            with open('../pages/phone.yml')as f:
                desired_caps = yaml.safe_load(f)['mumu_wework']
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(10)

        else:
            self._driver.launch_app()

        # 要注意返回自己不然调用不了下面的方法
        return self

    def close(self):
        self._driver.quit()

    def main(self):
        return MainPage(self._driver)
