# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MvPipeline:
    def open_spider(self, spider):
        self.file = open('dytt.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        print("===================================")
        print(item)
        self.file.write(str(item))
        return item

    def close_spider(self, spider):
        self.file.close()
