import pytest
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


def get_data():
    with open('member_data.yml', encoding='UTF-8')as f:
        datas = yaml.safe_load(f)
    return datas


class TestWeWork:

    def setup(self):
        with open('phone.yml')as f:
            desired_caps = yaml.safe_load(f)['mumu_wework']
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def find(self, *by):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(*by))

    def finds(self, *by):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located(*by))

    @pytest.mark.parametrize('name,gender,phone', get_data())
    def test_add_member(self, name, gender, phone):
        self.driver.find_element_by_xpath('//*[@class="android.widget.LinearLayout"]//*[@text="通讯录"]').click()
        self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
        self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        self.driver.find_element_by_xpath('//*[@text="姓名　"]/../android.widget.EditText[@text="必填"]').send_keys(name)
        self.driver.find_element_by_xpath('//*[@text="性别"]/..//android.widget.LinearLayout').click()

        # 稳定点击弹出的男女选择框页面，添加显示等待
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located(
            (By.XPATH, '//*[contains(@text,"男")or contains(@text,"女")]')))
        if gender == '男':
            self.driver.find_element_by_xpath('//*[@text="男"]').click()
        else:
            self.driver.find_element_by_xpath('//*[@text="女"]').click()

        self.driver.find_element_by_xpath('//*[@text="手机号"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@text="保存"]').click()

        # 获取添加用户成功的toast
        add_toast_info = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text

        assert add_toast_info == '添加成功'

    @pytest.mark.parametrize('name,gender,phone', get_data())
    def test_del_member(self, name, gender, phone):
        self.driver.find_element_by_xpath('//*[@class="android.widget.LinearLayout"]//*[@text="通讯录"]').click()
        self.driver.find_elements_by_xpath('//android.widget.LinearLayout//android.widget.RelativeLayout'
                                           '//android.widget.TextView')[2].click()
        # 跳转页面之后等元素稳定再进行查找元素
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_all_elements_located(
                (By.XPATH, '//android.widget.ListView/android.widget.RelativeLayout')))

        print("删除的目标用户为：", name)
        cur_username_list = self.driver.find_elements(By.XPATH,
                                                      f'//*[@text="{name}"]')
        # 在数据已被删除的情况，不进行删除操作
        if len(cur_username_list) == 0:
            print('目标用户不在当前用户列表当中')
        else:
            cur_username_list[0].click()
            self.find((By.XPATH, '//*[@text="删除成员"]')).click()
            self.find((By.XPATH, '//*[@text="确定"]')).click()

            return_to_member_list_loc = (
                By.XPATH, "//android.widget.ListView/android.widget.RelativeLayout//android.widget.TextView")

            # 跳转页面之后等元素稳定再进行查找元素
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_all_elements_located(return_to_member_list_loc))

            # 获取现在的所有用户的名字
            new_member_name_list = [name_element.text for name_element in self.finds(return_to_member_list_loc)]

            print('现在的用户列表为：', new_member_name_list)

            assert name not in new_member_name_list
