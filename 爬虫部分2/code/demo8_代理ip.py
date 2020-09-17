import urllib.request

url = ''
headers = {

}
request = urllib.request.Request(url=url, headers=headers)
# 设置代理
proxies = {
    'http': '21.231.231:8982'
}

# todo 代理池
proxy_pool = {
    {'http': 'xxxxxx'},
    {'http': 'xxxxxx'}
}

import random

proxies = random.choice(proxy_pool)

handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
