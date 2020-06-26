import pytest


@pytest.fixture()
def prepare():
    print('开始计算')
    yield '调用fixture'
    print('计算结束')
