import pytest
import yaml

from pytest_hw.calculator import Calculator


class Test_Calculator:
    def setup_class(self):
        self.cal = Calculator()

    @pytest.mark.story('测试')
    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('test_data.yml', encoding='UTF-8'))['add'])
    def test_add(self, a, b, c, prepare):
        assert c == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('test_data.yml', encoding='UTF-8'))['sub'])
    def test_sub(self, a, b, c, prepare):
        assert c == self.cal.sub(a, b)

    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('test_data.yml', encoding='UTF-8'))['mul'])
    def test_mul(self, a, b, c, prepare):
        assert c == self.cal.mul(a, b)

    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open('test_data.yml', encoding='UTF-8'))['div'])
    def test_div(self, a, b, c, prepare):
        assert c == self.cal.div(a, b)


if __name__ == '__main__':
    print(yaml.safe_load(open('test_data.yml')))
