# 相当于一个字符串数组，可以倒着指定元素的位置

otis = '你知道吗'

# print(otis[0:3])  #结果为：你知道
# print(otis[-1])
# print(otis[-2])
# print(otis[3])
# print(otis[1])

year = 2018
print(otis[year % 12])

# 判断是否存在
print('你' in otis)
print('你' not in otis)

# 字符串连接
print(otis + '知道啊')  # 你知道吗知道啊

# 重复3次
print(otis * 3)

# todo 列表  用[] 内容可以变更

a_list = ['aaa', 'bbb']
# 增加元素
a_list.append('vvv')
# 溢出元素
a_list.remove('bbb')
print(a_list)

# todo 元祖  一般元祖中存储的内容是不可以变更的

# xingzuo = ('双鱼座', '天枰座', '狮子座')
# day = ((1, 20), (2, 20), (3, 24))   #假设各星座对应的日期
# # 元祖中数值大小的比较规则  (1) < (2)  (1,2) < (2,0) 相当于12<20
# print(xingzuo[1])
