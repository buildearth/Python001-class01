# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
SQL_CREATE_TABLE = \
'''create table BookTop(
    name varchar(10),
    auth varchar(10),
    book_type varchar(10),
    update_status varchar(10),
    top_type varchar(10),
    intro varchar(300))comment = 'top_book_table' ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

class SystemProxyPipeline:
    def table_is_exist(self, cur, table_name):
        is_exist = False
        sql_command ='show tables'
        table_count = cur.execute(sql_command)
        tables_rel = cur.fetchall()
        print(tables_rel)
        for table  in tables_rel:
            if table_name in table:
                is_exist = True
                break

        return is_exist

    def open_spider(self, spider):
        self.db_info = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '123',
            'db': 'qidian',
        }

        self.conn = pymysql.connect(
            host = self.db_info['host'],
            port = self.db_info['port'],
            user = self.db_info['user'],
            password = self.db_info['password'],
            db = self.db_info['db']
            )

        # 数据库操作
        try:
            self.cur = self.conn.cursor()  # 获取游标
            #进行表是否存在的判定，存在直接添加数据，不存在创建表
            if not self.table_is_exist(self.cur, 'BookTop'):
                print('BookTop table not exist')
                self.cur.execute(SQL_CREATE_TABLE)
                self.conn.commit()
            #
        except Exception as e:
            print(e)
            self.conn.rollback()  # 回滚


    def close(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        print('-'*20)
        print('{name},{auth},{book_type},{update_status},{top_type},{intro}'.format(name = item['name'],
                        auth = item['auth'],
                        book_type = item['book_type'],
                        update_status = item['update_status'],
                        top_type = item['top_type'],
                        intro = item['intro']))
        try:
            sql_command = 'INSERT INTO BookTop(name,auth,book_type,update_status,top_type,intro) VALUES ("{name}","{auth}","{book_type}","{update_status}","{top_type}","{intro}");'.format(
                        name = item['name'],
                        auth = item['auth'],
                        book_type = item['book_type'],
                        update_status = item['update_status'],
                        top_type = item['top_type'],
                        intro = item['intro'])
            self.cur.execute(sql_command)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)

        return item
