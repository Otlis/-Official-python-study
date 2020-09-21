import urllib.request
from lxml import etree

url = 'https://www.zhipin.com/job_detail/?query=python%20%E5%BC%80%E5%8F%91&city=101010100&industry=&position='

headers = {
    'cookie': 'lastCity=101010100; __zp_seo_uuid__=4eb4d3b2-4066-41a9-af35-a9102be7f6ce; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1600417266,1600650107; __c=1600650107; __l=l=%2Fwww.zhipin.com%2Fbeijing%2F&r=https%3A%2F%2Fwww.dogedoge.com%2Fresults%3Fq%3Dboss%25E7%259B%25B4%25E8%2581%2598&g=&friend_source=0&friend_source=0; __a=77392022.1600417266.1600417266.1600650107.19.2.4.19; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1600651459; __zp_stoken__=c871bGm5qXDN9U1h7DQJHKD92JAR8Xhdpf3lcd1F8SVs6AAEaHkwoE3J5HT5eBl5lD1cSd3dHQjsDKBYPWBs4YnFNN3YjR2E%2BWVEybhVhKFssa3c6MFk3EnZMMT0ZAApRCQYYZEZORxt8VUFsRQ%3D%3D',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))
content = response.read().decode('utf-8')
# print(content)
tree = etree.HTML(content)
name_list = tree.xpath('//div[@class="job-list"]//ul/li//span[@class="job-name"]/a/text()')
area_list = tree.xpath('//div[@class="job-list"]//ul/li//span[@class="job-area"]/text()')
salary_list = tree.xpath('//div[@class="job-limit clearfix"]/span[@class="red"]/text()')
company_list = tree.xpath('//div[@class="info-company"]/div[@class="company-text"]//h3/a/text()')

for i in range(len(name_list)):
    title = name_list[i]
    salary = salary_list[i]
    area = area_list[i]
    company = company_list[i]
    print(title, salary, area, company)
