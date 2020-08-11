import os

print(os.name)
print(os.path.abspath('Demo1_os.py'))
# os.path.isfile() 是否时文件

# os.path.exists 是否存在
file_name = 'hehe.py'
print(file_name.rpartition('.'))
print(os.path.splitext(file_name))
