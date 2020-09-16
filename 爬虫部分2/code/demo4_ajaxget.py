import urllib.request
import urllib.parse

# 循环爬取豆瓣电影
for i in range(5):
    # https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=60&limit=20
    # 需要每次更换start的数值
    url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&'
    data = {
        'start': i * 20,
        'limit': 20
    }

    data = urllib.parse.urlencode(data)
    url = url + data
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))
