import json
import hashlib

# 读文件的方法




def read_file(file_name):
    try:
        with open(file_name, encoding='utf8') as f:
            content = f.read()
            return content
    except:
        print('文件没有找到！')


# 把数据写入文件
def write_to_json(data, filename):
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(data, f)


# 从文件中读取数据放到dict中
def read_json(filename):
    try:
        with open(filename, encoding='utf8') as f:
            a = json.load(f)
            return a
    except:
        return {}


def register(name, pwd):
    jiami = hashlib.md5()
    jiami.update(pwd.encode('utf8'))
    p = jiami.hexdigest()
    mydict[name] = p
    write_to_json(mydict, 'account.txt')
    print('注册成功！')


def login(name, pwd):
    jiami = hashlib.md5()
    jiami.update(pwd.encode('utf8'))
    p = jiami.hexdigest()
    realpwd = mydict.get(name, -1)
    print('真正的密码为：', realpwd)
    if realpwd == p:
        print('登陆成功！')
    else:
        print('登陆失败！')


# ==============================================开始==============================================
content = read_file('start.txt')
mydict = read_json('account.txt')
while True:
    c = content + '\n 请输入功能序号：'
    operatot = input(c)
    if operatot == '1':
        name = input('输入账号：')
        pwd = input('输入密码：')
        login(name, pwd)
    elif operatot == '2':
        name = input('输入账号：')
        pwd = input('输入密码：')
        register(name, pwd)
    elif operatot == '3':
        print('退出')
        break
    else:
        print('输入有误！')
