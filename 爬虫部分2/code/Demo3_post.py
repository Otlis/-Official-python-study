import urllib.request
import urllib.parse
# 百度翻译
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
data = {
    'from': ' en',
    'to': ' zh',
    'query': ' love',
    'transtype': ' translang',
    'simple_means_flag': ' 3',
    'sign': ' 198772.518981',
    'token': ' 68d4ed11037dec8908a979268942b0eb',
    'domain': ' common'
}

data = urllib.parse.urlencode(data).encode('utf-8')
headers = {
    # 'accept': ' */*',
    # 'accept-encoding': ' gzip, deflate, br',
    # 'accept-language': ' zh-CN,zh;q=0.9',
    # 'content-length': ' 136',
    # 'content-type': ' application/x-www-form-urlencoded; charset=UTF-8',
    'cookie':'BIDUPSID=4ECBE83C4D3E7EFD8B941DF069A788FC; PSTM=1587978534; BAIDUID=4ECBE83C4D3E7EFDE62A33A837EA73E3:SL=0:NR=10:FG=1; BDUSS=5oMTFUWkxJLTB5R0tURldSWG1INVdrNklCdlpDRFk3UXc1S3Z2YVRJbzNldGRlRVFBQUFBJCQAAAAAAAAAAAEAAAAiJ0YvwarP69Ch0KEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADftr1437a9ean; BDUSS_BFESS=5oMTFUWkxJLTB5R0tURldSWG1INVdrNklCdlpDRFk3UXc1S3Z2YVRJbzNldGRlRVFBQUFBJCQAAAAAAAAAAAEAAAAiJ0YvwarP69Ch0KEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADftr1437a9ean; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1600220655; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; yjs_js_security_passport=2048cbed25dd2baf44d96827c2bce916b072bcba_1600220654_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1600222352; __yjsv5_shitong=1.0_7_c772622835794efe0a004c6a8926a322bc32_300_1600222351259_124.64.18.219_024cf200',
    # 'origin: https': '//fanyi.baidu.com',
    # 'referer: https': '//fanyi.baidu.com/',
    # 'sec-fetch-dest': ' empty',
    # 'sec-fetch-mode': ' cors',
    # 'sec-fetch-site': ' same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    # 'x-requested-with': ' XMLHttpRequest'
}
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
