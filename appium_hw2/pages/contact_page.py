from selenium.webdriver.common.by import By
from appium_hw2.pages.add_member_method_page import AddMemberMethodPage
from appium_hw2.pages.base_page import BasePage


class ContactPage(BasePage):
    _add_member_loc = (By.XPATH, '//*[@text="添加成员"]')

    def add_member(self):
        self.find_and_click(*self._add_member_loc)
        return AddMemberMethodPage(self._driver)
