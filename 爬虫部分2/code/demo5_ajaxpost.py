import urllib.request
import urllib.parse

# ajax post 爬取kfc餐厅地址
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
# 注意数据''引号里面不能有空格，可能会数据错误
data = {
    'cname': '北京',
    'pid': ' ',
    'pageIndex': '7',
    'pageSize': '10'
}
data = urllib.parse.urlencode(data).encode('utf-8')
headers = {
    # 'Accept': ' application/json, text/javascript, */*; q=0.01',
    # 'Accept-Language': ' zh-CN,zh;q=0.9',
    # 'Connection': ' keep-alive',
    # 'Content-Length': ' 53',
    # 'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': ' route-cell=ksa; Hm_lvt_1039f1218e57655b6677f30913227148=1600235563; Hm_lpvt_1039f1218e57655b6677f30913227148=1600235563; SERVERID=02f4c994014ba2083ffa81762e56b1a0|1600235665|1600235560',
    # 'Host': ' www.kfc.com.cn',
    # 'Origin: http': '//www.kfc.com.cn',
    # 'Referer: http': '//www.kfc.com.cn/kfccda/storelist/index.aspx',
    'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    # 'X-Requested-With': ' XMLHttpRequest'
}

request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
