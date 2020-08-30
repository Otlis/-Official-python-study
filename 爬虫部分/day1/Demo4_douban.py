from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = 'https://movie.douban.com/j/chart/top_list?'

data = {
    'type': 5,
    'interval_id': '100%3A90',
    'action': '',
    'start': '20',
    'limit': '20'
}
headers = {
    'Cookie': 'bid=0EcQwFAILaA; ll="108288"; _ga=GA1.2.120320743.1596163562; _vwo_uuid_v2=DF81655DB664F86413030A825D8A635A1|7a1719d6332639a9c7d67606b39beb2f; _gid=GA1.2.17320288.1598021982; __utma=30149280.120320743.1596163562.1596163577.1598022032.2; __utmc=30149280; __utmz=30149280.1598022032.2.2.utmcsr=dogedoge.com|utmccn=(referral)|utmcmd=referral|utmcct=/results; __utmt=1; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1598022036%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.120320743.1596163562.1596163577.1598022036.2; __utmb=223695111.0.10.1598022036; __utmc=223695111; __utmz=223695111.1598022036.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_t1=1; __utmb=30149280.10.8.1598022054476; _pk_id.100001.4cf6=6fbc0c1d6c1bc130.1596163577.2.1598022054.1596163577.; RT=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def find_top():
    real_url = url + urlencode(data)
    response = urlopen(Request(real_url, headers=headers))
    print(response.code)
    with open('../pages/a.html', 'w+b') as f:
        da = response.read()
        f.write(da)

find_top()
