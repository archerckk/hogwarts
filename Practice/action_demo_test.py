from time import sleep

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@allure.feature('自动化测试demo')
class Test_demo:
    def setup(self):
        # 解决w3c错误的额外参数
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(chrome_options=opt)

        self.driver.implicitly_wait(5)
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
        drop_element_list = self.driver.find_elements(By.CSS_SELECTOR, '.item')
        action.drag_and_drop(drag_element, drop_element_list[0]).pause(1)
        action.click_and_hold(drag_element).release(drop_element_list[1]).pause(1)
        action.click_and_hold(drag_element).move_to_element(drop_element_list[2]).release().pause(1)
        action.drag_and_drop(drag_element, drop_element_list[3]).pause(1)

        action.perform()
        sleep(3)

    def test_key_ctrl(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        action = ActionChains(self.driver)
        input1 = self.driver.find_element(By.CSS_SELECTOR, "[type=textbox]")
        input2 = self.driver.find_element(By.CSS_SELECTOR, "tbody td:nth-child(2)")

        # action.send_keys_to_element(input1,'test_user33333')
        # action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).pause(1)
        # action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).pause(1)
        #
        sleep(5)
        input2.click()  # 切换输入框失败
        # action.move_to_element(input2).click()#切换输入框成功
        # action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).pause(1)
        action.send_keys_to_element(input2, 'testeset')
        action.perform()
        sleep(2)

    def test_touchaction_scroll(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element(By.ID, 'kw').send_keys('selenium test')
        touch_action = TouchActions(self.driver)
        touch_action.tap(self.driver.find_element(By.ID, 'su'))  # 有ID的元素才可以点击成功

        touch_action.scroll_from_element(on_element=self.driver.find_element(By.ID, 'su'),
                                         xoffset=10, yoffset=3000).perform()
        self.driver.find_element(By.CSS_SELECTOR, '#page a:nth-last-child(1)').click()  # 可以点击成功
        sleep(3)

    def test_windows_switch(self):
        self.driver.get('https://zhidao.baidu.com/question/201422003213420205.html')
        sleep(2)

        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.ID, "userbar-reg"))).click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('test_user888888')
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys(13631347763)
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('test_psw')
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element_by_id('userbar-login').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('test_user888888')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('test_psw')

        sleep(3)

    def test_frame_switch(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        action = ActionChains(self.driver)
        element_drag = self.driver.find_element_by_id('draggable')
        element_drop = self.driver.find_element_by_id('droppable')
        action.drag_and_drop(element_drag, element_drop).pause(1)
        action.perform()
        # print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()

        sleep(1)
        self.driver.switch_to.frame('iframeResult')
        assert self.driver.find_element_by_id('draggable').text == '请拖拽我！'

    @allure.story('JS滑动点击')
    def test_js_scroll(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element(By.ID, 'kw').send_keys('selenium test')
        # self.driver.find_element_by_id('su').click()
        self.driver.execute_script("document.getElementById('su').click()")
        self.driver.execute_script("document.documentElement.scrollTop=2000")
        self.driver.find_element(By.CSS_SELECTOR, '#page a:nth-last-child(1)').click()  # 可以点击成功
        sleep(3)
        for code in ['return JSON.stringify(performance.timing)', 'return document.title']:
            print(self.driver.execute_script(code))
        # print(self.driver.execute_script('return document.title'))

    @allure.story('测试12306的时间修改')
    def test_time_value(self):
        self.driver.get('https://www.12306.cn/index/')
        self.driver.execute_script("document.getElementById('train_date').removeAttribute('readonly')")
        sleep(2)
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(2)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        # print(self.driver.find_element_by_id('train_date').text)
        sleep(3)


if __name__ == '__main__':
    pytest.main()
