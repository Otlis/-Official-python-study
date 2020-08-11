# 常用的方法
# open() 打开文件
# read() 输入
# readline() 输入一行
# seek() 文件内移动
# write() 输出
# close() 关闭


# w 标志为写的意思
file1 = open('name.txt', 'w')
file1.write('otis')
file1.close()


# 追加写 'a'
file1 = open('name.txt', 'a')
file1.write('qinghua')
file1.close()
