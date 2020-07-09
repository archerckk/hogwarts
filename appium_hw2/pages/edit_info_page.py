from selenium.webdriver.common.by import By

from appium_hw2.pages.base_page import BasePage


class EditInfoPage(BasePage):
    _name_loc = (By.XPATH, '//*[@text="姓名　"]/../android.widget.EditText[@text="必填"]')
    _gender_loc = (By.XPATH, '//*[@text="性别"]/..//android.widget.LinearLayout')
    _gender_man_loc = (By.XPATH, '//*[@text="男"]')
    _gender_female_loc = (By.XPATH, '//*[@text="女"]')
    _edit_phone_number_loc = (By.XPATH, '//*[@text="手机号"]')
    _save_info_loc = (By.XPATH, '//*[@text="保存"]')

    def edit_name(self, name):
        self._find(*self._name_loc).send_keys(name)
        return self

    def edit_gender(self, gender):
        self._find_and_click(*self._gender_loc)
        if gender == '男':
            self._find_and_click(*self._gender_man_loc)
        else:
            self._find_and_click(*self._gender_female_loc)
        return self

    def edit_phone_number(self, phone):
        self._find(*self._edit_phone_number_loc).send_keys(phone)
        return self

    def save_info(self):
        from appium_hw2.pages.add_member_method_page import AddMemberMethodPage
        self._find_and_click(*self._save_info_loc)
        return AddMemberMethodPage(self._driver)
