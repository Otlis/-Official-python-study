class MyError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 这个就是报错时打印的信息
    def __str__(self):
        return 'x为{},y为{}'.format(self.x, self.y)


# 　raise 相当于 throw new RuntimeException
if True:
    raise MyError(1, 2)
