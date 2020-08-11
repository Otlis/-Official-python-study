def fun():
    a = 1
    b = 2
    return a + b


# 这种写法就是闭包
def mysum(a):
    def add(b):
        return a + b

    return add


haha = mysum(1)  # haha的type是一个函数
print(haha(2))


# todo 闭包写一个计数器
# 不传参数默认为0
def counter(FIRST=0):
    cnt = [FIRST]

    def add_one():
        cnt[0] += 1
        return cnt[0]

    return add_one


count = counter(5)
print(count())
print(count())
print(count())
