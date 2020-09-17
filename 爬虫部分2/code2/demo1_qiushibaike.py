import urllib.request
import re

# 爬取糗事百科的一些图片
url = 'https://www.qiushibaike.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

pattern = re.compile('<li class="item typs_video".*?<img src="(.*?)"', re.S)
img_list = pattern.findall(content)
for img in img_list:
    img_url = 'http:' + img
    filename = img_url.split("?")[0].split("/")[-1]
    urllib.request.urlretrieve(url=img_url, filename="./img/" + filename)
