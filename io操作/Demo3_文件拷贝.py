import os

# 判断文件是否存在
# os.path.isfile()

# 以二进制的形式读取文件 加上b  rb wb
# a = open('name.txt', 'rb')
a = open('name.txt')
b = open('newfile.txt', 'w')
b.write(a.read())
