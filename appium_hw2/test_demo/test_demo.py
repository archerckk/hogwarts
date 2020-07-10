from time import sleep

import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:

    def setup(self):
        with open('../pages/phone.yml')as f:
            desired_caps = yaml.safe_load(f)['mumu_wework']
        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self._driver.implicitly_wait(10)

    def teardown(self):
        self._driver.quit()

    def test_click(self):
        _contact_tab_loc = (By.XPATH, '//*[@class="android.widget.LinearLayout"]//*[@text="通讯录"]')

        element = WebDriverWait(self._driver, 10).until(
            expected_conditions.presence_of_element_located(*_contact_tab_loc))
        element.click()
        sleep(3)
