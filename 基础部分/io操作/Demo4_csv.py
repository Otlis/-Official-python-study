import csv

f1 = open('demo1.csv', 'w', newline='')

# 使用csv包装一层
c = csv.writer(f1)
c.writerow(['name', 'age', 'address'])
c.writerow(['otis', 19, 'beijing'])

# 写多行
# c.writerows([[], [], [], ])

f1.close()
