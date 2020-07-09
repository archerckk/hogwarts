import pytest
import yaml

from appium_hw2.pages.app import App

with open('../datas/datas.yml', encoding='UTF-8')as f:
    datas = yaml.safe_load(f)


class TestWework:

    def setup(self):
        self.app = App()

    def teardown(self):
        self.app.close()

    @pytest.mark.parametrize('name,gender,phone', datas)
    def test_add_member(self, name, gender, phone):
        add_success_toast = self.app.start().main().goto_contacts().add_member().manual_add() \
            .edit_name(name).edit_gender(gender).edit_phone_number(phone).save_info().get_add_success_toast()

        assert add_success_toast == '添加成功'
