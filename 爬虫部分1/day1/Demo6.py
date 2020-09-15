"""
# 这里主要是用了build_opener  和urlopen功能差不多  这个就是可以携带更多的信息，配置多种请求处理器
多个urllib的请求处理器
-cookie
-proxy
-http
"""

from urllib.request import Request, build_opener, HTTPHandler, HTTPCookieProcessor, ProxyHandler
from http.cookiejar import CookieJar
from urllib.parse import urlencode

open = build_opener(HTTPHandler(),
                    HTTPCookieProcessor(CookieJar()),
                    ProxyHandler(proxies={
                        'http': '175.43.151.112:9999'  # 这里可以百度http代理
                        # 'https': 'https://proxy-ip:port'
                    })
                    )
posturl = ''

# post请求需要的一些信息
data = {
    'email': 'xxxx',
    'password': 'xxxx',
    '...': '...'
}
# 请求需要的headers
headers = {

}

request = Request(posturl, urlencode(data).encode('utf-8'), headers)

resp = open.open(request)  # 响应类型是 http.client.HTTPResponse
bute_ = resp.read()  # 这样就可以获取信息
