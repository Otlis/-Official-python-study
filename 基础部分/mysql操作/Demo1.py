import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='order1',
    port=3306,
    charset='utf8'
)

# 获取一个cursor对象来操作数据库
cursor = db.cursor()
result = cursor.execute('select * from t_address')
print(result)  # 这样打印的是运行结果的条数
print(cursor.fetchone())  # 得到一条结果
print(cursor.fetchall())  # 得到所有的结果 结果是一个元祖（（），（），（））
db.commit()
db.close()
