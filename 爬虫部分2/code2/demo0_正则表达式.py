import re

# 正则表达式
str = 'abbbc'
# *？ 是非贪婪模式，尽可能少的匹配 最少0
pattern = re.compile('ab*?')
a = pattern.findall(str)
print(a)
