import os
import sys
from mitmproxy import http
import yaml
# from test_mitmproxy2.template import Template

addon_dir = os.path.dirname(__file__)
sys.path.append(addon_dir)
print(addon_dir)

import os

import pystache

def get_config_data():
    with open('D:\hogwarts\mitmproxy_hw\config.yml')as f:
        data=yaml.safe_load(f)
    return data








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
    api= flow.request.path.split('?')[0]
    tmplist=api.split('/')
    filename=''.join(tmplist)
    print(filename)


    # if api == '/api/payment/info':
    tmplist = api.split('/')
    filename = '_'.join(tmplist)
    print(filename)

    print('api为：',api)
    print("测试方法打印：", method.__repr__())
    url = flow.request.pretty_url.split('?')[0]

    data = get_config_data()['pararms_del']

    for i in data:
        print(i)

    print('=' * 200)
    print(flow.request.query.fields)
    print('=' * 200)
    params = [{k: v} for k, v in flow.request.query.fields for d in data if k not in d and k.isalpha()==True ]
    # cookies = [{k: v} for k, v in flow.request.cookies.fields]

    print('params实际内容为：',params)
    data = {
        "api": api,
        "method": method.__repr__(),
        "params": params,
    }

    content=Template.render(addon_dir+"/get.mustache", data)
    print("测试代码：",content)
    with open(r'D:\Hogwarts\mitmproxy_hw\api_generated\%s_api.yml'%(filename),'w')as f:
        f.write(content)
