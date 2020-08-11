# 读取
# file2 = open('name.txt')
# print(file2.read())
# file2.close()

# 读取一行
# file3 =open('name.txt')
# print(file3.readline())
# file3.close()

# 读取多行,逐行打印
# file4 =open('name.txt')
# for i in file4.readlines():
#     print(i)


file5 = open('name.txt')
print(file5.tell())  # 意思是指针读取到哪了
file5.read(1)
print(file5.tell())
file5.seek(0)  # 指针的位置重置
# 第一个参数代表偏移的位置，第二个参数 0：从文件开头偏移 1：从当前位置偏移 2：从文件结尾偏移
file5.seek(4, 0)
