import requests


# https://beijing.anjuke.com/community/?from=navigation
def download(url):
    resp = requests.get(url, params={'from': 'navigation'})
    if resp.status_code == 200:
        return resp.text  # 文本  resp.content
    else:
        return 'haha'


print(download('https://beijing.anjuke.com/community/'))

