from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
import pymysql
import json
from collections import Counter

conn = pymysql.connect(host='localhost', port=3306, db='stu_2', user='root', password='123456')

cursor = conn.cursor(pymysql.cursors.DictCursor)


# 首页 园林的数据
def index(request):
    return redirect('/yuanlin/')


# 数据统计
def showpic(requset):
    # 获取价格和米径
    cursor.execute('select rice_dia, price from yuanlin')


    #for i in cursor.fetchall():
    #if i['rice_dia']！=Null:
    #    if int(i['rice_dia'])< 1000:
    #        data.append((int(i.get('rice_dia')), float(i.get('price'))))

    data = [(eval(i.get('rice_dia')), float(i.get('price'))) for i in cursor.fetchall() if
            i['rice_dia'] and eval(i['rice_dia'])< 1000]

    cursor.execute('select rice_dia, price from huamu')
    data_1 = [(eval(i.get('rice_dia')), float(i.get('price'))) for i in cursor.fetchall() if
              i['rice_dia'] and eval(i['rice_dia']) < 1000]
    print(data_1)
    # 米径范围, 分五组
    # 0~19
    zero2ninety = []
    # 20~39
    twenty2thirytnine = []
    # 40~59
    forty2fivenine = []
    # 60~79
    sixty2sevennine = []
    # 80~99
    eigth2ninetynien = []
    # >100
    more_than_100 = []
    for r, p in data:
        if 0 <= r < 19:
            zero2ninety.append(p)
        elif 20 <= r < 39:
            twenty2thirytnine.append(p)
        elif 40 <= r < 59:
            forty2fivenine.append(p)
        elif 60 <= r < 79:
            sixty2sevennine.append(p)
        elif 80 <= r < 99:
            eigth2ninetynien.append(p)
        else:
            more_than_100.append(p)
        # 米径范围, 分五组
        # 0~19
    zero2ninety_1 = []
    # 20~39
    twenty2thirytnine_1 = []
    # 40~59
    forty2fivenine_1 = []
    # 60~79
    sixty2sevennine_1 = []
    # 80~99
    eigth2ninetynien_1 = []
    # >100
    more_than_100_1 = []
    for r, p in data_1:
        if 0 <= r < 19:
            zero2ninety_1.append(p)
        elif 20 <= r < 39:
            twenty2thirytnine_1.append(p)
        elif 40 <= r < 59:
            forty2fivenine_1.append(p)
        elif 60 <= r < 79:
            sixty2sevennine_1.append(p)
        elif 80 <= r < 99:
            eigth2ninetynien_1.append(p)
        else:
            more_than_100_1.append(p)
    # print(zero2ninety)
    # 求平均价格
    rice_price = [['0-19公分', int(sum(zero2ninety) / len(zero2ninety)), int(sum(zero2ninety_1) / len(zero2ninety_1))],
                  ['20-39公分', int(sum(twenty2thirytnine) / len(twenty2thirytnine)),
                   int(sum(twenty2thirytnine_1) / len(twenty2thirytnine_1))],
                  ['40-59公分', int(sum(forty2fivenine) / len(forty2fivenine)),
                   int(sum(forty2fivenine_1) / len(forty2fivenine_1))],
                  ['60-79公分', int(sum(sixty2sevennine) / len(sixty2sevennine)),
                   int(sum(sixty2sevennine_1) / len(sixty2sevennine_1))],
                  ['80-99公分', int(sum(eigth2ninetynien) / len(eigth2ninetynien)),
                   int(sum(eigth2ninetynien_1) / len(eigth2ninetynien_1))],
                  ['大于100公分', int(sum(more_than_100) / len(more_than_100)),
                   int(sum(more_than_100_1) / len(more_than_100_1))]
                  ]
    # print(rice_price)

    # 获取价格与高度
    cursor.execute('select height, price from yuanlin')
    data = [(int(i.get('height')), float(i.get('price'))) for i in cursor.fetchall() if
            i['height'] and int(i['height']) < 10000]
    cursor.execute('select height, price from huamu')
    data_1 = [(eval(i.get('height')), float(i.get('price'))) for i in cursor.fetchall() if
              i['height'] and eval(i['height']) < 10000]
    # print(data, len(data))
    # 高度范围
    # 1~299
    height_1 = []
    # 300~449
    height_3 = []
    # 450-599
    height_4 = []
    # 600-749
    height_5 = []
    # 大于等于750
    height_6 = []
    for r, p in data:
        if 1 <= r < 299:
            height_1.append(p)
        elif 300 <= r < 449:
            height_3.append(p)
        elif 450 <= r < 599:
            height_4.append(p)
        elif 600 <= r < 749:
            height_5.append(p)
        else:
            height_6.append(p)
    # 1~299
    height_1_1 = []
    # 300~449
    height_3_1 = []
    # 450-599
    height_4_1 = []
    # 600-749
    height_5_1 = []
    # 大于等于750
    height_6_1 = []
    for r, p in data_1:
        if 1 <= r < 299:
            height_1_1.append(p)
        elif 300 <= r < 449:
            height_3_1.append(p)
        elif 450 <= r < 599:
            height_4_1.append(p)
        elif 600 <= r < 749:
            height_5_1.append(p)
        else:
            height_6_1.append(p)
    # 求平均价格
    height_price = [['1-299公分', int(sum(height_1) / len(height_1)), int(sum(height_1_1) / len(height_1_1))],
                    ['300-449公分', int(sum(height_3) / len(height_3)), int(sum(height_3_1) / len(height_3_1))],
                    ['450-599公分', int(sum(height_4) / len(height_4)), int(sum(height_4_1) / len(height_4_1))],
                    ['600-749公分', int(sum(height_5) / len(height_5)), int(sum(height_5_1) / len(height_5_1))],
                    ['大于750公分', int(sum(height_6) / len(height_6)), int(sum(height_6_1) / len(height_6_1))]
                    ]

    # 获取价格和冠幅
    cursor.execute('select width, price from yuanlin')
    data = [(int(i.get('width')), float(i.get('price'))) for i in cursor.fetchall() if
            i['width'] and int(i['width']) < 10000]
    cursor.execute('select width, price from huamu')
    data_1 = [(eval(i.get('width')), float(i.get('price'))) for i in cursor.fetchall() if
              i['width'] and eval(i['width']) < 10000]
    # print(max([i[0] for i in data]), min([i[0] for i in data]))
    # 宽度范围
    # 1~199
    width_1 = []
    # 200~399
    width_2 = []
    # 400-599
    width_3 = []
    # 600-799
    width_4 = []
    # 800-999
    width_5 = []
    # 大于1000
    width_6 = []
    for r, p in data:
        if 1 <= r < 199:
            width_1.append(p)
        elif 200 <= r < 399:
            width_2.append(p)
        elif 400 <= r < 599:
            width_3.append(p)
        elif 600 <= r < 799:
            width_4.append(p)
        elif 800 <= r < 999:
            width_5.append(p)
        else:
            width_6.append(p)
    # 1~199
    width_1_1 = []
    # 200~399
    width_2_1 = []
    # 400-599
    width_3_1 = []
    # 600-799
    width_4_1 = []
    # 800-999
    width_5_1 = []
    # 大于1000
    width_6_1 = []
    for r, p in data_1:
        if 1 <= r < 199:
            width_1_1.append(p)
        elif 200 <= r < 399:
            width_2_1.append(p)
        elif 400 <= r < 599:
            width_3_1.append(p)
        elif 600 <= r < 799:
            width_4_1.append(p)
        elif 800 <= r < 999:
            width_5_1.append(p)
        else:
            width_6_1.append(p)
    # print(width_1)
    # 求平均价格
    width_price = [['1-199公分', int(sum(width_1) / len(width_1)), int(sum(width_1_1) / len(width_1_1))],
                   ['200-399公分', int(sum(width_2) / len(width_2)), int(sum(width_2_1) / len(width_2_1))],
                   ['400-599公分', int(sum(width_3) / len(width_3)), int(sum(width_3_1) / len(width_3_1))],
                   ['600-799公分', int(sum(width_4) / len(width_4)), int(sum(width_4_1) / len(width_4_1))],
                   ['800-999公分', int(sum(width_5) / len(width_5)), int(sum(width_5_1) / len(width_5_1))],
                   ['大于1000公分', int(sum(width_6) / len(width_6)), int(sum(width_6_1) / len(width_6_1))]
                   ]
    print(width_price)

    # 获取宽度和价格
    cursor.execute('select ground_dia, price from yuanlin')
    data = [(int(i.get('ground_dia')), float(i.get('price'))) for i in cursor.fetchall() if
            i['ground_dia'] and int(i['ground_dia']) < 600]

    cursor.execute('select ground_dia, price from huamu')
    data_1 = [(eval(i.get('ground_dia')), float(i.get('price'))) for i in cursor.fetchall() if
              i['ground_dia'] and not i['ground_dia'].startswith('0') and eval(i['ground_dia']) < 600]
    # print(max([i[0] for i in data]), min([i[0] for i in data]))
    # 宽度范围
    # 0~19
    ground_1 = []
    # 20~39
    ground_2 = []
    # 40-59
    ground_3 = []
    # 60-79
    ground_4 = []
    # 80-99
    ground_5 = []
    # 大于100
    ground_6 = []
    for r, p in data:
        if 1 <= r < 19:
            ground_1.append(p)
        elif 20 <= r < 39:
            ground_2.append(p)
        elif 40 <= r < 59:
            ground_3.append(p)
        elif 60 <= r < 79:
            ground_4.append(p)
        elif 80 <= r < 99:
            ground_5.append(p)
        else:
            ground_6.append(p)
    # 0~19
    ground_1_1 = []
    # 20~39
    ground_2_1 = []
    # 40-59
    ground_3_1 = []
    # 60-79
    ground_4_1 = []
    # 80-99
    ground_5_1 = []
    # 大于100
    ground_6_1 = []
    for r, p in data_1:
        if 1 <= r < 19:
            ground_1_1.append(p)
        elif 20 <= r < 39:
            ground_2_1.append(p)
        elif 40 <= r < 59:
            ground_3_1.append(p)
        elif 60 <= r < 79:
            ground_4_1.append(p)
        elif 80 <= r < 99:
            ground_5_1.append(p)
        else:
            ground_6_1.append(p)
    # print(width_1)

    # 求平均价格
    ground_price = [['1-19公分', int(sum(ground_1) / len(ground_1)), int(sum(ground_1_1) / len(ground_1_1))],
                    ['20-39公分', int(sum(ground_2) / len(ground_2)), int(sum(ground_2_1) / len(ground_2_1))],
                    ['40-59公分', int(sum(ground_3) / len(ground_3)), int(sum(ground_3_1) / len(ground_3_1))],
                    ['60-79公分', int(sum(ground_4) / len(ground_4)), int(sum(ground_4_1) / len(ground_4_1))],
                    ['80-99公分', int(sum(ground_5) / len(ground_5)), int(sum(ground_5_1) / len(ground_5_1))],
                    ['大于100公分', int(sum(ground_6) / len(ground_6)), int(sum(ground_6_1) / len(ground_6_1))]
                    ]
    # print(ground_price)
    # print(height_price)

    # 从数据库中获取价格
    cursor.execute('select price from yuanlin')

    data = [float(i.get('price')) for i in cursor.fetchall()]
    cursor.execute('select price from huamu')
    data_1 = [float(i.get('price')) for i in cursor.fetchall()]
    result = {'0-49元': 0, '50-99元': 0, '100-199元': 0, '200-499元': 0, '500-999元': 0, '>1000元': 0}
    result_1 = {'0-49元': 0, '50-99元': 0, '100-199元': 0, '200-499元': 0, '500-999元': 0, '>1000元': 0}

    # 将data里面的数据进行处理放入数组中
    for d in data:
        if 0 <= d < 49:
            result['0-49元'] += 1
        elif 50 <= d < 99:
            result['50-99元'] += 1
        elif 100 <= d < 199:
            result['100-199元'] += 1
        elif 200 <= d < 499:
            result['200-499元'] += 1
        elif 500 <= d < 999:
            result['500-999元'] += 1
        else:
            result['>1000元'] += 1

        # 处理data_1里面的数据进行处理放入数组中

    for d in data_1:
        if 0 <= d < 49:
            result_1['0-49元'] += 1
        elif 50 <= d < 99:
            result_1['50-99元'] += 1
        elif 100 <= d < 199:
            result_1['100-199元'] += 1
        elif 200 <= d < 499:
            result_1['200-499元'] += 1
        elif 500 <= d < 999:
            result_1['500-999元'] += 1
        else:
            result_1['>1000元'] += 1
    return render(requset, 'index.html',
                  {'rice2price': rice_price, 'height2price': height_price,
                   'width2price': width_price,
                   'ground2price': ground_price,
                   'yuanlin_price': list(result.items()),
                   'huamu_price': list(result_1.items())
                   })


# 苗木类型统计分析
def miaomu_types(requeset):
    # 从数据库中获取苗木种类
    query = "select product_name from yuanlin"
    cursor.execute(query)
    data = [i.get('product_name') for i in cursor.fetchall()]
    # print(data)
    counter = Counter(data)
    data = counter.most_common(100)
    print(data)
    # address = ['河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '海南', '四川',
    #            '贵州', '云南', '陕西', '甘肃', '青海', '广西', '西藏', '北京', '天津', '上海', '重庆']

    # 地区供应苗木统计
    cursor.execute('select provider from yuanlin union select provider from huamu')
    addr_nums = [i.get('provider')[:2] for i in cursor.fetchall()]
    # print(len(addr_nums))
    # print(addr_nums)
    addr_counter = Counter(addr_nums)
    # print(addr_counter)
    addr_data = [(i, j) for i, j in addr_counter.items() if j >= 9]
    # print(list(counter.items()))
    print(addr_data)
    # data = list(zip([i.strip() for i in counter.keys()], counter.values()))
    return render(requeset, 'miaomu_types.html', {'test': data, 'addr_nums': addr_data})


# 价格统计分析
def price(request):
    # 从数据库中获取价格
    query = "select price from yuanlin"
    cursor.execute(query)

    data = [float(i.get('price')) for i in cursor.fetchall()]
    result = {'0-49元': 0, '50-99元': 0, '100-199元': 0, '200-499元': 0, '500-999元': 0, '>1000元': 0}
    for d in data:
        if 0 <= d < 49:
            result['0-49元'] += 1
        elif 50 <= d < 99:
            result['50-99元'] += 1
        elif 100 <= d < 199:
            result['100-199元'] += 1
        elif 200 <= d < 499:
            result['200-499元'] += 1
        elif 500 <= d < 999:
            result['500-999元'] += 1
        else:
            result['>1000元'] += 1
    # print(result)
    return render(request, 'price.html', {'data': list(result.items())})


def yuanlin(request):
    # return HttpResponse('hello world')
    return render(request, 'yuanlin.html')


def huamu(request):
    return render(request, 'huamu.html')


kw = None
name = None

# 定义count为全局变量
count = None


def search(request):
    global kw
    global name
    global count
    name = request.GET.get('name')
    print(name)
    kw = request.GET.get('kw')
    # print(kw)
    # 查询的结果数量
    cursor.execute(f"select count(*) from {name} where concat(product_name, provider) like '%{kw}%'")
    count = cursor.fetchall()[0].get('count(*)')
    print(count)
    return render(request, 'search.html', {'count': count, 'name': name})


# 搜索接口
def search_data(request):
    global kw
    print(request.GET)
    print(kw)
    global name
    # 第几页
    page = int(request.GET.get('page'))
    # 数量
    limit = int(request.GET.get('limit'))
    if kw is not None:
        query = f"select * from {name} where concat(product_name, provider) like '%{kw}%' limit {limit} offset {(page - 1) * limit}"
        # print(query)
        cursor.execute(query)
        data = cursor.fetchall()
        # print(data)  再此处修改了count 实现按实际搜索数量渲染layui里面的表格
        return HttpResponse(json.dumps({"code": 0, "msg": "", "count": count,
                                        "data": data}
                                       ))
    else:
        return HttpResponse('<h3 style="text-align: center">没有找到相关结果!</h3>')


# json接口获取数据
def get_data(request):
    path = request.get_full_path().split('/')[1]
    print(path)
    # 向数据库获取数据
    print(request.GET)
    # 第几页
    page = int(request.GET.get('page'))
    # 数量
    limit = int(request.GET.get('limit'))
    query = f"select * from {path} limit {limit} offset {(page - 1) * limit}"
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    # 只取了1000条数据 实际数据量多于1000
    return HttpResponse(json.dumps({"code": 0, "msg": "", "count": 1000,
                                    "data": data}
                                   ))
