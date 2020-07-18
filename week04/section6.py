'''
pandas基本操作
Pandas 计算功能操作文档：
https://pandas.pydata.org/docs/user_guide/computation.html#method-summary
'''
import pandas as pd
df = pd.DataFrame([
                    [1,2,3,4],
                    [5,1,7,None],
                    [3,4,8,8]
                  ],
                  index = ['one','two', 'three'],
                  columns = ['A', 'B', 'C', 'D']
                )

# print(df['A']+df['B'])  # 计算'A'列和'B'的和
# print(df['A'] + 5)
# print(df['A'] < df['B'])
# print(df.count())
print(df.sum())  # 计算每一列的和
