from Page_Object.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):

    def register(self):
        ele_corp_name = self._find(By.ID, 'corp_name')
        ele_corp_name.send_keys('test_name')
        ele_manager_name = self._find(By.ID, 'manager_name')
        ele_manager_name.send_keys('test_manager')
        print(ele_corp_name.get_attribute('value'))
        print(ele_manager_name.get_attribute('value'))
        return ele_corp_name.get_attribute('value'),ele_manager_name.get_attribute('value')


    def judge_register_jump_success(self):
        register_page_title_list = self._finds(By.CSS_SELECTOR, '.register_simple_header_title')

        if register_page_title_list == []:
            return False
        else:
            return True