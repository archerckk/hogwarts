import requests
from pprint import pprint


class TestApiDemo:
    host = 'http://httpbin.testing-studio.com/'

    def test_get(self):
        payload = {"key1": "value1", "key2": "value2"}
        r = requests.get(f'{self.host}/get', params=payload)
        pprint(r.json())

    def test_post_form(self):
        payload = {"key1": "value1", "key2": "value2"}

        r = requests.post(f"{self.host}/post", data=payload)
        pprint(r.json())

    def test_file_upload(self):
        files={'file':open('phone.yml','rb')}
        r=requests.post(f"{self.host}/post",files=files)
        pprint(r.raw.read())

    def test_post_json(self):
        payload = {"some": "data"}
        r = requests.post(f"{self.host}/post", json=payload)
        pprint(r.json())

    def test_post_xml(self):
        xml="""<?xml version='10.0' encoding='utf-8'><a>test</a>"""
        headers={'Content-Type':'application/xml'}
        r=requests.post(f"{self.host}/post")
