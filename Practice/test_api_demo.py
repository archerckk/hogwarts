import requests
import pprint


class TestApiDemo:
    host = 'http://httpbin.testing-studio.com/'

    def test_get(self):
        payload = {"key1": "value1", "key2": "value2"}
        r = requests.get(f'{self.host}/get', params=payload)
        pprint.pprint(r.json())

    def test_post_form(self):
        payload = {"key1": "value1", "key2": "value2"}

        r = requests.post(f"{self.host}/post", data=payload)
        pprint.pprint(r.json())
