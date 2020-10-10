import pytest
import yaml
from typing import List
import pytest
import yaml
from _pytest.config import Config
from _pytest.nodes import Item
from requests import Session


@pytest.fixture(scope='function')
def prepare():
    print('开始计算')
    yield '调用fixture'
    print('计算结束')



# @pytest.fixture()
# def prepare():
#     print('开始计算')
#     yield '调用fixture'
#     print('计算结束')


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """ called after collection has been performed, may filter or re-order
    the items in-place.

    :param _pytest.main.Session session: the pytest session object
    :param _pytest.config.Config config: pytest config object
    :param List[_pytest.nodes.Item] items: list of item objects
    """
    # 修复中文的ids显示问题
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')

        # 自定义添加标签
        if 'find' in item.nodeid:
            item.add_marker(pytest.mark._find)
        elif 'update' in item.nodeid:
            item.add_marker(pytest.mark.update)


def pytest_configure(config):
    # config.addinivalue_line(
    #     "markers", "find: some cases contain find "
    # )
    config.addinivalue_line(
        "markers", "update: some cases contain find"
    )



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
