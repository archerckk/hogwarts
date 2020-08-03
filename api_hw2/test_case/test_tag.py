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


    def test_all(self,token):
        #新增一个tag
        try :
            res=self.tag.tag_add('tag1',token)
            assert res['errmsg'] == 'created'
        except Exception as e:
            if '40071' in e.__str__():
                print(e.__str__())
        #查询这个tag
        #升级这个tag
        #查询这个tag
        #删除这个tag
        #查询这个tag