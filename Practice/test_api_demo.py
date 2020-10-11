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

    def setup(self):
        print('执行了setup')

    def teardown(self):
        print('执行了teardown')

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

    def test_file_upload(self):
        files = {'file': open('phone.yml', 'rb')}
        r = requests.post(f"{self.host}/post", files=files)
        pprint(r.raw.read())

    def test_post_json(self):
        payload = {"some": "data"}
        r = requests.post(f"{self.host}/post", json=payload)
        pprint(r.json())

    def test_post_xml(self):
        xml = """<?xml version='10.0' encoding='utf-8'><a>test</a>"""
        headers = {'Content-Type': 'application/xml'}
        r = requests.post(f"{self.host}/post")
        print('测试上传代码')
