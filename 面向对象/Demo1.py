class Foo:
    def __next__(self):
        return 1


class Stu(object):
    # 在slot中定义这个类可以存在的属性
    # 不可以动态增加slot中没有的属性
    # 可以看到slots中只有name和age属性，就不能动态增加address属性了
    # __slots__ = ('name', 'age')

    def __init__(self, x, y):
        self.name = x
        self.age = y
        self.__score = 100  # 以两个下划线开始的为私有变量

    def __eq__(self, other):
        return self.name == other.name

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs['fn'])

    # 只要重写了这个方法，这个类就是可以迭代的对象。
    # 返回值必须是一个可以迭代的对象,并调用这个对象的next方法
    def __iter__(self):
        # return (1, 2, 3)
        return Foo()

    def run(self):
        print('正在跑步')

    @staticmethod
    def sleep():
        print('ahah这是静态方法')


s1 = Stu('otis', 12)
# s1.address = 'beijing'  # 可以动态的增加属性
# print(s1.address)

# 这个方法会调用 __call__
s1('haha', 67, fn=lambda x, y: x + y)

# 获取私有变量的方法
print(s1._Stu__score)
