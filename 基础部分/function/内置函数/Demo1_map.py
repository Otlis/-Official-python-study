alist = [1, 2, 3, 4, 5, 6, 1, 34, 5, 6, 7]

# 和scala中的map一样
print(list(map(lambda x: (x, 1), alist)))

from functools import reduce

# reduce
print(reduce(lambda x, y: x + y, alist, 1))

# zip函数
print(list(zip((1, 2, 3), (4, 5, 6))))
