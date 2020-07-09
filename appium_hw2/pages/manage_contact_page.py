from selenium.webdriver.common.by import By

from appium_hw2.pages.base_page import BasePage


class ManageContactPage(BasePage):
    _wait_element_loc = (By.XPATH, '//android.widget.ListView/android.widget.RelativeLayout')
    _del_member_icon_loc = (By.XPATH, '//*[@text="删除成员"]')
    _del_member_confirm_loc = (By.XPATH, '//*[@text="确定"]')

    def del_member(self, name):
        # 让页面稳定在进行查找
        self._finds(self._wait_element_loc)

        edit_member = (By.XPATH, f'//*[@text="{name}"]')
        if len(self._finds(edit_member)) == 0:
            return '删除的目标用户不在列表当中'
        else:
            self._find_and_click(edit_member)
            self._find_and_click(self._del_member_icon_loc)
            self._find_and_click(self._del_member_confirm_loc)
            result = self.confirm_element_disappear(edit_member)

            return result
