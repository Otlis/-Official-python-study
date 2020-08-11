i = 1
while i < 10:
    a = 1
    while a <= i:
        print('%d * %d = %d' % (a, i, a * i), end="   ")
        a += 1
    print('')
    i += 1
