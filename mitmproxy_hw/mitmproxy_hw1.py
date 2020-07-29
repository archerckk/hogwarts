import json
from pprint import pprint
from mitmproxy import http

def response(flow: http.HTTPFlow):
    # redirect to different host
    if "quote.json" in flow.request.url and "x=" in flow.request.url:
        ## 先接收到返回信息
        data = json.loads(flow.response.content)
        print("=============修改前的信息============================")
        pprint(data)
        ## 中间做一些修改
        # data["data"]["items"][1]["quote"]["name"] = data["data"]["items"][1]["quote"]["name"]*2
        # data["data"]["items"][2]["quote"]["name"] = ""
        length=len(data['data']['items'])
        for i in range(length):
            data['data']['items'][i]['quote']['current']*=2

        ## 修改返回信息的字段
        print("*******************修改后的信息************************")
        pprint(data)
        flow.response.text = json.dumps(data)