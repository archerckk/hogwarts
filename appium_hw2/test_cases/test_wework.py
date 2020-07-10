from time import sleep

import pytest
import yaml

from appium_hw2.pages.app import App

with open('../datas/datas.yml', encoding='UTF-8')as f:
    datas = yaml.safe_load(f)


class TestWework:

    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()

    def teardown_class(self):
        self.app.close()

    @pytest.mark.parametrize('name,gender,phone', datas)
    def test_add_member(self, name, gender, phone):
        add_success_toast = self.main.goto_contacts().add_member().manual_add() \
            .edit_name(name).edit_gender(gender).edit_phone_number(phone).save_info().get_add_success_toast()

        assert add_success_toast == '添加成功'
        self.app.back(1)

    @pytest.mark.parametrize('name,gender,phone', datas)
    def test_del_member(self, name, gender, phone):
        result = self.main.goto_contacts().go_to_manage_contact().del_member(name)

        assert result in (True, '删除的目标用户不在列表当中')
        sleep(1)  # 解决断言过快导致back没有切回到练习人页面的问题
        self.app.back(1)
