import urllib.request
from lxml import etree

# todo 汽车之家获取的网页一部分是 gb2312 一部分是utf-8
url = 'https://car.autohome.com.cn/price/brand-181-4.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('gb18030 '))
# content = response.read().decode('utf-8')
#
# tree = etree.HTML(content)
# title_list = tree.xpath('//div[@class="job-list-box"]//li[@class="job-name"]/@title')
# salary_list = tree.xpath('//div[@class="job-list-box"]//li[@class="job-salary"]/text()')
# company_list = tree.xpath('//div[@class="job-list-box"]//li[@class="job-company"]/text()')
#
# for i in range(len(title_list)):
#     title = title_list[i]
#     salary = salary_list[i]
#     company = company_list[i]
#     print(title, salary, company)
