# 为什么要用selenium?  因为一些网站会检测到是不是真实的浏览器访问的地址，如果不是真实的，有部分数据会不返回。
# 所以使用selenium来用代码操作浏览器，来获取数据

import selenium.webdriver

# 谷歌浏览器驱动的地址
path = 'chromedriver.exe'
browser = selenium.webdriver.Chrome(path)

url = 'http://www.baidu.com'
# 会自定打开浏览器，自动化测试 填写表单等
browser.get(url)
