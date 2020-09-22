import scrapy

from mv.items import MvItem


class DyttSpider(scrapy.Spider):
    name = 'dytt'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        print('=======================')
        name_list = response.xpath('//div[@class="co_content8"]//table//td[2]/b/a/text()')
        href_list = response.xpath('//div[@class="co_content8"]//table//td[2]/b/a/@href')
        for i in range(len(name_list)):
            name = name_list[i].extract()
            href = href_list[i].extract()
            # 拼接第二页的地址
            url = 'https://www.ygdy8.net' + href
            # 1. 跳转（重定向）到第二页
            # 2. callback 是调用解析第二页的方法
            # 3. 携带meta参数。是一个dict
            # 4. 注意修改allowed_domains  不能仅仅是第一页了，改成更宽泛的地址
            yield scrapy.Request(url=url, callback=self.second_parse, meta={'name': name})

    def second_parse(self, response):
        # todo 在items.py文件中定义数据结构
        img = response.xpath('//div[@id="Zoom"]//p[1]/img/@src').extract_first()
        # 获取重定向时，携带的meta参数
        name = response.meta['name']
        movie = MvItem(name=name, img=img)
        yield movie
