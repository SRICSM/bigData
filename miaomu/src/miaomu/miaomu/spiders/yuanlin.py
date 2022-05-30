import scrapy

class YuanlinSpider(scrapy.Spider):
    name = 'yuanlin'
    allowed_domains = ['yuanlin.com']
    start_urls = ['https://www.yuanlin.com/mmbj/']
    page = 1
    handle_httpstatus_list = [404]

    def parse(self, response):
        if response.status == 200:
            # 产品名称
            product_name = response.xpath(
                '//table[@class="mmbj_list_tb"]//tr[position() > 1]//td[1]//a//text()').extract()
            # print(len(product_name), product_name)
            # 米径
            rice_dia = []
            for i in response.xpath('//table[@class="mmbj_list_tb"]//tr[position() > 1]//td[2]'):
                dat = i.xpath('./text()').extract_first()
                if i.xpath('./text()').extract_first() is None:
                    rice_dia.append('')
                else:
                    rice_dia.append(dat)
            # print(len(rice_dia), rice_dia)
            # 高度
            height = []
            for i in response.xpath('//table[@class="mmbj_list_tb"]//tr[position() > 1]//td[3]'):
                dat = i.xpath('./text()').extract_first()
                if dat is None:
                    height.append('')
                else:
                    height.append(dat)
            # print(len(height), height)
            # 冠幅
            width = []

            for i in response.xpath('//table[@class="mmbj_list_tb"]//tr[position() > 1]//td[4]'):
                dat = i.xpath('./text()').extract_first()

                if dat is None:
                    width.append('')
                else:
                    width.append(dat)
            # print(len(width), width)
            # 地径
            ground_dia = []
            for i in response.xpath('//table[@class="mmbj_list_tb"]//tr[position() > 1]//td[5]'):
                dat = i.xpath('./text()').extract_first()
                if dat is None:
                    ground_dia.append('')
                else:
                    ground_dia.append(dat)
            # print(len(ground_dia), ground_dia)
            # 价格
            price = []
            for i in response.xpath('//table[@class="mmbj_list_tb"]//tr[position() > 1]//td[6]'):
                dat = i.xpath('./text()').extract_first()
                if dat is None:
                    price.append('')
                else:
                    price.append(dat)
            # print(len(price), price)
            # 单位
            unit = []
            for i in response.xpath('//table[@class="mmbj_list_tb"]//tr[position() > 1]//td[7]'):
                dat = i.xpath('./text()').extract_first()
                if dat is None:
                    unit.append('')
                else:
                    unit.append(dat)

            # print(len(unit), unit)
            # 提供商
            provider = response.xpath(
                '//table[@class="mmbj_list_tb"]//tr[position() > 1]//td[8]//div[@class="user_div"]//a[1]//text()').extract()

            print(len(provider), provider)
            data = zip(product_name, rice_dia, height, width, ground_dia, price, unit, provider)
            for d in data:
                yield {'product_name': d[0], 'rice_dia': d[1], 'height': d[2], 'width': d[3],
                       'ground_dia': d[4], 'price': d[5], 'unit': d[6], 'provider': d[7],
                       }

        # 下一页
        # next_page = response.xpath('//*[@id="WxfPageControl1"]//a[@class="page-next"]//@href').extract_first()
        self.page += 1
        if self.page <= 16856:
            url = f"https://www.yuanlin.com/mmbj/{self.page}.html"
            yield scrapy.Request(url=url, callback=self.parse)
