from mitmproxy import http
import json


def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 拿到响应数据，转化成为python对象
        # json.loads:将字符串转成字典格式
        data = json.loads(flow.response.content)
        # 修改对应的字段的值
        data['data']['items'][1]['quote']['name'] = data['data']['items'][1]['quote']['name'] *2
        data['data']['items'][2]['quote']['name'] = ""
        # 把修改后的数据，转为字符串，赋值给原始响应数据
        flow.response.text = json.dumps(data)