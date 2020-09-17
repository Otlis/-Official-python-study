import http.cookiejar
import urllib.request

# 设置request
request = urllib.request.Request()
# 设置cookiejar
cookiejar = http.cookiejar.CookieJar()
# 创建handler
handler = urllib.request.HTTPCookieProcessor(cookiejar=cookiejar)
# 创建opener
opener = urllib.request.build_opener(handler)
# 如果opener是通过cookiejar来获取的，那么通过opener发送的请求 就可以直接将相应的cookie保存到opener中
# 来达到动态cookie的效果
response = opener.open(request)
