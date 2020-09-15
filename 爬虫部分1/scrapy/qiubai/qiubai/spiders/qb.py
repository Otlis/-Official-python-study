import scrapy


class QbSpider(scrapy.Spider):
    name = 'qb'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        # 开始解析 安装了xpath helper 快捷键 ctrl+shift+x
        # //div[@class="col1 old-style-col1"]//div[@class="author clearfix"]//img//@alt 昵称
        # //div[@class="col1 old-style-col1"]//div[@class="author clearfix"]//img//@src 图片的地址

        alt_list = response.xpath('//div[@class="col1 old-style-col1"]//div[@class="author clearfix"]//img//@alt')
        src_list = response.xpath('//div[@class="col1 old-style-col1"]//div[@class="author clearfix"]//img//@src')
        ret_list = []
        for i in range(len(alt_list)):
            # extract()	提取的是selector对象的data
            alt = alt_list[i].extract()
            src = src_list[i].extract()
            ret_map = {}
            ret_map['alt'] = alt
            ret_map['src'] = src
            # print(alt, src)
            ret_list.append(ret_map)
        return ret_list
