from selenium.webdriver.common.by import By
from appium_hw2.pages.add_member_method_page import AddMemberMethodPage
from appium_hw2.pages.base_page import BasePage
from appium_hw2.pages.manage_contact_page import ManageContactPage


class ContactPage(BasePage):
    _add_member_loc = (By.XPATH, '//*[@text="添加成员"]')
    _go_to_manage_contact_loc = (
    By.XPATH, '//android.widget.LinearLayout//android.widget.RelativeLayout/android.widget.TextView')

    def add_member(self):
        self._find_and_click(*self._add_member_loc)

        return AddMemberMethodPage(self._driver)

    def go_to_manage_contact(self):
        self._driver.find_elements(*self._go_to_manage_contact_loc)[2].click()
        return ManageContactPage(self._driver)
