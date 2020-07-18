'''
输出和图形
2. plot 学习文档：
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
3. seaborn 学习文档：
http://seaborn.pydata.org/tutorial.html
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dates = pd.date_range('20200101', periods=12)
df = pd.DataFrame(np.random.randn(12,4), index=dates, columns=list('ABCD'))

# plt.plot(df.index, df['A'], )
# plt.show()


import seaborn as sns
# 绘制散点图
plt.scatter(df.index, df['A'])
plt.show()

# 美化plt
sns.set_style('darkgrid')
plt.scatter(df.index, df['A'])
plt.show()
