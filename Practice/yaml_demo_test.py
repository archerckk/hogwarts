import pytest
import yaml


@pytest.mark.parametrize('env', yaml.safe_load(open('./data.yml')))
def test_ymal_demo(env):
    if 'test' in env:
        print('现在是测试环境')
        print(f'环境的IP地址为：{env["test"]}')
    elif 'dev' in env:
        print('现在是开发环境')
        print(f'环境的IP地址为：{env["dev"]}')


print(yaml.safe_load(open('./data.yml')))
