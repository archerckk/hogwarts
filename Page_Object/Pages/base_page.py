from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Base_Page(object):
    _base_url=''

    def __init__(self,driver:WebDriver=None):
        self.count=0
        if driver==None:
            self._driver=webdriver.Chrome()
            self.count+=1
        else:
            self._driver=driver
        # self._driver=webdriver.Chrome()

        if self._base_url!="":
            self._driver.get(self._base_url)

    def find(self,by,locater):
        return self._driver.find_element(by,locater)

    def finds(self, by, locater):
        return self._driver.find_elements(by, locater)