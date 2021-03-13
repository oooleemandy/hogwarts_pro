from mitmproxy import http
from pprint import pprint

def response(flow: http.HTTPFlow):
    #拿到响应数据，content里看都有什么内容
    pprint(flow.response.content)