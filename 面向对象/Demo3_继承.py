class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 集成Person
class Stu(Person):

    def run(self):
        print('haha')


s1 = Stu('otis', 45)
s1.run()
