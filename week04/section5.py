'''
pandas的数据调整
DataFrame 学习文档：
https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
'''
import pandas as pd

df = pd.DataFrame([
                    [1,2,3,4],
                    [5,6,7,None],
                    [3,4,8,8]
                  ],
                  index = ['one','two', 'three'],
                  columns = ['A', 'B', 'C', 'D']
                )
# 1.列的选择
# print(df[ ['A','C'] ])  # 拿到'A','C'两列
# print(df.iloc[0:1, [0,2]])  # 拿到指定行,第一行的'A','C'两列, [0,1)
# print(df.iloc[0:3])
print(df['A'].agg('count'))
# 2.行的选择
# print(df.loc['one':'three'])  # 拿到'one'到'three'行
# print(df.loc[['one','three']])  # 拿到第一行和第三行

# 3.比较
# print(df[df['A'] < 5])  # 拿到'A'列中小于5的所有行
# print(df[(df['A'] < 5) & (df['C'] > 4)])  # 拿到'A'列中小于5,并且'C'列中大于4的所有行

# 4.对单个异常值处理

# print(df['C'].replace(7, 70))  # 将'C'列中的7换成70， 只返回'C'列的数据

# 空值替换
# import numpy as np
# print(df.replace(np.NaN, 0))

# 多值替换
# print(df.replace([3,5,7], 100))  # 将里面3,5,7替换为100
# print(df.replace( {4:400, 8:800} ))  # 将4替换为400,8替换成800

# 5.排序
# print(df.sort_values(by = ['A'], ascending = False))  # 按'A'列降序排序
# print(df.sort_values(by = ['A', 'B'], ascending = [False, True]))

# 6.删除
# print(df.drop('A', axis = 1))  # 删除指定列
# print(df.drop('one', axis = 0)) # 删除指定行
# print(df[ df['A'] > 3])  # 删除满足条件的行

# 7.行列互换
# print(df.T)
# print(df.T.T)

# 8.数据透视化
# print(df.stack())  # 以行为单位入栈
# print(df.unstack()) # 以列为单位入栈
# print(df.stack().reset_index())
