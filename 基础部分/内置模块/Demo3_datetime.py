import datetime as dt

# 以一个下划线开始 _
# 以两个下划线开始
# 以两个下划线开始 两个下划线结束

print(dt.datetime.now())  # 2020-08-11 17:42:20.571181
print(dt.date(2020, 8, 11))  # 2020-08-11
print(dt.time(10, 10, 10))  # 10:10:10
print(dt.datetime.now() + dt.timedelta(-1))  # 2020-08-10 17:42:20.571181
