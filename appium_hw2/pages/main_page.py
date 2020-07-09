from selenium.webdriver.common.by import By

from appium_hw2.pages.base_page import BasePage
from appium_hw2.pages.contact_page import ContactPage


class MainPage(BasePage):
    _contact_tab_loc = (By.XPATH, '//*[@class="android.widget.LinearLayout"]//*[@text="通讯录"]')

    def goto_contacts(self):
        self._find_and_click(*self._contact_tab_loc)
        return ContactPage(self._driver)
