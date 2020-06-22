from Page_Object.Pages.base_page import Base_Page
from Page_Object.Pages.register import Register
from selenium.webdriver.common.by import By


class Login(Base_Page):

    def scan(self):
        pass

    def goto_register(self):
        self.find(By.CSS_SELECTOR,'.login_registerBar_link').click()

        return Register(self._driver)

    def judge_login_jump_success(self):
        result = self.finds(By.CSS_SELECTOR, '.login_stage_title_text')

        if result == []:
            return False
        else:
            return True