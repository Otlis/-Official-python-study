# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 在这里定义的是解析后的返回的数据结构
class MvItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    img = scrapy.Field()