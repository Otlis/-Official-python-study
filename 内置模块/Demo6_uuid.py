import uuid

print(uuid.uuid4())  # 通过伪随机数得到的uuid,有一定概率的重复
print(uuid.uuid1())  # 根据机器码 时间戳等生成的随机数，全球唯一
