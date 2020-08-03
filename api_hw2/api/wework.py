from api_hw2.api.base_api import BaseApi


class WeWork(BaseApi):

    def get_token(self):
        req = {
            'method':'get',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'params':{
                "corpid": "ww5df43357194e9ba6",
                "corpsecret": "NUZ-NHi5wvrgYNp9NgnTbBezimNV5sBiWqxs3KdNLgk"
            }
        }
        res = self.send_request(req)
        return res.json()['access_token']
