import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"] # 设置显示中文字体 宋体
mpl.rcParams["axes.unicode_minus"] = False #字体更改后，会导致坐标轴中的部分字符无法正常显示，此时需要设置正常显示负号

data = pd.read_excel(r'D:\study\begin\python\城市比赛\1\青岛.xlsx', index_col=0)
print(data.index)
print(data.columns)
print(data)
data = {
    '生产总值': [5350.69, 8658.57, 10949.38, 11741.31, 12400.56],
    '总人口': [871.51, 944.6, 981.4, 992.3, 1010.57],
    '社会消费品零售总额': [1892.38, 3548.16, 4742.72, 5126.6, 5203.5],
    '城市居民人均年可支配收入': [24380, 40370, 50817, 54484, 55905],
    '农民人均年可支配收入': [9326, 16730, 20820, 22573, 23656],
    '货运量': [35012, 49749, 54250, 57736, 60459],
    '用电量': [292.97, 342.3, 432, 458, 476.6]
}


# 创建DataFrame
df = pd.DataFrame(data)

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
plt.title('青岛Person相关系数矩阵热图')
plt.show()


import pandas as pd

# 定义数据字典
data_dict = {
    '年份': ['2010', '2015', '2018', '2019', '2020'],
    '生产总值(亿元)': [5350.69, 8658.57, 10949.38, 11741.31, 12400.56],
    '总人口（万人）': [871.51, 944.6, 981.4, 992.3, 1010.57],
    '社会消费品零售总额（亿元）': [1892.38, 3548.16, 4742.72, 5126.6, 5203.5],
    '城市居民人均年可支配收入（元）': [24380, 40370, 50817, 54484, 55905],
    '农民人均年可支配收入（元）': [9326, 16730, 20820, 22573, 23656],
    '货运量（万吨）': [35012, 49749, 54250, 57736, 60459],
    '用电量（亿千瓦时）': [292.97, 342.3, 432, 458, 476.6]
}

# 将数据字典转换为 DataFrame
data_df = pd.DataFrame(data_dict)

# 计算每个指标的得分
# 计算每个指标的得分
data_df['生产总值得分'] = data_df['生产总值(亿元)'] / data_df['生产总值(亿元)'].max() * 25
data_df['总人口得分'] = data_df['总人口（万人）'] / data_df['总人口（万人）'].max() * 10
# 以下列名也需要根据实际定义进行修正
data_df['社会消费品零售总额得分'] = data_df['社会消费品零售总额（亿元）'] / data_df['社会消费品零售总额（亿元）'].max() * 20
data_df['城市居民人均年可支配收入得分'] = data_df['城市居民人均年可支配收入（元）'] / data_df['城市居民人均年可支配收入（元）'].max() * 15
data_df['农民人均年可支配收入得分'] = data_df['农民人均年可支配收入（元）'] / data_df['农民人均年可支配收入（元）'].max() * 15
data_df['货运量得分'] = data_df['货运量（万吨）'] / data_df['货运量（万吨）'].max() * 10
data_df['用电量得分'] = data_df['用电量（亿千瓦时）'] / data_df['用电量（亿千瓦时）'].max() * 5

data_df['总得分'] = data_df[['生产总值得分', '总人口得分', '社会消费品零售总额得分', '城市居民人均年可支配收入得分', '农民人均年可支配收入得分', '货运量得分', '用电量得分']].sum(axis=1)
# 打印结果
print(data_df[['年份', '总得分']])
