# with 关键字
# 上下文管理器，数据库 socket都可以自动关闭


try:
    with open('mya.txt', 'r') as f1:
        f1.read()
        # f1.close() don't need to close，'with'  will help us to close the file
except:
    print('file not found')


# 可以自己写一个类使用with关键字
# 但是必须重写两个方法

class Demo(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('退出时调用的方法，可以是关闭数据库连接等')

    def run(self):
        print('hahahahahahhaha')


with Demo() as d:
    d.run()
