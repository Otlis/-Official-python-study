amap = {'name': 'otis', 'age': 18}
alist = [1, 2, 3, 5, 6, 6]
import json

print(json.dumps(amap))
print(json.dumps(alist))

# loads 命令将json格式的字符串，转换成对应的python格式 dict list
b = json.dumps(alist)
c = json.loads(b)
print(type(c))

