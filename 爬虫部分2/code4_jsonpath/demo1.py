import json
import jsonpath

# 教程 https://blog.csdn.net/myself8202/article/details/80724968
obj = json.load(open('store.json', 'r', encoding='utf-8'))

# 书店所有书的作者
a_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
# print(a_list)

# 所有作者
b_list = jsonpath.jsonpath(obj, '$..author')
# print(b_list)

# store 中所有的价格
c_list = jsonpath.jsonpath(obj, '$.store.book[*].price')
# print(c_list)

# 第三本书
d_list = jsonpath.jsonpath(obj, '$..book[0].price')
# print(d_list)

# 最后一本书
e = jsonpath.jsonpath(obj, '$..book[(@.length-1)].price')
# print(e)

# 前面2本书
f = jsonpath.jsonpath(obj, '$..book[0,1].price')
# print(f)

# 过滤出所有的包含isbn属性的书
g = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
# print(g)

# 过滤出价格低于10的书
h = jsonpath.jsonpath(obj, '$..book[?(@.price<10)]')
print(h)