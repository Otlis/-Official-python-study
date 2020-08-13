class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 集成Person
class Stu(Person):
    # 子类属性增加
    # 写法1
    # def __init__(self, name, age, address):
    #     Person.__init__(self, name, age)
    #     self.address = address

    # 写法2
    def __init__(self, name, age, address):
        super(Stu, self).__init__(name, age)
        self.address = address

    def run(self):
        print('haha')


s1 = Stu('otis', 45)
s1.run()


# 允许多继承,多继承找一个方法的话是深度优先
# 子类不继承父类的私有方法


class A(object):
    __name = 'otis'

    def run(self):
        print("aaaaaaaaaaa")


class B(object):
    __age = 12

    def eat(self):
        print("okokok")


class C(A, B):
    def haha(self):
        print('__name, __age')


c1 = C()
c1.run()
print(c1._A__name)  # 这样可以获取父类中的私有属性，同样的方案可以获取父类中的私有方法
