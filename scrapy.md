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

#### get和post的区别

```

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

#### extract和extract_first的区别？

```
使用xpath解析得到的是一个seletor对象，需要进一步使用extract()方法拆包，转换为unicode字符串

extract（） 
	提取seletor对象的值，如果提取不到值，会报错。
extract_first()
	提取seletor列表中的第一个值，如果取不到值，会返回一个空值
	返回第一个解析到的值，如果列表为空，此种方法也不会报错
```



## 三、操作

> 解析后输出到文件

```shell
#　输出json文件
scrapy crawl qb -o qb.json
#　输出csv文件
scrapy crawl qb -o qb.csv
#　输出xml文件
scrapy crawl qb -o qb.xml
```

## 四、原理

> 由四部分组成
>
> spider 、 调度器（schedluer）、下载器（downloader）和管道（pipline） .

```shell
1. spider向引擎提供一个url
2. 引擎把url传给调度器，调度器定制请求对象。把定制好的请求对象传给下载器
3. 下载器根据请求对象从互联网下载数据
4. 下载的数据再由spider通过xpath解析
5. 解析完的数据最后由管道保存到文件或者数据库
```

## 五、知识点

> 管道的用法pipeline

```shell
1. 默认是关闭的，可以再settings文件中打开

2. 在pipeline这个方法中 item是一个一个的数据，比如解析返回一个list,那么item就是list中的一个值

3. 写文件可以重写一个open_spider() 方法，只打开一次数据库连接、文件等
				  close_spider()
4. 在setting文件中可以指定多个管道，来达到多线成下载的效果
# 数字代表优先级，越小优先级越高。1-1000之间
ITEM_PIPELINES = {
   'dang.pipelines.DangPipeline': 300, 
   'dang.pipelines.自定义的类':299 
}
```

```python
# 高效的文件和数据库写入数据，不必频繁的打开连接
class DangPipeline:

    def open_spider(self,spider):
        self.file = open('dang.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 保存到文件中
        self.file.write(str(item))
        # print('oooooooooooooooooooooooooooooooooooooooooooooooo')
        # print(item)
        return item

    def close_spider(self,spider):
        self.file.close()
```
> 日志设置
```shell
# 设置日志等级 在settings文件中加上
LOG_LEVEL='WARNING'
# 设置日志保存到文件
LOG_FILE='mylog.log'
```
## 六、post请求

```
1. 因为是post请求，所以start_urls 和 parse方法都不能用 需要注释掉
2. 重写start_requests(self): 方法
```



```python
    def start_requests(self):
        print('----------------------------------------------------------------')
        data = {
            'from': 'zh',
            'to': 'en',
            'query': '学习',
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': '275626.55195',
            'token': '68d4ed11037dec8908a979268942b0eb',
            'domain': 'common'
        }

        headers = {
            'cookie': 'xxxxxxxxx'
        }
        url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.second_parse, headers=headers)

```

## 七、代理



```shell
1. 打开settings文件中的 downloader middlewares
#DOWNLOADER_MIDDLEWARES = {
#    'demopost.middlewares.DemopostDownloaderMiddleware': 543,
#}
2. 在middlewares.py文件中写代码
 def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        request.meta['proxy']='xxxxxx:8888'
        return None
```




























