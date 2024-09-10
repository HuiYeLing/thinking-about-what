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

data = pd.read_excel(r'D:\study\begin\python\城市比赛\1\郑州.xlsx', index_col=0)
print(data.index)
print(data.columns)
print(data)
data = {

    '生产总值': [930.17180, 1067.01400, 1158.64173, 1185.03478, 1269.10166],  # 万元转换为亿元
    '总人口': [1164.3, 1205.2, 1235.5, 1261.7, 1274.2],
    '社会消费品零售总额': [40.572, 48.639, 53.244, 50.763, 53.892],  # 亿元保持不变，数值调整
    '城镇居民人均可支配收入': [36050, 39042, 42087, 42887, 45246],
    '农民居民人均可支配收入': [19974, 21652, 23536, 24783, 26790],
    '货运量': [25130, 27631, 30426, 25819, 23117],
    '用电量': [543.22, 560.32, 564.6, 554.1, 595.5]
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
plt.title('郑州Person相关系数矩阵热图')
plt.show()

import pandas as pd

# 定义数据字典
data_dict = {
    '年份': ['2017', '2018', '2019', '2020', '2021'],
    '生产总值(亿元)': [930.17180, 1067.01400, 1158.64173, 1185.03478, 1269.10166],  # 万元转换为亿元
    '总人口（万人）': [1164.3, 1205.2, 1235.5, 1261.7, 1274.2],
    '社会消费品零售总额（亿元）': [40.572, 48.639, 53.244, 50.763, 53.892],  # 亿元保持不变，数值调整
    '城镇居民人均可支配收入（元）': [36050, 39042, 42087, 42887, 45246],
    '农民居民人均可支配收入（元）': [19974, 21652, 23536, 24783, 26790],
    '货运量（万吨）': [25130, 27631, 30426, 25819, 23117],
    '用电量(单位：亿千瓦时)': [543.22, 560.32, 564.6, 554.1, 595.5]
}

# 将数据字典转换为 DataFrame
data_df = pd.DataFrame(data_dict)

# 计算每个指标的得分
data_df['生产总值得分'] = data_df['生产总值(亿元)'] / data_df['生产总值(亿元)'].max() * 25
data_df['总人口得分'] = data_df['总人口（万人）'] / data_df['总人口（万人）'].max() * 10
data_df['社会消费品零售总额得分'] = data_df['社会消费品零售总额（亿元）'] / data_df['社会消费品零售总额（亿元）'].max() * 20
data_df['城镇居民人均可支配收入得分'] = data_df['城镇居民人均可支配收入（元）'] / data_df['城镇居民人均可支配收入（元）'].max() * 15
data_df['农民居民人均可支配收入得分'] = data_df['农民居民人均可支配收入（元）'] / data_df['农民居民人均可支配收入（元）'].max() * 15
data_df['货运量得分'] = data_df['货运量（万吨）'] / data_df['货运量（万吨）'].max() * 10
data_df['用电量得分'] = data_df['用电量(单位：亿千瓦时)'] / data_df['用电量(单位：亿千瓦时)'].max() * 5

# 计算总得分
data_df['总得分'] = data_df[['生产总值得分', '总人口得分', '社会消费品零售总额得分', '城镇居民人均可支配收入得分', '农民居民人均可支配收入得分', '货运量得分', '用电量得分']].sum(axis=1)

# 打印结果
print(data_df[['年份', '总得分']])