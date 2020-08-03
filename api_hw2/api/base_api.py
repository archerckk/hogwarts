import requests


class BaseApi:

    def send_request(self,req:dict):
        return requests.request(**req)