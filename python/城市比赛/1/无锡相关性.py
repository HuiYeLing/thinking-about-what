import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"] # 设置显示中文字体 宋体
mpl.rcParams["axes.unicode_minus"] = False #字体更改后，会导致坐标轴中的部分字符无法正常显示，此时需要设置正常显示负号

data = pd.read_excel(r'D:\study\begin\python\城市比赛\1\无锡.xlsx', index_col=0)

print(data.index)

print(data.columns)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 将数据转换为pandas DataFrame
# 修改后的数据字典，调整了单位和列名以匹配计算得分的部分
data_dict = {
    '年份': [2015, 2016, 2017, 2018, 2019, 2020],
    '生产总值（亿元）': [8681.37, 9340.16, 10313.07, 11202.98, 11803.32, 12370.48],
    '总人口（万人）': [480.9007, 486.2, 493.05, 497.21, 502.83, 508.97],
    '货运量（万吨）': [15353, 15830, 17385, 18640, 20601, 21691],
    '社会消费品零售总额（万元）': [2186.34, 2357.62, 2585.69, 2785.21, 3024.34, 2994.36],
    '农村居民人均可支配收入（元）': [24155, 26158, 28358, 30787, 33574, 35750],
    '城缜居民人均可支配收入（元）': [45129, 48628, 52659, 56989, 61915, 64714],
    '全社会用电量（万千瓦时）': [598.18, 600.5, 638.67, 686.67, 732.81, 750.82]
}
import pandas as pd


# 创建DataFrame
df = pd.DataFrame(data_dict)

# 计算Pearson相关系数矩阵
pearson_corr = df.corr()

# 计算Spearman等级相关系数矩阵
spearman_corr = df.corr(method='spearman')

# 打印相关系数矩阵
print("Pearson相关系数矩阵:")
print(pearson_corr)
print("\nSpearman等级相关系数矩阵:")
print(spearman_corr)

import seaborn as sns
import matplotlib.pyplot as plt

# 绘制Pearson相关系数矩阵的热图
plt.figure(figsize=(10, 8))
sns.heatmap(pearson_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Pearson相关系数矩阵热图')
plt.show()

import pandas as pd

# 定义数据字典
# 修改后的数据字典，调整了单位和列名以匹配计算得分的部分
data_dict = {
    '年份': [2015, 2016, 2017, 2018, 2019, 2020],
    '生产总值（亿元）': [8681.37, 9340.16, 10313.07, 11202.98, 11803.32, 12370.48],
    '总人口（万人）': [480.9007, 486.2, 493.05, 497.21, 502.83, 508.97],
    '货运量（万吨）': [15353, 15830, 17385, 18640, 20601, 21691],
    '社会消费品零售总额（万元）': [2186.34, 2357.62, 2585.69, 2785.21, 3024.34, 2994.36],
    '农村居民人均可支配收入（元）': [24155, 26158, 28358, 30787, 33574, 35750],
    '城缜居民人均可支配收入（元）': [45129, 48628, 52659, 56989, 61915, 64714],
    '全社会用电量（万千瓦时）': [598.18, 600.5, 638.67, 686.67, 732.81, 750.82]
}


# 将数据字典转换为 DataFrame
data_df = pd.DataFrame(data_dict)

# 计算每个指标的得分
data_df['生产总值得分'] = data_df['生产总值（亿元）'] / data_df['生产总值（亿元）'].max() * 25
data_df['总人口得分'] = data_df['总人口（万人）'] / data_df['总人口（万人）'].max() * 10
data_df['社会消费品零售总额得分'] = data_df['社会消费品零售总额（万元）'] / data_df['社会消费品零售总额（万元）'].max() * 20
data_df['城缜居民人均可支配收入得分'] = data_df['城缜居民人均可支配收入（元）'] / data_df['城缜居民人均可支配收入（元）'].max() * 15
data_df['农村居民人均可支配收入得分'] = data_df['农村居民人均可支配收入（元）'] / data_df['农村居民人均可支配收入（元）'].max() * 15
data_df['货运量得分'] = data_df['货运量（万吨）'] / data_df['货运量（万吨）'].max() * 10
data_df['用电量得分'] = data_df['全社会用电量（万千瓦时）'] / data_df['全社会用电量（万千瓦时）'].max() * 5

# 计算总得分
data_df['总得分'] = data_df[['生产总值得分', '总人口得分', '社会消费品零售总额得分', '城缜居民人均可支配收入得分', '农村居民人均可支配收入得分', '货运量得分', '用电量得分']].sum(axis=1)

# 打印结果
print(data_df[['年份', '总得分']])