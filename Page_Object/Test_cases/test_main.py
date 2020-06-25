from time import sleep

from Page_Object.Pages.main import Main



class Test_main:

    def setup(self):
        self.main=Main()

    def teardown(self):
        self.main._driver.quit()

    def test_main_login_click(self):
        assert self.main.goto_login().judge_login_jump_success()==True

    def test_main_register_click_success(self):
        assert  self.main.goto_register().judge_register_jump_success()==True

    def test_register_info_form(self):
        # result=self.main.goto_register().register()
        # assert 'test_name','test_manager'==result
        assert ('test_name','test_manager')==self.main.goto_register().register()
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

        # 断言已删除用户不在新的名字列表信息里面
        assert result[0] not in result[1]

    # 测试通讯录上传文件成功
    def test_upload_file_success(self):
        result = self.main.goto_login().scan().go_to_address_book().import_address_book_file()
        print(result)
        assert result == '重新上传'
