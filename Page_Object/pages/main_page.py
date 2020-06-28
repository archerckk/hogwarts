from Page_Object.pages.base_page import BasePage
from Page_Object.pages.login_page import LoginPage
from Page_Object.pages.register_page import RegisterPage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    _base_url='https://work.weixin.qq.com/'

    def goto_register(self):
        self._find(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return RegisterPage(self._driver)

    def goto_login(self):
        self._find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return LoginPage(self._driver)
