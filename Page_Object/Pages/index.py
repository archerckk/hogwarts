from selenium.webdriver.common.by import By

from Page_Object.Pages.address_book import Address_Book
from Page_Object.Pages.base_page import Base_Page
from Page_Object.Pages.contract import Contract

"""

"""


class Index(Base_Page):

    def go_to_contract(self):
        self.find(By.CSS_SELECTOR, "#menu_contacts> span").click()
        return Contract(self._driver)

    def go_to_address_book(self):
        self.find(By.XPATH, '//*[@class="index_service_cnt js_service_list"]//a[21]').click()
        return Address_Book(self._driver)
