from selenium.webdriver.common.by import By

from Page_Object.pages.address_book_page import AddressBookPage
from Page_Object.pages.base_page import BasePage
from Page_Object.pages.contract_page import ContractPage

"""

"""


class IndexPage(BasePage):

    def go_to_contract(self):
        self._find(By.CSS_SELECTOR, "#menu_contacts> span").click()
        return ContractPage(self._driver)

    def go_to_address_book(self):
        self._find(By.XPATH, '//*[@class="index_service_cnt js_service_list"]//a[21]').click()
        return AddressBookPage(self._driver)
