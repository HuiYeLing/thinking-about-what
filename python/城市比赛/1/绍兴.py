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

data = pd.read_excel(r'D:\study\begin\python\城市比赛\1\S.xlsx', index_col=0)
print(data.index)
print(data.columns)
print(data)

data = {
    '年份': ['2016', '2017', '2018', '2019', '2020'],
    '生产总值(亿元)': [4697.15, 5027.48, 5382.72, 5780.74, 6000.66],
    '总人口（万人）': [444.53, 446.48, 447.21, 447.87, 447.64],
    '社会消费品零售总额（亿元）': [1740.68, 1930.39, 2139.64, 2352.56, 2322.5],
    '城镇居民人均可支配收入（元）': [50305, 54445, 59049, 63935, 66694],
    '农民居民人均可支配收入（元）': [27744, 30331, 33097, 36120, 38696],
    '货运量（万吨）': [12447, 13426, 14161.21, 15276.53, 17786.89],
    '用电量(单位：亿千瓦时)': [374.51, 411.55, 437.72, 462.37, 453.4]
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
plt.title('绍兴Person相关系数矩阵热图')
plt.show()
