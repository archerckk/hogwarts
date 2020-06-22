from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_demo:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        action=ActionChains(self.driver)
        action.double_click(self.driver.find_element(By.CSS_SELECTOR,'[value="dbl click me"]')).pause(1)
        action.click(self.driver.find_element(By.CSS_SELECTOR,'[value="click me"]')).pause(1)
        action.context_click(self.driver.find_element(By.CSS_SELECTOR,'[value="right click me"]')).pause(1)

        action.perform()
        sleep(3)

    def test_move_to(self):
        self.driver.get('http://www.baidu.com')
        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID,'s-usersetting-top')).pause(2)
        action.perform()

    def test_drag_drop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        action=ActionChains(self.driver)
        drag_element=self.driver.find_element(By.ID,'dragger')
        drop_element1=self.driver.find_element(By.CSS_SELECTOR,'')