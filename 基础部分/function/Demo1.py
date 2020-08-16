a = 123


# 如果方法里面用到了同名的变量，只是在方法里面会改变变量的值
# 在方法外面不会改变变量的值
def myFunction1():
    a = 444
    print(a)

# 如果在方法里面声明变量为global 那么会影响方法外面变量的数值
def myFunction2():
    global a
    a = 7878
    print(a)


myFunction1()  # 结果为 444
print(a)  # 结果为 123
