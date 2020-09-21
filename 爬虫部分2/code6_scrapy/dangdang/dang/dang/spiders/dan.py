import scrapy


class DanSpider(scrapy.Spider):
    name = 'dan'
    # allowed_domains 是只允许这个连接访问，但是在循环获取100页数据的时候，这样写就台固定了。要改成范围更广的地址
    # allowed_domains = ['http://category.dangdang.com/pg1-cp01.05.17.00.00.00.html']
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cp01.05.17.00.00.00.html']

    # base_utl='http://category.dangdang.com/pg3-cp01.05.17.00.00.00.html'
    base_utl = 'http://category.dangdang.com/pg'
    pg = 1
    last_url = '-cp01.05.17.00.00.00.html'

    # 多页的数据操作
    def parse(self, response):

        list = response.xpath('//ul[@id="component_59"]/li')

        for e in list:
            img = e.xpath('./a/img/@data-original').extract_first()
            if img:
                img = img
            else:
                img = e.xpath('./a/img/@src').extract_first()

            name = e.xpath('./p[@name="title"]/a/text()').extract_first()
            price = e.xpath('./p[@class="price"]/span[1]/text()').extract_first()
            book_dict = {}
            book_dict['img'] = img
            book_dict['name'] = name
            book_dict['price'] = price
            yield book_dict
        if self.pg < 2:
            self.pg += 1
            url = self.base_utl + str(self.pg) + self.last_url
            print('aaaaa'+url)
            # 这里好像前端的逻辑，类似于重定向
            yield scrapy.Request(url, callback=self.parse)


    # todo 一页的数据操作
    # def parse(self, response):
    #     # img_list = response.xpath('//ul[@id="component_59"]/li/a/img/@src')
    #     # name_list = response.xpath('//ul[@id="component_59"]/li/p[@name="title"]/a/text()')
    #     # price_list = response.xpath('//ul[@id="component_59"]/li/p[@class="price"]/span[1]/text()')
    #     list = response.xpath('//ul[@id="component_59"]/li')
    #
    #     result = []
    #     for e in list:
    #         img = e.xpath('./a/img/@data-original').extract_first()
    #         if img:
    #             img=img
    #         else:
    #             img = e.xpath('./a/img/@src').extract_first()
    #
    #         name = e.xpath('./p[@name="title"]/a/text()').extract_first()
    #         price = e.xpath('./p[@class="price"]/span[1]/text()').extract_first()
    #         book_dict = {}
    #         book_dict['img'] = img
    #         book_dict['name'] = name
    #         book_dict['price'] = price
    #     #     result.append(book_dict)
    #     # return result
    #         # todo 优化不使用return
    #         yield book_dict
