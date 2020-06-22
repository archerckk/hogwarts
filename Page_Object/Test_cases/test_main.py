from Page_Object.Pages.main import Main



class Test_main:

    def setup(self):
        self.main=Main()

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