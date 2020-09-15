"""
应用：百度翻译
-urllibe.request.Request
-urllibe.request.urlopen()
-urllib.parse.urlencode()
"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en?'
data = {
    # 'from': 'zh',
    # 'to': 'en',
    'query': '你好'
    # 'simple_means_flag': 3,
    # 'sign': 232427.485594,
    # 'token': '5df686e15b2ab116d7cc57896c72b429',
    # 'domain': 'common'
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'cookie': 'BIDUPSID=1FE37DBC7353E989CC144891CC891247; PSTM=1595935211; BAIDUID=1FE37DBC7353E989C51A17D5AB6DD0AA:FG=1; BDUSS=1SLWhGYVljUUR1OHQyRFkxUGVIS2Roam5obUF0ODNxRmhabWUxS2VNVkV1VWRmRVFBQUFBJCQAAAAAAAAAAAEAAAAiJ0YvwarP69Ch0KEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQsIF9ELCBfMk; BDUSS_BFESS=1SLWhGYVljUUR1OHQyRFkxUGVIS2Roam5obUF0ODNxRmhabWUxS2VNVkV1VWRmRVFBQUFBJCQAAAAAAAAAAAEAAAAiJ0YvwarP69Ch0KEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQsIF9ELCBfMk; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1598017179; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1598017356; __yjsv5_shitong=1.0_7_e60e5a3b4619812dd5bece3bd0103853c6ee_300_1598017356338_61.48.208.173_b8a63d09; yjs_js_security_passport=7b5269cc43d70bf87bcad3dae8f33df27b4a670d_1598017358_js',
    'x-requested-with': 'XMLHttpRequest'
}

import json


def fanyi():
    req = Request(url, data=urlencode(data).encode('utf-8'))
    response = urlopen(req)
    print(response.code)  # 响应吗200

    print(response.getheader('content-type'))  # 用这个可以找出格式
    content_encode = response.getheader('content-type')  # 用这个可以找出格式
    # content_encode = 'utf-8' if type is None else type.split('=')[-1]
    json_data = response.read()
    print(json.loads(json_data))


fanyi()
