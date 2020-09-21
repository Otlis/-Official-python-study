import selenium.webdriver
import time

# 谷歌浏览器驱动的地址
path = 'chromedriver.exe'
browser = selenium.webdriver.Chrome(path)

url = 'http://www.baidu.com'
# 1. 会自定打开浏览器，自动化测试 填写表单等
browser.get(url)

# 2. 通过输入框的id来找到输入框
t = browser.find_element_by_id('kw')
# 3. 在文本框中输入搜索的内容
t.send_keys('哈哈')
# 4. 点击百度一下
button = browser.find_element_by_id('su')
button.click()
time.sleep(2)
# 5. 返回上一页
browser.back()
time.sleep(2)
# 6. 返回下一页
browser.forward()
time.sleep(2)
# 7. 向下滑动
js = "var q=document.documentElement.scrollTop=100000"
browser.execute_script(js)
time.sleep(2)
# 退出
browser.quit()
