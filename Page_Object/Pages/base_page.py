from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page(object):
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

        #如果基础连接不等于空，则使用子类重写的基础地址
        if self._base_url!="":
            self._driver.get(self._base_url)

    def find(self, by, locater):
        '''
        通过显示等待15秒，直到元素显示出来，查找元素并且返回，假如超时的话，返回指定元素没有找到的字符串
        :param by:查找元素的方法类型
        :param locater: 元素定位的表达式
        :return: 返回查找的具体元素
        '''
        try:
            WebDriverWait(self._driver, 15).until(expected_conditions.presence_of_element_located(
                (by, locater)))
            return self._driver.find_element(by, locater)
        except TimeoutException:
            print(f'对应的元素没有找到{locater}')

    def finds(self, by, locater):
        '''
               通过显示等待15秒，直到元素显示出来，查找元素的列表并且返回，假如超时的话，返回指定元素没有找到的字符串
               :param by:查找元素的方法类型
               :param locater: 元素定位的表达式
               :return: 返回查找的具体元素
        '''
        try:
            WebDriverWait(self._driver, 15).until(expected_conditions.presence_of_element_located(
                (by, locater)))
            return self._driver.find_elements(by, locater)
        except TimeoutException:
            print(f'对应的元素没有找到{locater}')
