import json
import os
from time import sleep

from Page_Object.Pages.base_page import Base_Page
from Page_Object.Pages.index import Index
from Page_Object.Pages.register import Register
from selenium.webdriver.common.by import By


class Login(Base_Page):

    def take_cookies(self):
        # 重新获取cookie时的调试代码
        # sleep(20)

        self.cookies = self._driver.get_cookies()

        # json文件不存在的是时候需要新建，存在的时候的时候读取本地文件
        if not os.path.exists('../data/cookies.json'):
            with open('../data/cookies.json', 'w')as f:
                json.dump(self.cookies, f)
                print('执行新建cookie的json文件')
        else:
            with open('../data/cookies.json')as f:
                print('json文件已存在，执行读取cookies')
                self.cookies = json.load(f)

        return self.cookies

    def scan(self):
        # 调用获取cookie方法
        cookies = self.take_cookies()

        for cookie in cookies:
            # 处理每个cookie里面是否包含expiry属性
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self._driver.add_cookie(cookie)

        # 持续刷新页面
        while True:
            self._driver.refresh()
            result = self.find(By.ID, 'menu_index')
            if result:
                break

        # 调试用测试代码
        # sleep(1000000)

        return Index(self._driver)
    def goto_register(self):
        self.find(By.CSS_SELECTOR,'.login_registerBar_link').click()

        return Register(self._driver)

    def judge_login_jump_success(self):
        result = self.finds(By.CSS_SELECTOR, '.login_stage_title_text')

        if result == []:
            return False
        else:
            return True