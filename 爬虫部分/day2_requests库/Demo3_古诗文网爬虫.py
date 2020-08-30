import os
import uuid

import requests
from lxml import etree
import random

user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36']


def itempipline(data):
    """保存数据  写入到数据库"""
    print(data)


from csv import DictWriter

csv_file = open('gushici.csv', 'a')
is_first_flage = os.path.exists('gushici.csv')  # 是否时第一次操作csv文件
header_fields = ('id', 'title', 'author', 'tags')


def itempipline4csv(data):
    """保存数据到csv文件"""
    global is_first_flage
    with open('gushici.csv', 'a') as f:
        writer = DictWriter(f, header_fields)

        # 第一次写入，需要写入标题
        if not is_first_flage:
            writer.writeheader()
            is_first_flage = True

        # 写入数据
        writer.writerow(data)


def parse(html):
    root = etree.HTML(html)  # 获取根对象
    divs = root.xpath('//div[@class="left"]/div[@class="sons"]')  # 获取所有的sons  div
    for div in divs:
        item = {}
        item['id'] = uuid.uuid4().hex
        item['title'] = div.xpath('.//p[1]//text()')
        item['author'] = ' '.join(div.xpath('.//p[2]/a/text()'))
        item['tags'] = ','.join(div.xpath('./div[@class="tag"]/a/text()'))
        itempipline4csv(item)


def download(url):
    resp = requests.get(url,
                        # headers={'user-agent': random.choice(user_agent)},
                        )
    if resp.status_code == 200:
        parse(resp.text)
    else:
        print('hhahhaha')


if __name__ == '__main__':
    download('https://www.gushiwen.cn/')
