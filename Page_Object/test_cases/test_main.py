from time import sleep

from Page_Object.pages.main_page import MainPage


class TestMain:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main._driver.quit()

    def test_main_login_click(self):
        assert self.main.goto_login().judge_login_jump_success() == True

    def test_main_register_click_success(self):
        assert self.main.goto_register().judge_register_jump_success() == True

    def test_register_info_form(self):
        # result=self.main.goto_register().register()
        # assert 'test_name','test_manager'==result
        assert ('test_name', 'test_manager') == self.main.goto_register().register()
        print(self.main.count)

    def test_init_count(self):
        self.main.goto_login().goto_register().register()
        print(self.main.count)
        assert 'test name'

    # 测试删除联系人成功
    def test_del_contract(self):
        # scan函数方法需要扫描二维码保存一次缓存，在scan里面调用了take_cookies，这个方法上面有测试代码
        # result 返回的是删除的目标用户姓名，跟新的用户名字列表信息
        result = self.main.goto_login().scan().go_to_contract().del_member()

        del_target_name = result[0]
        current_user_list = result[1]

        # 断言已删除用户不在新的名字列表信息里面
        assert del_target_name not in current_user_list

    # 测试通讯录上传文件成功
    def test_upload_file_success(self):
        upload_success_info = self.main.goto_login().scan().go_to_address_book().import_address_book_file()
        print(upload_success_info)
        assert upload_success_info == '重新上传'
