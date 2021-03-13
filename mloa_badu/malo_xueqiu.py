"""Send a reply from the proxy without sending any data to the remote server."""
from mitmproxy import http

#request方法名不能修改
def request(flow: http.HTTPFlow) -> None:
    #发起请求 判断url是否为预期值
    if flow.request.pretty_url == "https://www.baidu.com/":
        #创建一个response
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )