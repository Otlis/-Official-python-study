# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DangPipeline:

    def open_spider(self, spider):
        self.file = open('dang.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 保存到文件中
        self.file.write(str(item))
        return item

    def close_spider(self, spider):
        self.file.close()


import urllib.request


# 这个管道用于下载图片   记得一定要return item 意思是，优先级高的管道处理完数据后，把数据传送到优先级低的管道中
# 记得要在settings文件中配置，加上这个类
# todo
# ITEM_PIPELINES = {
#     'dang.pipelines.DangPipeline': 300,
#     'dang.pipelines.MyPipleline': 299
# }
class MyPipleline:
    def process_item(self, item, spider):
        src = item.get('img')
        print('bbbbb'+src)
        name = item.get('name')
        urllib.request.urlretrieve(src, './bookimg/'+name + '.jpg')
        return item
