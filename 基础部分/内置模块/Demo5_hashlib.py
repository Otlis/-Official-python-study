import hashlib
import hmac

# 这两个模块是用来加密的

x = hashlib.md5()
x.update('sdsad'.encode('utf8'))
print(x.hexdigest())

h1 = hashlib.sha224('4545asd'.encode('utf8'))
print(h1.hexdigest())
