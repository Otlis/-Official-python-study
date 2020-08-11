otis = '你知道吗'
for x in otis:
    print(x)

for i in range(3):
    print(i)  # 结果为 0 1 2
for i in range(1, 3):
    print(i)  # 结果为  1 2

# 字符串替换
print('%s 哈哈哈哈%s' % (2018, 'okok'))

# todo while循环

num = 6
while True:
    print('a')
    num += 1
    if num > 10:
        break

# 这样引入包
import time

n = 3
while True:
    n += 1
    if n == 5:
        continue
    print(n)
    time.sleep(1)
