class Singleton(object):
    __instance = None
    __first_flage = True

    # new一个对象时先调用new方法申请一个内存
    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, a, b):
        # 只能第一次创建时赋值，以后创建不能更改类的属性值
        if self.__first_flage:
            self.a = a
            self.b = b
            self.__first_flage = False


p1 = Singleton(1, 2)
p2 = Singleton(2, 2)
print(p2.a)
print(p1 is p2)
