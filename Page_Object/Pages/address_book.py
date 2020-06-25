from selenium.webdriver.common.by import By

from Page_Object.Pages.base_page import Base_Page


class Address_Book(Base_Page):

    def import_address_book_file(self):
        self.find(By.ID, 'js_upload_file_input').send_keys('J:\Ar_hogwarts\Page_Object\data\contract.xlsx')
        judge_text = self.find(By.XPATH, '//*[@id="js_upload_file_input"]/../label').text

        return judge_text
