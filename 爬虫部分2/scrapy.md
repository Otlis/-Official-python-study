# 爬虫大方向

## 1.urllib

``` shell
1.urllib.request.urlopen() 模拟浏览器向服务器发送请求
2.一个类型以及6个方法
3.get
4.post
5.ajax
6.ajax-post 
7.复杂的get
8.error
9.cookie登陆
10.handler
11.代理
12.cookie库
```

## 2.解析

```shell
1.正则
2.xpath
3.jsonpath
4.bs4
```

## 3.selenium

> 如果网站中返回的是js文件，那么urllib是解析不了的。可以使用selenium

```shell
1.selenium
2.phantomjs
3.headless
```



































# scrapy

## 一、quick start

```shell
# 1.创建项目
scrapy startproject  name

# 2.进到spiders目录
cd myscrapy/myscrapy/spiders

# 3.创建爬虫文件
spider genspider 爬虫文件名字（不能和项目名一样）  爬取的域名
scrapy genspider baidu www.baidu.com

# 4.运行创建的爬虫文件
scrapy crawl 爬虫文件
scrapy crawl baidu

#更改settings文件中不遵守robots协议
ROBOTSTXT_OBEY = False
```

反爬策略解决

```shel
1. 去掉 http/https
2. 去掉www
3. 关闭ROBOTS协议
4. setting文件中添加ua（从网页上粘贴）
```

## 二、介绍

```shell
爬虫文件的基本组成：
	集成scrapy.Spider类
			name='qiubai'		===>
			allowed_domains     ===>爬虫允许的域名，在爬取的时候，如果不是此域名下的url会被过滤
			start_urls          ===>声明排重的气势地址，可以写多个url，一般是一个
			parse(self,response)===>解析数据的回调函数
				response.text
				response.body   ===>响应的是二进制文件
				response.xpath()===>xpath方法的返回值类型是selector列表
			extract()			===>提取的是selector对象的data
			extract_first()     ===>提取的是selector列表中的第一个数据
```

## 三、操作

> 解析后输出到文件

```shell
#　输出json文件
scrapy crawl qb -o qb.json
#　输出csv文件
scrapy crawl qb -o qb.csv
```









































