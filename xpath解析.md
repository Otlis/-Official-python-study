## 一、quick start

```python
from lxml import etree
# 解析本地文件
tree=etree.parse('xxx.html')
# 服务器响应文件
tree=etree.HTML()
	html_tree=etree.HTML(response.read().decode('utf-8'))
# 开始解析
tree.xpath('xpath路径')

```

## 二、基本语法

```
// 不考虑层级关系，下面所有的标签里查找
/ 子标签里查找
text()
```























































