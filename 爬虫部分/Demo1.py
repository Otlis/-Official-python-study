"""
            基本操作
urllib.request.urlopen(url) 发起get请求
url.parse.quote() 将中文进行url编码
urllib.request.url.urlretrieve(url,filename) 下载url保存到filename
"""

from urllib.request import urlopen, urlretrieve, Request
from urllib.parse import quote

"""
利用狗狗搜索某个关键字，然后把结果保存到本地的文件中
"""


def start_search(q):
    # 请求数据的格式
    url = 'https://www.dogedoge.com/results?q=%s'
    url1 = 'https://www.dogedoge.com/results?q={}}'

    # 根据关键字拼接url
    real_url = url % quote(q)
    print(real_url)
    # response2 = urlopen(url1.format(quote(q))) 设置url的不同的方式
    # 封装请求参数
    request = Request(url=real_url, headers={
        'cookie': '__cfduid=dfcce8c9c9d5b35cb6c0111e30f6803051597130575; token=a5016085dbac934989cefa4324a7ee4a; vID=10358828176; _pk_ses.1.709b=1; _pk_id.1.709b=8256c00d3e761b0b.1595935317.58.1597588028.1597582118.',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    })
    response1 = urlopen(request)

    bytes_ = response1.read()

    with open('{}.html'.format(q), 'w+b') as file:
        file.write(bytes_)


start_search('千峰')
