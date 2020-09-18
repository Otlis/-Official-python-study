from lxml import etree

tree = etree.parse('D:\peoject\python\Official-python-study\爬虫部分2\code3_xpath解析\est.html')
# 获取所有li标签的内容
list1 = tree.xpath('//li/text()')
# print(list1)


# 查询所有带id的li标签  [@属性] 来限制查询的标签
list_2 = tree.xpath('//li[@id]/text()')
# print(list_2)

list_3 = tree.xpath('//li[@id="1"]/text()')
# print(list_3)

# 查询某个标签的属性  @class 即可，@属性
value1 = tree.xpath('//li[@id="1"]/@class')
print(value1)

# 包含查询 查询所有的 li标签 li标签的id中包含‘a’   [contains(@属性,'过滤条件')]
# starts-with 以什么开始过滤
list_4 = tree.xpath('//li[contains(@id,"a")]/text()')
print(list_4)
