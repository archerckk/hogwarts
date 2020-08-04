import json

import pytest
from api_hw2.api.tag import Tag
from api_hw2.api.wework import WeWork
from filelock import FileLock


def produce_expensive_data():
    '生成token的函数'
    we_work = WeWork()
    token = we_work.get_token()
    return token


class TestTag:
    @pytest.fixture(scope='session')
    def token(self, tmp_path_factory, worker_id):
        # 假如是单线程运行的话直接返回token
        if not worker_id:
            return produce_expensive_data()

        # 多线程运行先生成一个临时的路径
        root_tmp_dir = tmp_path_factory.getbasetemp().parent

        fn = root_tmp_dir / "data.json"
        with FileLock(str(fn) + ".lock"):
            if fn.is_file():
                #第二次获取的时候读取文件里面的内容
                data = json.loads(fn.read_text())
            else:
                #第一次获取的时候读取函数返回的数据并且写入临时存放的文件路径
                data = produce_expensive_data()
                fn.write_text(json.dumps(data))
        return data


    def setup(self):
        self.tag=Tag()

    @pytest.mark.parametrize('tagname', ['tagx11', 'taxg21', 'taxg31'])
    def test_tag_add(self, tagname, token):
        res = self.tag.tag_add(tagname, token)
        assert res['errmsg']=='created'

    def test_tag_get(self, token):
        res = self.tag.tag_get(2, token)
        print(res)
        assert res['errmsg'] == 'ok'
        assert res['tagname'] is not None

    def test_tag_update(self, token):
        res = self.tag.tag_update(1, 'test_xx', token)
        assert res['errmsg'] == 'updated'

    def test_tag_delete(self, token):
        res = self.tag.tag_delete(1, token)
        assert res['errmsg'] == 'deleted'

    @pytest.mark.parametrize('tagname', ['tagx11', 'taxg21', 'taxg31'])
    def test_all(self, tagname, token):
        #新增一个tag
        try :
            res = self.tag.tag_add(tagname, token)
            assert res['errmsg'] == 'created'
            self.tagid = res['tagid']
        except Exception as e:
            if '40071' in e.__str__():
                res = self.tag.tag_list_get(token)
                for i in res['taglist']:
                    if tagname in i.values():
                        self.tagid = i['tagid']
                        self.tag.tag_delete(self.tagid, token)
                res = self.tag.tag_add(tagname, token)
                assert res['errmsg'] == 'created'

        # 查询这个tag是否创建成功
        res = self.tag.tag_get(self.tagid, token)
        assert res['errmsg'] == 'ok'
        assert res['tagname'] == tagname
        #升级这个tag
        res = self.tag.tag_update(self.tagid, tagname + '1', token)
        assert res['errmsg'] == 'updated'
        # 查询tag是否升级成功
        res = self.tag.tag_get(self.tagid, token)
        assert res['errmsg'] == 'ok'
        #删除这个tag
        res = self.tag.tag_delete(self.tagid, token)
        assert res['errmsg'] == 'deleted'
        # 查询tag是否删除成功
        res = self.tag.tag_get(self.tagid, token)
        assert res['userlist'] == []
