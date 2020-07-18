'''
2. pandas 中文文档：
https://www.pypandas.cn/
sklearn-pandas
3. 安装参考文档：
https://pypi.org/project/sklearn-pandas/1.5.0/
4. Numpy 学习文档：
https://numpy.org/doc/
5. matplotlib 学习文档：
https://matplotlib.org/contents.html
'''

'''
from sklearn import datasets
iris = datasets.load_iris()

x,y = iris.data, iris.target  # x是花的四个特征, y是哪种花

# print(iris.feature_names)  # 四个特征的名字,每一个特征分别表示什么
# print(iris.target_names)   # 查看花的名字


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size = 0.25)  # 将可迭代对象按照比例划分,test部分占4/4
'''

import pandas as pd
import numpy as np  # 数学库
import matplotlib as plt  # 可视化
import os

pwd = os.path.dirname(os.path.abspath(__file__))
book_path = os.path.join(pwd, 'book_utf8.csv')

# pd读取csv数据
df_book = pd.read_csv(book_path)

# 增加列名
df_book.columns = ['star', 'vote', 'shorts']

# 获取前三行
# print(df_book[0:3])

# 获取一列
# print(df_book['star'])

# 显示特定的行列
# print(df_book.loc[1:3,['star', 'vote']])

# 过滤数据
# print(df_book['star'] == '力荐')  # 每一行和'力荐'对比,相同返回True,不同返回False
# print(df_book[df_book['star'] == '力荐'])  # 拿到star为'力荐'这行的所有数据


# 缺失数据
# df_book.dropna()  # 删除有缺失的数据

# 数据聚合
# print(df_book.groupby('star').sum())  # 统计star这一列每个词出现的次数


# 创建新列
# star_to_number = {
#     '力荐': 5,
#     '很差': 4,
#     '推荐': 3,
#     '较差': 2,
#     '还行': 1,
# }

# df_book['new_star'] =df_book['star'].map(star_to_number) # 参照star_to_number的映射关系创建新列

# print(df_book)


# for col in df_book.columns:  # 拿到所有的列名遍历
#     series = df_book[col]  # 拿到这一列对应的数据
#     print(series)

# for idx in df_book.index:
#     print(idx)

