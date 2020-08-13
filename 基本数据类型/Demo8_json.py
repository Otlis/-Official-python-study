amap = {'name': 'otis', 'age': 18}
alist = [1, 2, 3, 5, 6, 6]
import json

print(json.dumps(amap))
print(json.dumps(alist))

# loads 命令将json格式的字符串，转换成对应的python格式 dict list
b = json.dumps(alist)

# 把数据转换成json格式并写入文件
f = open('name.txt')
b = json.dump(alist, f)
f.close()

c = json.loads(b)
print(type(c))
