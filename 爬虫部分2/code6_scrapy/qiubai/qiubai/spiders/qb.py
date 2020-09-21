import scrapy


class QbSpider(scrapy.Spider):
    name = 'qb'
    # 这里每个网站的反爬策略都不同 可以去掉 https或者http  或者去掉www
    # setings文件开启ua设置
    # 关闭robots协议
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        name_list = response.xpath('//div[@class="col1 old-style-col1"]/div//h2/text()')
        img_list = response.xpath('//div[@class="col1 old-style-col1"]/div/div[@class="author clearfix"]//img/@src')
        list = []
        for i in range(len(name_list)):
            name = name_list[i].extract()
            img = img_list[i].extract()
            qiubai_dict = {}
            qiubai_dict['name'] = name
            qiubai_dict['img'] = img
            list.append(qiubai_dict)
        return list
