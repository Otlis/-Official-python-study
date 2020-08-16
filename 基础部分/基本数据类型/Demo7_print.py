print('helo my name is {},and my age is {}'.format('otis', 18))
print('helo my name is {1},and my age is {0}'.format(18, 'otis'))

alist = ['otis', 18, 'beijing']
print('helo my name is {},and my age is {},and my address is {}'.format(*alist))

amap = {'name': 'otis', 'age': 19, 'addr': '天津'}
print('helo my name is {name},and my age is {age},and my address is {addr}'.format(**amap))
