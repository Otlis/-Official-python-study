import scrapy

from fangtian.items import FangtianItem


class FangSpider(scrapy.Spider):
    name = 'fang'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        # 省名字 有的为空
        provience_list = response.xpath('//table[@id="senfe"]//tr')
        # // table[ @ id = "senfe"] // tr / td[2] / strong / text()
        # city的名字和连接
        city_list = response.xpath('//table[@id="senfe"]//tr/td[3]')

        # 两个list长度都是56，有的provience_list的值为空，取上一个即可，但是上一个也没有那就再取上一个
        for i in range(len(provience_list)):
            provience_name = provience_list[i].xpath('./td[2]/strong/text()').extract_first()
            a = i
            while (provience_name is None or provience_name.strip() == '') and a > 0:
                a -= 1
                provience_name = provience_list[a].xpath('./td[2]/strong/text()').extract_first()

            if provience_name.strip() != '其它':
                cities = city_list[i].xpath('./a')
                for city in cities:
                    city_name = city.xpath('./text()').extract_first()
                    city_href = city.xpath('./@href').extract_first()
                    url = 'https:' + city_href.split('.')[0].split(':')[1] + '.newhouse.fang.com/house/s/'
                    yield scrapy.Request(url=city_href, callback=self.second_parse,
                                         meta={'provience_name': provience_name, 'city_name': city_name})

    def second_parse(self, response):
        provience_name = response.meta['provience_name']
        city_name = response.meta['city_name']
        print('===========================')
        # 解析第二页的连接
        # '//a[@class="last"][2]' ！=‘尾页’
        # list = response.xpath(
        #     '//div[@class="nl_con clearfix"]/ul/li')
        list=response.xpath('//div[contains(@class,"nl_con")]/ul/li')
        print(city_name, len(list))
        # house_price_list = response.xpath(
        #     '//div[@class="nhouse_price"]/span/text()')

        # for i in range(len(house_name_list)):
        #     house_name = house_name_list[i].extract()
        #     house_price = house_price_list[i].extract()
        # print(house_name,house_price)
        # for i in range(len(house_name_list)):
        #     house_name = house_name_list[i].extract()
        #     house_price = house_price_list[i].extract()
        #     item = FangtianItem(house_name=house_name, house_price=house_price, provience_name=provience_name,
        #                         city_name=city_name)
        #     yield item
