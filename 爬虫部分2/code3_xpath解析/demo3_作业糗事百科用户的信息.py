from lxml import etree
import urllib.request

url = 'https://www.qiushibaike.com/text/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
tree = etree.HTML(content)

list1 = tree.xpath('//div[@class="article block untagged mb15 typs_hot"]/div[@class="author clearfix"]//img/@src')
list2 = tree.xpath('//div[@class="article block untagged mb15 typs_hot"]/div[@class="author clearfix"]//a/h2/text()')
with open('bbb.txt', 'w', encoding='utf8') as f:
    for i in range(len(list1)):
        print(list1[i])
        print(list2[i])
