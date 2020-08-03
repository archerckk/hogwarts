from api_hw2.api.base_api import BaseApi


class Tag(BaseApi):

    def tag_add(self, tagname, token):
        req = {
            'method': 'post',
            'url': f'https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}',
            'json': {
                'tagname': tagname
            }
        }
        res = self.send_request(req)
        return res.json()

    def tag_update(self, tagid, tagname, token):
        req = {
            'method': 'post',
            'url': f'https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}',
            'json': {
                'tagid': tagid,
                'tagname': tagname
            }
        }
        res=self.send_request(req)
        return res.json()

    def tag_delete(self,tagid, token):
        req = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/tag/delete',
            'params': {
                'tagid': tagid,
                'access_token': token
            }
        }
        res=self.send_request(req)
        return res.json()

    def tag_get(self,tagid,token):
        req = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/tag/get',
            'params': {
                'tagid': tagid,
                'access_token': token
            }
        }

        res=self.send_request(req)
        return res.json()

    def tag_list_get(self,token):
        req = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/tag/list',
            'params': {
                'access_token': token
            }
        }
        res = self.send_request(req)
        return res.json()