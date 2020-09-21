import selenium.webdriver
import time

# 谷歌浏览器驱动的地址
path = 'chromedriver.exe'
browser = selenium.webdriver.Chrome(path)

url = 'http://www.baidu.com'
browser.get(url)

# 通过标签的id查找
a = browser.find_element_by_id('su')

# 通过标签的name属性查找 name="wd"
b = browser.find_elements_by_name('wd')
# print(b)

# 通过xpath查找标签   根据xpath路径来查找
# c = browser.find_elements_by_xpath('')

# 专门查找超链接的标签   百度中学术的
d = browser.find_elements_by_link_text('学术')
print(d)

browser.quit()
