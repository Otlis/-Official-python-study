import threading

ticket = 100

# 创建一个锁
lock = threading.Lock()


def sale1():
    global ticket
    while True:
        lock.acquire()  # 获取锁
        if ticket > 0:
            ticket -= 1
            lock.release()
            print('剩余{}张票'.format(ticket))
        else:
            lock.release()  # 释放锁
            break


t1 = threading.Thread(target=sale1)
t2 = threading.Thread(target=sale1)

t1.start()
t2.start()
