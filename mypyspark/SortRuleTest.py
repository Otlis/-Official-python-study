"""
# 任何Spark程序都是SparkContext开始的，
# SparkContext的初始化需要一个SparkConf对象，
# SparkConf包含了Spark集群配置的各种参数(比如主节点的URL)。
# 初始化后，就可以使用SparkContext对象所包含的各种方法来创建和操作RDD和共享变量。
# Spark shell会自动初始化一个SparkContext(在Scala和Python下可以，但不支持Java)。
# getOrCreate表明可以视情况新建session或利用已有的session
"""

# 定义自定义函数
from pyspark.sql.types import StructType, StructField, StringType

from mypyspark import SortRuleFunction
from pyspark.sql import SparkSession


def is_nulludf(fieldValue, defaultValue):
    if fieldValue == None:
        return defaultValue
    return fieldValue


spark = SparkSession.builder.appName('test_udf').master('local').getOrCreate()

struct1 = StructType([StructField("name", StringType(), True)])
df = spark.read.json("D:\peoject\python\Official-python-study\mypyspark\mya.json", schema=struct1)
print(df)
df.createTempView("table")

# 注册自定义函数
spark.udf.register("myudf", SortRuleFunction.myFun)

# 使用自定义函数
spark.sql(
    "select name, myudf('accountName', 'account', 'currencyCode', 'transactionCode', 'transactionAmount','borrowFlage', 'businessCode', '融资', 'accountChinessName') as col_name2 from table ").show()
spark.stop()
