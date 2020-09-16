import urllib.request
import urllib.parse

# 请求参数写成map格式，会自动转码并拼接

url = 'http://www.baidu.com/s?'
data = {
    'name': '张三',
    'age': 15
}
data = urllib.parse.urlencode(data)
print(data)

url = url + data
headers = {

}

request = urllib.request.Request(url=url, headers=headers)
response=urllib.request.urlopen(request)
print(response.read().decode('utf-8'))