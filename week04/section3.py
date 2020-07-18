'''
pandas 数据导入
'''
import pandas as pd
# txt文件导入
# x = pd.read_table('t1.txt', sep = ' ')
# print(x)

# 数据库导入
import pymysql
conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '123',
    db = 'qidian'
    )
sql = "select * from BookTop"

df = pd.read_sql(sql, conn)
# print(df.head(3))  # 显示前三行
# print(df.shape)  # 显示行列数量
# print(df.info())  # 每一列的信息
# print(df.describe())  # 表格的详细信息,
