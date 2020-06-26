import pytest
import yaml

from pytest_hw.calculator import Calculator


def get_datas():
    with open('test_data.yml', encoding='UTF-8')as f:
        datas = yaml.safe_load(f)
        return datas


class Test_Calculator:
    def setup_class(self):
        self.cal = Calculator()
        self.datas = get_datas()

    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='add')
    @pytest.mark.parametrize('a,b,c', get_datas()['add'])
    @pytest.mark.add
    def check_add(self, a, b, c, prepare, cmdoption):
        '''加法测试用例'''
        print(f'{cmdoption}')
        assert c == self.cal.add(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name='mul')
    @pytest.mark.parametrize('a,b,c', get_datas()['mul'])
    def test_mul(self, a, b, c, prepare, cmdoption):
        '''乘法测试用例'''
        print(f'{cmdoption}')
        assert c == self.cal.mul(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=['mul'])
    @pytest.mark.parametrize('a,b,c', get_datas()['div'])
    def test_div(self, a, b, c, prepare, cmdoption):
        '''除法测试用例'''
        print(f'{cmdoption}')
        assert c == self.cal.div(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=['add'])
    @pytest.mark.parametrize('a,b,c', get_datas()['sub'])
    def test_sub(self, a, b, c, prepare, cmdoption):
        '''减法测试用例'''
        print(f'{cmdoption}')
        assert c == self.cal.sub(a, b)


if __name__ == '__main__':
    print(yaml.safe_load(open('test_data.yml')))
