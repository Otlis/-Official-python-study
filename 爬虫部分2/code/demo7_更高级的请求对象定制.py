"""
handler 可以定制更高级的请求头
1. 创建handler对象  handler=urllibe.request.HTTPHandler()
2. 创建opener对象  opener=urllibe.request.build_opener(*handler)
3. 创建Request对象
4. 发送Request请求  opener.open(req)
"""

from urllib.request import HTTPHandler, build_opener
import urllib.request
# 1
url = ''
# 2
headers = {

}
# 3
request = urllib.request.Request(url=url, headers=headers)
# 4
handler = HTTPHandler()
# 5
opener = build_opener(handler)
# 6
response = opener.open(request)
