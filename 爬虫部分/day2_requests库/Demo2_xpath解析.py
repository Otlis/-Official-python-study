import requests
from lxml import etree


# 自定义一个异常
class RequestError(Exception):
    """
    请求异常
    """
    pass


class ParaseError(Exception):
    """
    解析异常
    """
    pass


# https://beijing.anjuke.com/community/?from=navigation
# todo 一定要加headers 不然会很容易被认为是爬虫而被封ip
def download(url):
    resp = requests.get(url,
                        headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'},
                        params={'from': 'navigation'},
                        proxies={
        'http': 'http://125.108.117.240:9999'
    })
    if resp.status_code == 200:
        parse(resp.text)  # 文本  resp.content
    else:
        raise RequestError('请求失败！')


def parse(html):
    root = etree.HTML(html)  # 找到根节点 Element元素对象
    divs = root.xpath('//div[@class="li-itemmod"]')  # 查找所有class="li-itemmod" 的div，返回的是一个可迭代的对象
    print(divs)
    for div in divs:
        cover_url = div.xpath('.//img/@data-src')[0]  # extract之后是一个集合 取第一个元素，就是图片的地址
        title = div.xpath('.//h3/a/text()')[0]  # 获取标题
        print(title, cover_url)


if __name__ == '__main__':
    download('https://beijing.anjuke.com/community/')
