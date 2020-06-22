# from time import sleep
from selenium import webdriver
import os
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Test_cookie:

    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    def teardown(self):
        self.driver.quit()

    def take_cookies(self):
        #重新获取cookie时的调试代码
        # sleep(20)

        self.cookies = self.driver.get_cookies()

        #json文件不存在的是时候需要新建，存在的时候的时候读取本地文件
        if not os.path.exists('./data/cookies.json'):
            with open('./data/cookies.json', 'w')as f:
                json.dump(self.cookies, f)
                print('执行新建cookie的json文件')
        else:
            with open('data/cookies.json')as f:
                print('json文件已存在，执行读取cookies')
                self.cookies = json.load(f)

        return self.cookies

    def test_click_contract(self):

        #获取浏览器cookies
        cookies=self.take_cookies()

        for cookie in cookies:
            #处理每个cookie里面是否包含expiry属性
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        element_index_loc=(By.ID,'menu_index')
        element_contract_loc=(By.XPATH,'//*[@class="index_service_cnt js_service_list"]//a[2]')
        element_upload_file_loc=(By.ID,'js_upload_file_input')
        element_judge_upload_info_text_loc=(By.XPATH,'//*[@id="js_upload_file_input"]/../label')

        #持续刷新逻辑
        while True:
            self.driver.refresh()
            result=WebDriverWait(self.driver,15).until(ec.presence_of_element_located(element_index_loc))
            if result:
                break
        #点击通讯录
        WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable(element_contract_loc)).click()
        #上传文件
        WebDriverWait(self.driver, 15).until(ec.presence_of_element_located(element_upload_file_loc)
                                             ).send_keys(r'G:\PyTest\Hogworts\selenium_test\data\test.xlsx')
        #获取上传成功的断言文案
        judge_upload_info_text=WebDriverWait(self.driver, 15).until(ec.presence_of_element_located(
            element_judge_upload_info_text_loc)).text
        # judge_upload_info_text=self.driver.find_element(By.XPATH,'//*[@id="js_upload_file_input"]/../label').text
        assert judge_upload_info_text=='重新上传'
        # sleep(10000)#调试代码
