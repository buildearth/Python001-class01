import pandas as pd
import numpy as np
'''
pandas 基本数据类型:
    Series
    DataFrame
'''
# 一.Series
# 1.用列表生成Series,Pandas 默认自动生成整数索引
# l = ['name', 'id', 'age']
# series = pd.Series(l)
# print(series)
# >>>>:
# 0    name
# 1      id
# 2     age
# print(np.random.randn(6, 4))

# 2.用字典的方式创建带索引的Series
# series = pd.Series({'a':'name', 'b':'id', 'c':'age'})
# print(series)
#  >>>>:
# a    name
# b      id
# c     age

# 3.用关键字指定的方式创建带索引的Series
# series = pd.Series([1,2,3], index = ['a', 'b', 'c'])
# print(series)
# >>>>:
# a    1
# b    2
# c    3

# 4.取出全部索引和全部值
# series = pd.Series([1,2,3], index = ['a', 'b', 'c'])
# print(series.index, type(series.index))
# print(series.values, type(series.values))

# # 转换成列表
# l = series.values.tolist()
# print(l, type(l))

# 5.结合正则,lambda取出email
# import re
# emails = pd.Series(['abc at amazom.com', 'admin1@163.com', 'mat@m.at', 'ab@abc.com'])
# pattern = '.*@\w+\.\w+'
# # print(re.findall(pattern, 'admin1@163.com'))
# mask = emails.map(lambda x: bool(re.match(pattern, x)))
# print(emails[mask])

# 二.DataFrame
# 1.列表创建
# df1 = pd.DataFrame(['a','b','c','d'])
# print(df1)
# >>>>:  创建出来只有一列的,自动添加行列的索引
#    0
# 0  a
# 1  b
# 2  c
# 3  d

# 2.嵌套列表的方式创建
df1 = pd.DataFrame([
        ['a','b'],
        ['c', 'd']
    ])
# print(df1)
# >>>>:
#    0  1
# 0  a  b
# 1  c  d
# 自定义列索引
df1.columns = ['one', 'two']
# 自定义行索引
df1.index = ['first', 'second']
# print(df1)
# >>>>:
#        one two
# first    a   b
# second   c   d

# 获取index,columns,values

# print(df1.index)
# print(df1.columns)
# print(df1.values)
