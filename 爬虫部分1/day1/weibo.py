import urllib.request
import requests

url = 'https://m.weibo.cn/profile/info?uid=5313585008'

headers = {
    "accept": " application/json, text/plain, */*",
    "accept-encoding": " gzip, deflate, br",
    "accept-language": " zh-CN,zh;q=0.9",
    "cookie": " SUB=_2A25yUZQUDeRhGeNN6lEU-CvMyzSIHXVRvTxcrDV6PUNbktANLWTYkW1NScO_NiLA65LeE-netViIPQw3HwUwdOTQ; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFuq.loq7.msJ.2k6AnP4ym5JpX5KzhUgL.Fo-0eKef1h-7ehn2dJLoIEXLxK-L1K5LBonLxKqLB-BLB.zLxK.L1hzLBKeLxKBLBonLB-2LxK-L1KqLBo-t; SUHB=079TB8IPo5ms4V; SSOLoginState=1599464516; ALF=1602056516; _T_WM=54838147013; MLOGIN=1; WEIBOCN_FROM=1110106030; M_WEIBOCN_PARAMS=lfid%3D2304135313585008_-_WEIBO_SECOND_PROFILE_WEIBO%26luicode%3D20000174%26uicode%3D20000174; XSRF-TOKEN=48ff60",
    "mweibo-pwa": " 1",
    "referer": " https://m.weibo.cn/profile/5313585008",
    "sec-fetch-mode": " cors",
    "sec-fetch-site": " same-origin",
    "user-agent": " Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
    "x-requested-with": " XMLHttpRequest",
    "x-xsrf-token": " 48ff60"
}
response = requests.get(url, headers)
# reque = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(reque)
# print(response.text)
# print(response)
# print(response.content)

# content = response.read().decode('utf-8')
# with open('weibo.html', 'w', encoding='utf-8') as file:
#     file.write(content)
