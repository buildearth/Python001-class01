# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MoviesPipeline:
    db_info = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123',
            'db': 'movies',
        }
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host = self.db_info['host'],
            port = self.db_info['port'],
            user = self.db_info['user'],
            password = self.db_info['password'],
            db = self.db_info['db'])
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        try:
            sql_command = 'INSERT INTO Douban(star,short) VALUES ("{star}","{short}");'.format(
                    short = item['short'], star = item['star'])
            self.cur.execute(sql_command)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        # return item


# create table Douban(
#     star varchar(5),
#     short varchar(300))comment = 'douban_movie_table' ENGINE=InnoDB DEFAULT CHARSET=utf8;
