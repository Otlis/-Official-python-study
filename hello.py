# from hello import * 这种方式默认导入的是这个list中的变量或者方法
# 如果不写默认是所有的
__all__ = ['x']
x = 123
y = 'haha'

_z = 'otis'  # 这种写法就相当于 protect关键字修饰，只是在这个py里面用，强烈不建议外部使用

# 这段代码的意思是只有在本文件运行时才会打印
# 如果是被import __name__就不是__main__了，就是另一个py文件的名字了
if __name__ == '__main__':
    print('haha')
