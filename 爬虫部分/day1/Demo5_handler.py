"""
handler 可以定制更高级的请求头
1. 创建handler对象  handler=urllibe.request.HTTPHandler()
2. 创建opener对象  opener=urllibe.request.build_opener(*handler)
3. 创建Request对象
4. 发送Request请求  opener.open(req)
"""

from urllib.request import HTTPHandler, build_opener


def get(url):
    opener = build_opener(HTTPHandler())
    resp = opener.open(url)  # 返回整个网页
    # return resp
    # 现在要求返回一个对象，带有headers->dict  code->int  text文本 body->byte
    respdict = {'headers': dict(resp.headers), 'code': resp.code, 'body': resp.read()}
    try:
        encoding = resp.headers['Content-Type'].split('=')[-1]
    except:
        encoding = 'utf-8'
    respdict['encoding'] = encoding
    respdict['body'] = resp.read()
    respdict['text'] = resp.read().decode(encoding)

    return respdict


if __name__ == '__main__':
    resp = get('https://www.baidu.com/')
    # print(resp.read())
    print(resp['code'])
    print(resp['body'])
    # print(resp['text'])
    print(resp['headers'])
