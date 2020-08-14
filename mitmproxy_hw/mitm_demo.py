import os
import sys
from mitmproxy import http

# from test_mitmproxy2.template import Template

addon_dir = os.path.dirname(__file__)
sys.path.append(addon_dir)
print(addon_dir)

import os

import pystache


class Template:
    @classmethod
    def render(cls, path, dict):
        render = pystache.Renderer(escape=lambda u: u)  # 完全禁用转义符
        print(os.path.abspath(os.getcwd()))
        with open(path) as f:
            content = f.read() #读取模板内容
            parsed = pystache.parse(content) #将模板内容转换成为模板对象
            result = render.render(parsed, dict) #模板对象还有字典内容整合起来
            return result


def response(flow: http.HTTPFlow):
    method = flow.request.method
    print("测试方法打印：", method.__repr__())
    url = flow.request.pretty_url.split('?')[0]
    print('=' * 80)
    print(flow.request.query.fields)
    print('=' * 80)
    params = [{k: v} for k, v in flow.request.query.fields]
    cookies = [{k: v} for k, v in flow.request.cookies.fields]
    data = {
        "method": method.__repr__(),
        "url": url.__repr__(),
        "params": params,
        "cookies": cookies
    }
    # content=Template.render(addon_dir+"/test.mustache", data)
    # # print("测试代码：",content)
    # with open(r'D:\Hogwarts\mitmproxy_hw\test.py','w')as f:
    #     f.write(content)
