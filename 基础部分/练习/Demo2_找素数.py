# python 特有的语句 for ...else ...  for循环里面没有走break 就会走else语句
# for i in range(101, 201):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# 斐波那契数列

print()


def fei(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fei(n - 1) + fei(n - 2)


n = int(input("输入要查的位数："))
print(fei(n))
