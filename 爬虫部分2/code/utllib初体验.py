import urllib.request as request

# 简单的请求
url = 'https://www.baidu.com/s?wd=haha'
response = request.urlopen(url=url)
print(response)

# response对象的6个方法和1个类型
print(type(response))

# 1. read方法获取网页二进制
# print(response.read())
# 解码后的网页源码
print(response.read().decode('utf-8'))

# 可以在csdn上找ua大全
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}

response = request.urlopen(url=url, headers=headers)
print(response)
# 2.
