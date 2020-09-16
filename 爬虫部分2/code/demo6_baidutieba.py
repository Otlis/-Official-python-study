import urllib.request
import urllib.parse

# ajax get请求 爬百度贴吧
url = 'https://tieba.baidu.com/f?ie=utf-8&kw=python&pn=200'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
for i in range(10):
    data = {
        'pn': i * 50
    }
    my_url = url + urllib.parse.urlencode(data)
    my_request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(my_request)
    print(response.read().decode('utf-8'))
