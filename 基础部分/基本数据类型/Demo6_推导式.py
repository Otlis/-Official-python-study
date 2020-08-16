# 普通的写法
alist = []
for i in range(1, 11):
    alist.append(i)

# 推导式的写法
blist = [i for i in range(1, 11)]
print(blist)

amap = {i: 0 for i in range(1, 11)}
print(amap)
