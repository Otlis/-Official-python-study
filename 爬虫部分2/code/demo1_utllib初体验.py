import urllib.request as request

# 简单的请求
url = 'https://www.baidu.com/s?wd=haha'
response = request.urlopen(url=url)
# print(response)

# response对象的6个方法和1个类型
# print(type(response))

# 1. read方法获取网页二进制
# print(response.read())
# 解码后的网页源码
# print(response.read().decode('utf-8'))

# 可以在csdn上找ua大全
headers = {
'accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'accept-encoding':' gzip, deflate, br',
'accept-language':' zh-CN,zh;q=0.9',
'cache-control':' max-age=0',
'cookie':' pgv_pvi=1653881856; _pk_ses.1.709b=1; token=0cfd8f38d12bedec5a2c9f82953e73d9; vID=98452357581; _pk_id.1.709b=c668d4bccb0371df.1587987914.119.1600219503.1600137064.',
'sec-fetch-dest':' document',
'sec-fetch-mode':' navigate',
'sec-fetch-site':' cross-site',
'sec-fetch-user':' ?1',
'upgrade-insecure-requests':' 1',
'user-agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}

# 2. 构建request对象
my_request = request.Request(url=url, headers=headers)

response = request.urlopen(my_request)
# print(response)
# 3. 转码汉字 urllib.parse.quote
import urllib.parse as parse
name="李清华"
a=parse.quote(name)
print(a) # %E6%9D%8E%E6%B8%85%E5%8D%8E