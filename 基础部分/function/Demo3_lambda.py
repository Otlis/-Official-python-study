def ok(a, b, fun):
    return fun(a, b)


print(ok(1, 4, lambda x, y: x + y))
