import os
import sys
from mitmproxy import http
import yaml
# from test_mitmproxy2.template import Template
import os
import json
import pystache


addon_dir = os.path.dirname(__file__)
sys.path.append(addon_dir)
print(addon_dir)
json_data = []

new_result = []


def get_config_data():
    with open(f'{addon_dir}/config.yml')as f:
        data = yaml.safe_load(f)
    return data


def json_to_str(dict_data: dict):
    if isinstance(dict_data, dict):
        for key, value in dict_data.items():
            if isinstance(value, dict):
                json_data.append(f'{key}: ')
                json_to_str(value)
            else:
                json_data.append(f"{key}: {value}")
    else:
        json_data.append(dict_data)

    return json_data


def format_list(list_data: list):
    deep = 1
    for i in list_data:
        if i[-1] == ' ' and list_data.index(i) == 0:
            new_result.append(i)
        elif i[-1] == ' ' and list_data.index(i) != 0:
            tab_str = '\t' * deep
            i = f'{tab_str}{i}'
            deep += 1
            new_result.append(i)
        elif i[-1] != ' ' and list_data[list_data.index(i) - 1][-1] == " ":
            tab_str = '\t' * deep
            i = f'{tab_str}{i}'
            deep += 1
            i = i
            print(i)
            new_result.append(i)
        else:
            new_result.append(i)

    return new_result


class Template:
    @classmethod
    def render(cls, path, dict):
        render = pystache.Renderer(escape=lambda u: u)  # 完全禁用转义符
        print(os.path.abspath(os.getcwd()))
        with open(path) as f:
            content = f.read() # 读取模板内容
            parsed = pystache.parse(content)  # 将模板内容转换成为模板对象
            result = render.render(parsed, dict)  # 模板对象还有字典内容整合起来
            return result


def response(flow: http.HTTPFlow):
    host = flow.request.host  # 获取请求域名
    method = flow.request.method  # 获取请求的方法
    api = flow.request.path.split('?')[0]  # 获取请求的接口api
    data=get_config_data()
    params_block_list = data['pararms_del']  # 获取params参数过滤列表
    api_generate_list=data['api_list'] #获取需要拦截的api列表

    # if host == 'service.vins.live':
    if api in api_generate_list:
        tmplist = api.split('/')
        filename = '_'.join(tmplist)  # 保存的文件名
        print(filename)

        print('api为：', api)
        print("请求方法打印：", method.__repr__())
        print('headers:', flow.request.headers)


        print('=' * 200)
        print(flow.request.query.fields)
        print('=' * 200)
        variables = [f"{k}: {v}" for k, v in flow.request.query.fields for d in params_block_list if
                     k not in d and k.isalpha() is True]  # 获取yaml文件的varibales参数，params不在过滤列表，并且所有都是字符构成
        params = [f"{k}: ${k}" for k, v in flow.request.query.fields for d in params_block_list if
                  k not in d and k.isalpha() is True]  # 获取请求里面的params参数

        print('variables内容为：', variables)
        print('params内容为：', params)


        if method == 'POST':
            print('data:>>>>>>>', flow.request.get_text())

            request_data = json.loads(flow.request.get_text())  # 将post请求的body参数转换为json对象

            json_data = json_to_str(request_data)
            json_data = format_list(json_data)

            print('json_data内容为：', json_data)

            params_block_list = {
                "api": api,
                "method": method.__repr__(),
                "params": params,
                "variables": variables,
                "json_data": json_data
            }

            content = Template.render(addon_dir + "/post.mustache", params_block_list)
        else:
            params_block_list = {
                "api": api,
                "method": method.__repr__(),
                "params": params,
                "variables": variables,
            }

            content = Template.render(addon_dir + "/get.mustache", params_block_list)

        # print("测试代码：", content)

        with open(rf'{addon_dir}\api_generated\%s_api.yml' % (filename), 'w')as f:
            f.write(content)
