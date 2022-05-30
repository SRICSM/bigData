import scrapy

#花木求购信息
class HuamuSpider(scrapy.Spider):
    name = 'huamu'
    allowed_domains = ['huamu.com']
    start_urls = ['https://m.huamu.com/qiugou']

    def start_requests(self):
        for p in range(1, 300):
            url = f"https://m.huamu.com/fenlei/9____{p}_changlvqiaomu_.html"
            cookies = {
                'refresh_times': '0',
                'last_time': '1621040576',
                'cookie_id': '0dfd1219c6615cf5aff899489e285b27',
                'HUAMU_ID': '93869c6aeefd459465fa874d6f33a77ca1aa6241',
                '__51cke__': '',
                'Hm_lvt_79ff8b04d2408694a6d3bf5a8f2d368e': '1620995019,1621040416',
                'Hm_lpvt_79ff8b04d2408694a6d3bf5a8f2d368e': '1621040458',
                'refresh_times': '0',
                'last_time': '1621040585',
                '__tins__16508866': '%7B%22sid%22%3A%201621040415467%2C%20%22vd%22%3A%205%2C%20%22expires%22%3A'
                                    '%201621042385320%7D',
                '__51laig__': '5'
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/89.0.4389.114 Safari/537.36',
                'Referer': 'https://m.huamu.com/fenlei/9_changlvqiaomu.html',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            }
            yield scrapy.Request(url=url, callback=self.parse, method='POST', body='ajax=1&lat=0&lon=0',
                                 headers=headers)

    def parse(self, response):
        response_text = response.json()
        if response_text['goods_list']:
            data = response_text['goods_list']
            print('----')
            print(data)
            for d in data:
                # print(d)
                # 提供商
                provider = d['store_name']
                # print(provider)
                # 产品名  可以将此处的产品名修改成pyType 变成品种类别，而不是无意义的描述信息 但是可能要修改爬虫结构，可以后期进行完善
                product_name = d['goods_name']
                # print(product_name)
                # 价格
                price = d['price']
                # print(price)
                # 单位
                unit = d['goods_unit']
                # print(unit)
                # 高度, 米径, 地径, 冠幅
                height, rice_dia, ground_dia, width = '', '', '', ''
                for j in d['attr']:
                    # 高度
                    if '高' in j:
                        height = j.split(':')[-1].split('公分')[0]
                    elif '米' in j:
                        rice_dia = j.split(':')[-1].split('公分')[0]
                    elif '地' in j:
                        ground_dia = j.split(':')[-1].split('公分')[0]
                    elif '冠' in j:
                        width = j.split(':')[-1].split('公分')[0]
                # print(height, width, ground_dia, rice_dia)
                yield {'product_name': product_name, 'rice_dia': rice_dia, 'height': height, 'width': width,
                       'ground_dia': ground_dia, 'price': price, 'unit': unit, 'provider': provider,
                       }
        # if response_text['status'] == 0:
        #     data = response_text['data']
        #     for d in data:
        #         # 标题
        #         title = d['cate_name']
        #         print(title)
        #         # 数量
        #         nums = str(list(d['requirements_spec'].values())[0]['num']) + str(
        #             list(d['requirements_spec'].values())[0]['unit'])
        #         print(nums)
        #
        #         # 苗源
        #         source = d['province']
        #         # 截止时间
        #         expire = d['formated_expire']
        #         yield {'title': title, 'rice_dia': rice_dia, 'height': height, 'width': width, 'ground_dia': ground_dia,
        #                'nums': nums,
        #                'source': source, 'expire': expire}
