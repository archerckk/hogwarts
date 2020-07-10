from selenium.webdriver.common.by import By

from appium_hw2.pages.base_page import BasePage


class ManageContactPage(BasePage):
    _del_member_icon_loc = (By.XPATH, '//*[@text="删除成员"]')
    _del_member_confirm_loc = (By.XPATH, '//*[@text="确定"]')

    def del_member(self, name):
        # 没有将弹出来的删除页面封装多一个页面，假如删除的名字不存在，不好做逻辑判断

        edit_member = (By.XPATH, f'//*[@text="{name}"]')
        edit_member_result = self._driver.find_elements(*edit_member)
        if len(edit_member_result) == 0:
            return '删除的目标用户不在列表当中'
        else:
            self._find_and_click(edit_member)
            self._find_and_click(self._del_member_icon_loc)
            self._find_and_click(self._del_member_confirm_loc)
            result = self.confirm_element_disappear(edit_member)

            return result
