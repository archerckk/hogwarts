from time import sleep
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
1、编写添加联系人测试用例
2、编写删除联系人测试用例

注意：

注意setup_class,setup, teardown, teardown_class 灵活使用
将测试数据保存在yaml文件里面读取出来
添加联系人与删除联系人共有一份测试数据文件

"""


class TestWeWork:

    def setup(self):
        with open('phone.yml')as f:
            desired_caps = yaml.safe_load(f)['mumu_wework']
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_add_member(self):
        self.driver.find_element_by_xpath('//*[@class="android.widget.LinearLayout"]//*[@text="通讯录"]').click()
        self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
        self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        self.driver.find_element_by_xpath('//*[@text="姓名　"]/../android.widget.EditText[@text="必填"]').send_keys('xf_001')
        self.driver.find_element_by_xpath('//*[@text="性别"]/..//android.widget.LinearLayout').click()

        # print(self.driver.find_element_by_xpath('//*[@text="男"]').text)
        self.driver.find_element_by_xpath('//*[@text="女"]').click()
        self.driver.find_element_by_xpath('//*[@text="手机号"]').send_keys(13870000001)
        self.driver.find_element_by_xpath('//*[@text="保存"]').click()
        add_toast_info = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text

        assert add_toast_info == '添加成功'

    def test_del_member(self):
        self.driver.find_element_by_xpath('//*[@class="android.widget.LinearLayout"]//*[@text="通讯录"]').click()
        self.driver.find_elements_by_xpath('//android.widget.LinearLayout//android.widget.RelativeLayout'
                                           '//android.widget.TextView')[2].click()
        sleep(2)
        member_row_elements: list = self.driver.find_elements_by_xpath(
            '//android.widget.ListView/android.widget.RelativeLayout')
        member_row_elements.pop(0)
        print(member_row_elements)
        target_user_name = member_row_elements[0].find_elements_by_xpath('//android.widget.LinearLayout')[0].text
        print(target_user_name)

        member_row_elements[0].find_elements_by_xpath('//android.widget.ImageView')[1].click()
        self.driver.find_element_by_xpath('//*[@text="删除成员"]').click()
        self.driver.find_element_by_xpath('//*[@text="确定"]').click()

        return_to_member_list_loc = (By.XPATH, '//android.widget.ListView//android.widget.LinearLayout')
        WebDriverWait(self.driver, 8).until(expected_conditions.
                                            visibility_of_all_elements_located(return_to_member_list_loc))

        new_member_name_elements_list = self.driver.find_elements(return_to_member_list_loc)
        new_member_name_list = [name.text for name in new_member_name_elements_list]
        assert target_user_name not in new_member_name_list
