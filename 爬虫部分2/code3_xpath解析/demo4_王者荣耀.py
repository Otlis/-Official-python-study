import urllib.request
from lxml import etree

url = 'https://lol.qq.com/data/info-heros.shtml'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('gb2312')
# '//ul[@class="herolist clearfix"]//li//img/@src'
# print(content)

tree = etree.HTML(content)
url_list = tree.xpath('//ul[@id="jSearchHeroDiv"]//img/@src')
name_list = tree.xpath('//ul[@id="jSearchHeroDiv"]//p/text()')
print(len(url_list))
# for i in range(len(url_list)):
#     url = 'https://' + url_list[i]
#     print(url)
#     name = name_list[i]
#     urllib.request.urlretrieve(url, './imgs/' + name + '.png')
