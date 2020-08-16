import requests

# 请求一个地址
response = requests.get('https://www.bilibili.com/')

print(response)  # 这个是状态码

print(response.content.decode('utf8'))  # 这个是页面上的内容

# print(response.text) # 和上边差不多
print(response.json()) # 如果返回的是json字符串 可以解析,不是的话 会报错