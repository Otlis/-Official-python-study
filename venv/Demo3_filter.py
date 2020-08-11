a = (1, 2, 3, 4, 5)
b = 4
list(filter(lambda x: x < b, a))  # 取出a中小于b的元素
len(list(filter(lambda x: x < b, a)))  # 计算元素的个数
