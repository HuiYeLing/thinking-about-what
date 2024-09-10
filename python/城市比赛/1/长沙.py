# 修正列名错误和计算得分的代码

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

# 设置显示中文字体 宋体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# 读取数据
data = pd.read_excel(r'D:\study\begin\python\城市比赛\1\长沙.xlsx', index_col=0)
print(data.index)
print(data.columns)
print(data)

# 定义数据字典
data_dict = {
    '总人口': [613.87, 639.3, 704.07, 828.27, 1006.08],
    '生产总值': [720.85, 1589.41, 4440.32, 8502.6, 12142.52],
    '社会消费品零售总额': [332.16, 691.24, 1622.09, 3150.24, 4469.76],
    '货物运输量': [5910, 10991, 22947, 33932, 38838],
    '城镇居民人均可支配收入': [7529.76, 12433.9, 22813.9, 39961.1, 57971],
    '农村居民人均可支配收入': [2941, 4735, 10639.8, 23601, 34754],
    '用电量': [221763, 923856, 1603152, 2464961, 4116782]
}

# 将数据字典转换为 DataFrame
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

# 绘制Pearson相关系数矩阵的热图
plt.figure(figsize=(10, 8))
sns.heatmap(pearson_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('长沙Person相关系数矩阵热图')
plt.show()

# 计算每个指标的得分
df['生产总值得分'] = df['生产总值（亿元）'] / df['生产总值（亿元）'].max() * 25
df['总人口得分'] = df['总人口（万人）'] / df['总人口（万人）'].max() * 10
df['社会消费品零售总额得分'] = df['社会消费品零售总额（亿元）'] / df['社会消费品零售总额（亿元）'].max() * 20
df['城镇居民人均可支配收入得分'] = df['城镇居民人均可支配收入（元）'] / df['城镇居民人均可支配收入（元）'].max() * 15
df['农村居民人均可支配收入得分'] = df['农村居民人均可支配收入（元）'] / df['农村居民人均可支配收入（元）'].max() * 15
df['货物运输量得分'] = df['货物运输量（万吨）'] / df['货物运输量（万吨）'].max() * 10
df['用电量得分'] = df['用电量（万度）'] / df['用电量（万度）'].max() * 5

df['总得分'] = df[['生产总值得分', '总人口得分', '社会消费品零售总额得分', '城镇居民人均可支配收入得分', '农村居民人均可支配收入得分', '货物运输量得分', '用电量得分']].sum(axis=1)

# 打印结果
print(df[['年份', '总得分']])