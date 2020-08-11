import time


def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)

    return wrapper


# 这中写法叫语法糖
@timer
def i_sleep():
    time.sleep(3)


# 执行顺序  发现i_sleep有语法糖修饰，就会执行语法糖的方法
i_sleep()



# todo 带参数  可以无限封装
def new_haha(args):
    def haha(func):
        def hehe(a, b):
            print('start' + args)
            func(a, b)
            print('stop')

        return hehe

    return haha


@new_haha('sum')
def sum(a, b):
    print(a + b)


sum(1, 2)
