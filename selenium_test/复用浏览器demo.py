from selenium.webdriver.chrome.options import Options
from selenium import webdriver

class Test_repeat:

    def test_login(self):
        #实例化谷歌参数
        option=Options()
        #配置测试地址
        option.debugger_address='localhost:9222'
        #实例化的参数传入谷歌浏览器驱动里面
        driver=webdriver.Chrome(options=option)
        #打开已经进入进入过的网页
        driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
