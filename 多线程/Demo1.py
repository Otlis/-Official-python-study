import threading


def eat():
    for i in range(50):
        print('吃饭')


def happy():
    for i in range(50):
        print('xiao ha ha ')

# target 传递的是一个行为   方法名
t1 = threading.Thread(target=eat)
t2 = threading.Thread(target=happy)

t1.start()
t2.start()
