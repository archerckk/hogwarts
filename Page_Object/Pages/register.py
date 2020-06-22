from Page_Object.Pages.base_page import Base_Page
from selenium.webdriver.common.by import By


class Register(Base_Page):

    def register(self):
        ele_corp_name=self.find(By.ID,'corp_name')
        ele_corp_name.send_keys('test_name')
        ele_manager_name=self.find(By.ID,'manager_name')
        ele_manager_name.send_keys('test_manager')
        print(ele_corp_name.get_attribute('value'))
        print(ele_manager_name.get_attribute('value'))
        return ele_corp_name.get_attribute('value'),ele_manager_name.get_attribute('value')



    def judge_register_jump_success(self):
        result=self.finds(By.CSS_SELECTOR,'.register_simple_header_title')

        if result==[]:
            return False
        else:
            return True