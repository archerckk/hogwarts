from time import sleep

import pytest
import requests
from pprint import pprint

test_resut = 'test'


# @pytest.fixture(scope='function')
# def login():
#     print('执行登录')

# @pytest.mark.usefixtures('prepare')
class TestApiDemo:
    host = 'http://httpbin.testing-studio.com/'

    def setup_class(self):
        print('执行了class方法')

    def setup(self):
        print('执行了setup')

    def teardown(self):
        print('执行了teardown')

    def teardown_class(self):
        print('执行了类teardown方法')

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('a',['value1','value2'],ids=['参数1','参数2'])
    def test_get(self,a):
        payload = {"key1": a, "key2": "value2"}
        r = requests.get(f'{self.host}/get', params=payload)
        pprint(r.json())
        test_resut = 'test2'

    @pytest.mark.skipif(test_resut == 'test', reason='测试结果是test，所以不执行')
    def test_post_form(self):
        payload = {"key1": "value1", "key2": "value2"}

        r = requests.post(f"{self.host}/post", data=payload)
        pprint(r.json())

    @pytest.mark.dependency(name='upload')
    @pytest.mark.run(order=4)
    def test_file_upload(self):
        files = {'file': open('phone.yml', 'rb')}
        r = requests.post(f"{self.host}/post", files=files)
        sleep(5)
        pprint(r.raw.read())

    # @pytest.mark.flaky(reruns=2,reruns_delay=2)
    def test_post_json(self):
        payload = {"some": "data"}
        r = requests.post(f"{self.host}/post", json=payload)
        pprint(r.json())
        assert 1==2

    @pytest.mark.dependency(depends=['upload','order'])
    def test_post_xml(self):
        xml = """<?xml version='10.0' encoding='utf-8'><a>test</a>"""
        headers = {'Content-Type': 'application/xml'}
        r = requests.post(f"{self.host}/post")
        print('测试上传代码')
        pytest.assume(1==2)
        pytest.assume(1==1)
        print('继续执行下方断言1')
        pytest.assume(1==2)
        pytest.assume(1==1)
        print('继续执行下方断言2')

    @pytest.mark.dependency(name='order')
    @pytest.mark.run(order=2)
    def test_ording1(self):
        print('执行111111111111')
        assert 1==2

    @pytest.mark.run(order=3)
    def test_ording2(self):
        sleep(5)
        print('执行222222222222222')

    @pytest.mark.run(order=1)
    def test_ording3(self):
        print('执行33333333333333')