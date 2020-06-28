from selenium.webdriver.common.by import By

from Page_Object.pages.base_page import BasePage


class AddressBookPage(BasePage):

    def import_address_book_file(self):
        self._find(By.ID, 'js_upload_file_input').send_keys('J:\Ar_hogwarts\Page_Object\data\contract.xlsx')
        judge_text = self._find(By.XPATH, '//*[@id="js_upload_file_input"]/../label').text

        return judge_text
