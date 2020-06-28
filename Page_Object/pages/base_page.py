from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    _base_url=''

    def __init__(self,driver:WebDriver=None):
        self.count = 0  # 测试初始化次数变量

        # 假如没有传入driver的时候，新建一个webdriver
        if driver==None:
            self._driver=webdriver.Chrome()
            self.count += 1  # 测试初化次数

        #如果已经有driver了，就只用原来的driver
        else:
            self._driver=driver
        # self._driver=webdriver.Chrome()#测试代码

        # 如果基础链接不等于空，则使用子类重写的基础地址
        if self._base_url!="":
            self._driver.get(self._base_url)

    # 查找单个元素的方法封装显式等待
    def _find(self, *by):
        return WebDriverWait(self._driver, 15).until(expected_conditions.presence_of_element_located(*by))

    # 查找多个元素的方法封装显式等待
    def _finds(self, *by):
        return WebDriverWait(self._driver, 15).until(expected_conditions.presence_of_all_elements_located(*by))
