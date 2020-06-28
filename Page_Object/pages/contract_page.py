from time import sleep

from selenium.webdriver.common.by import By

from Page_Object.pages.base_page import BasePage


class ContractPage(BasePage):

    # def add_member(self):

    def del_member(self):
        check_box_list = self._finds(By.CSS_SELECTOR, '#member_list tr td>input[class="ww_checkbox"]')
        name_list = [name.text for name in self._finds(By.CSS_SELECTOR, '#member_list tr td:nth-child(2)')]
        del_icon = self._finds(By.CSS_SELECTOR, "a[class='qui_btn ww_btn js_delete']")[0]

        # length=len(check_box_list)

        # 点击需要删除的用户的选中框，现选择第二个用户进行删除，第一个用户无法删除
        check_box_list[1].click()
        sleep(1)
        target_name = name_list[1]
        print(f'需要删除的用户信息为：{target_name}')
        # 点击删除按钮
        del_icon.click()
        sleep(1)
        # 点击确认删除的确定按钮
        self._find(By.CSS_SELECTOR, 'a[class="qui_btn ww_btn ww_btn_Blue"]').click()
        sleep(1)
        # 获取到新的所有用户信息名字列表
        new_name_list = [name.text for name in self._finds(By.CSS_SELECTOR, '#member_list tr td:nth-child(2)')]
        print(new_name_list)
        # sleep(200)
        # 断言删除的用户不在新获取的用户列表信息里面
        return target_name, new_name_list
        # confirm_delete=self._driver.find(By.CSS_SELECTOR,'a[class="qui_btn ww_btn ww_btn_Blue"]')
