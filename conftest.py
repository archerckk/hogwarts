import pytest
import yaml


@pytest.fixture()
def prepare():
    print('开始计算')
    yield '调用fixture'
    print('计算结束')


# 注册一个env参数
def pytest_addoption(parser):
    mygroup = parser.getgroup('hogwarts')  # 先获取一个组名
    mygroup.addoption(
        "--env",  # 注册一个参数
        default='test',  # 默认参数为test
        dest='dev',
        help='check function info'
    )


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')

    if myenv == 'test':
        print('获取到测试环境数据')
        with open('./env_data/test/test_env.yml')as f:
            datas = yaml.safe_load(f)
    elif myenv == 'dev':
        print('获取到开发环境数据')
        with open('./env_data/dev/dev_env.yml')as f:
            datas = yaml.safe_load(f)
    elif myenv == 'st':
        print('获取到线上环境数据')
        with open('./env_data/st/st_env.yml')as f:
            datas = yaml.safe_load(f)

    return datas
