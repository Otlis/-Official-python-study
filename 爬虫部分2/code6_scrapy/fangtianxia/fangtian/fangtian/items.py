# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FangtianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    provience_name = scrapy.Field()
    city_name = scrapy.Field()
    house_name = scrapy.Field()
    house_price = scrapy.Field()


