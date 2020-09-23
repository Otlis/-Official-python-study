import scrapy


class BtSpider(scrapy.Spider):
    name = 'bt'
    allowed_domains = ['fanyi.baidu.com']

    # start_urls = ['http://https://fanyi.baidu.com/v2transapi?from=zh/']
    #
    # def parse(self, response):
    #     pass

    # 因为是post请求所以 start_urls 和 parse方法不能用，需要自己写
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
            'cookie': 'BIDUPSID=4ECBE83C4D3E7EFD8B941DF069A788FC; PSTM=1587978534; BAIDUID=4ECBE83C4D3E7EFDE62A33A837EA73E3:SL=0:NR=10:FG=1; BDUSS=5oMTFUWkxJLTB5R0tURldSWG1INVdrNklCdlpDRFk3UXc1S3Z2YVRJbzNldGRlRVFBQUFBJCQAAAAAAAAAAAEAAAAiJ0YvwarP69Ch0KEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADftr1437a9ean; BDUSS_BFESS=5oMTFUWkxJLTB5R0tURldSWG1INVdrNklCdlpDRFk3UXc1S3Z2YVRJbzNldGRlRVFBQUFBJCQAAAAAAAAAAAEAAAAiJ0YvwarP69Ch0KEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADftr1437a9ean; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1600220655,1600825416; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1600825416; __yjsv5_shitong=1.0_7_c772622835794efe0a004c6a8926a322bc32_300_1600825416170_124.64.18.79_f2e881ee; yjs_js_security_passport=9685c8e73842299fbe3cce0be5235e37245ac665_1600825419_js',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
        }
        url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.second_parse, headers=headers)


    def second_parse(self, response):
        print(response.text)
