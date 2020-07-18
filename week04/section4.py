'''
数据预处理:
    缺失值处理
    重复值处理
Series 学习文档：
https://pandas.pydata.org/pandas-docs/stable/reference/series.html
'''
import pandas as pd
# Series的处理
# s = pd.Series([1,None,2,None,None,5,8,None])
# print(s.hasnans)  # 检测是否有空值,出现空值返回True
# s1=s.fillna(value = s.mean())  # 空值填充指定值,不会有该原数据,返回一个新的Series对象
# print(s1)

# DataFrame的处理
# df = pd.DataFrame([
#     [1,2,None,4],
#     [5,None,6,None],
#     [7,8,9,10],
#     [None,None,None,None]

#     ])
# print(df)
# # print(df.isnull().sum())  # 统计每列的空值个数

# # 空值填充
# # df1 = df.ffill()  # 用上一行填充
# # print(df1)

# # df2 = df1.ffill(axis=1)
# # print(df2)

# # 缺失值删除
# print(df.info())
# df3 = df.dropna()  # 将有缺失值的行整行删除
# print(df3)


#重复值处理
df = pd.DataFrame([
    [1,2,3,4],
    [5,None,6,None],
    [1,2,3,4],
    [9,3,3,8],
    [7,8,9,10],
    [None,None,None,None]

    ])
# df2 = df.drop_duplicates()  # 删除重复的行
# print(df2)
print(df)
df3 = df.drop_duplicates(subset = 1)
print(df3)
