import selenium.webdriver
import time

# 谷歌浏览器驱动的地址
path = 'chromedriver.exe'
browser = selenium.webdriver.Chrome(path)

url = 'http://www.baidu.com'
browser.get(url)
# 获取标签
i = browser.find_element_by_id('su')
# 1. 获取属性
a = i.get_attribute('class')

# 退出
browser.quit()
