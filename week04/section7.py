'''
pandas分组与聚合
'''
import pandas as pd
import numpy as np
sales = [{'account': 'Jones LLC','type':'a', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co','type':'b',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc','type':'a',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]
df = pd.DataFrame(sales)
# print(df.groupby('type').groups)
# >>> {'b': Int64Index([1], dtype='int64'), 'a': Int64Index([0, 2], dtype='int64')}
# for a,b in df.groupby('type'):  #打印分组信息
#     print(a)
#     print(b)

# res = df.groupby('type').aggregate({'type':'count', 'Feb':'sum'})
# 按照'type'分为a,b两组，以a，b别作为行索引，将分组的'type'列求个数作为第一列，'Feb'列求和作为第二列，
# print(res)
# >>>:
#       Feb  type
# type
# a     290     2
# b     210     1
group=['x','y','z']
data=pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "salary":np.random.randint(5,50,10),
    "age":np.random.randint(15,50,10)
    })
print(data)
# res = data.groupby('group').agg('mean')  # 以'group'分组，求各组的年龄和薪资平均值
# print(res)

# res = data.groupby('group').mean().to_dict()  # 等价与上面
# print(res)

# res = data.groupby('group').transform('mean')
# print(res)

res = pd.pivot_table(data,
               values='salary',
               columns='group',
               index='age',
               aggfunc='count',
               margins=True
            ).reset_index()
print(res)
