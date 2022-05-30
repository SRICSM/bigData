# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

'''
创建数据库
create database Stu_2 charset utf8mb4;
创建表
create table yuanlin(
    product_name VARCHAR(64),
    rice_dia VARCHAR(64),
    height VARCHAR(64),
    width VARCHAR(64),
    ground_dia VARCHAR(64),
    price VARCHAR(64),
    unit VARCHAR(32),
    provider VARCHAR(128)
    );
---创建花木网的表
create table huamu(
    product_name VARCHAR(64),
    rice_dia VARCHAR(64),
    height VARCHAR(64),
    width VARCHAR(64),
    ground_dia VARCHAR(64),
    price VARCHAR(64),
    unit VARCHAR(32),
    provider VARCHAR(128)
    );
'''
class MiaomuPipeline:
    # 打开数据库
    def open_spider(self, spider):
        self.db_conn = pymysql.connect(host='localhost', port=3306, db='Stu_2', user='root', passwd='123456')
        self.db_cur = self.db_conn.cursor()

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self, item, spider):
        # if spider.name == 'yuanlin':
        query = f"select * from {spider.name} where product_name = %s and rice_dia = %s and width = %s and height = %s"
        self.db_cur.execute(query, (item['product_name'], item['rice_dia'], item['width'], item['height']))
        result = self.db_cur.fetchone()
        if result:
            update_query = f"update {spider.name} set ground_dia = %s ,price= %s ,unit = %s, provider = %s where " \
                           f"product_name = %s and rice_dia = %s and width = %s and height = %s "
            self.db_cur.execute(update_query, (
                item['ground_dia'], item['price'], item['unit'], item['provider'], item['product_name'],
                item['rice_dia'],
                item['width'], item['height']))
            self.db_conn.commit()
            print(f"{item['product_name']}, {item['provider']}更新成功!")
        else:
            self.insert(item, spider.name)
        # elif spider.name == 'huamu':
        #     query = "select * from huamu where product = %s and expire = %s and count = %s"
        #     self.db_cur.execute(query, (item['title'], item['expire'], item['nums']))
        #     result = self.db_cur.fetchone()
        #     if result:
        #         update_query = "update huamu set height = %s ,rice_dia= %s ,ground_dia = %s, width = %s, source = %s where title = %s and expire = %s and count = %s"
        #         self.db_cur.execute(update_query, (
        #             item['height'], item['rice_dia'], item['ground_dia'], item['width'], item['source'],
        #             item['title'],
        #             item['expire'], item['nums']))
        #         self.db_conn.commit()
        #         print(f"{item['title']}, {item['source']}更新成功!")
        #     else:
        #         self.insert(item, spider.name)
        return item

    def insert(self, item, table_name):
        try:
            sql = f'INSERT INTO {table_name} VALUES({",".join((["%s"] * len(item)))})'
            print(sql)
            print(item.values())
            self.db_cur.execute(sql, tuple(item.values()))
            self.db_conn.commit()
            print("插入成功!")
        except Exception as e:
            print("插入失败!")
            self.db_conn.commit()
