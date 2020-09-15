"""
复杂的get请求 带分页的
url + urlencode(params) urlencode的作用就是把字典里的元素转换成这样的格式  name='xxx'&age='xxx'

"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = 'https://www.dogedoge.com/results?'
params = {
    'q': '',
    'p': 1
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'cookie': '__cfduid=dfcce8c9c9d5b35cb6c0111e30f6803051597130575; token=5e1fd100c179bd07a4be9f39792d3314; vID=13470908375; _pk_ses.1.709b=1; _pk_id.1.709b=8256c00d3e761b0b.1595935317.76.1598020406.1598017176.'
}

import time


def pages_get(wd):
    params['q'] = wd
    for page in range(100):
        params['p'] = page
        page_url = url + urlencode(params)
        response = urlopen(Request(page_url, headers=headers))
        print(response.code)
        with open('pages/{}-{}.heml'.format(wd, page), 'w+b') as f:
            data = response.read()
            f.write(data)
        time.sleep(2)

pages_get('python')
