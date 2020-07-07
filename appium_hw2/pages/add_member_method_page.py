from selenium.webdriver.common.by import By

from appium_hw2.pages.base_page import BasePage


class AddMemberMethodPage(BasePage):
    _manual_add_loc = (By.XPATH, '//*[@text="手动输入添加"]')

    def manual_add(self):
        from appium_hw2.pages.edit_info_page import EditInfoPage

        self.find_and_click(*self._manual_add_loc)

        return EditInfoPage(self._driver)

    def get_add_success_toast(self):
        return self.get_toast()
