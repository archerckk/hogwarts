from Page_Object.Pages.base_page import Base_Page
from Page_Object.Pages.login import Login
from Page_Object.Pages.register import Register
from selenium.webdriver.common.by import By


class Main(Base_Page):
    _base_url='https://work.weixin.qq.com/'

    def goto_register(self):
        self.find(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return Login(self._driver)
