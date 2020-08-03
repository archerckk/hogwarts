import json

import pytest
from api_hw2.api.tag import Tag
from api_hw2.api.wework import WeWork
from filelock import FileLock


class TestTag:
    @pytest.fixture(scope='session')
    def token(self):
        with FileLock("session.lock"):
            we_work=WeWork()
            token=we_work.get_token()
        yield token

    def setup(self):
        self.tag=Tag()

    def test_tag_add(self,token):
        res=self.tag.tag_add('test_tag1',token)
        assert res['errmsg']=='created'

    def test_tag_get(self,token):
        res=self.tag.tag_get(2,token)
        assert res['errmsg'] == 'ok'
        assert res['tagname'] is not None

    def test_tag_update(self,token):
        res=self.tag.tag_update(1,'test_xx',token)
        assert res['errmsg'] == 'updated'

    def test_tag_delete(self,token):
        res = self.tag.tag_delete(1, token)
        assert res['errmsg']=='deleted'

    def test_all(self, tagname, token):
        #新增一个tag
        try :
            res=self.tag.tag_add('tag1',token)
            assert res['errmsg'] == 'created'
            self.tagid = res['tagid']
        except Exception as e:
            if '40071' in e.__str__():
                res = self.tag.tag_list_get(token)
                print(res)
                for i in res['taglist']:
                    if 'tag1' in i.values():
                        self.tagid = i['tagid']
                        self.tag.tag_delete(self.tagid, token)
                res = self.tag.tag_add('tag1', token)
                assert res['errmsg'] == 'created'

        # 查询这个tag是否创建成功
        res = self.tag.tag_get(self.tagid, token)
        assert res['errmsg'] == 'ok'
        assert res['tagname'] is not None
        #升级这个tag
        res = self.tag.tag_update(self.tagid, 'test_xxx', token)
        assert res['errmsg'] == 'updated'
        # 查询tag是否升级成功
        res = self.tag.tag_get(self.tagid, token)
        assert res['errmsg'] == 'ok'
        #删除这个tag
        res = self.tag.tag_delete(self.tagid, token)
        assert res['errmsg'] == 'deleted'
        # 查询tag是否删除成功
        res = self.tag.tag_get(self.tagid, token)
        print(res)
