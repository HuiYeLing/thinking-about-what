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

data = pd.read_excel(r'D:\study\begin\python\城市比赛\1\副本宁波.xlsx', index_col=0)
print(data.index)
print(data.columns)
print(data)


import pandas as pd

# 定义数据字典
data_dict = {
    '生产总值': [5264.7, 8295.35, 11193.14, 12035.11, 12408.66],
    '全社会用电量': [12577, 16029, 21240, 22135, 22736],
    '社会消费品零售总额': [44320, 83567, 108613, 116947, 115800],
    '货运量': [83.71, 115.30, 168.37, 187.42, 196.44],
    '总人口': [574.08, 586.57, 602.96, 608.47, 613.66],
    '城缜居民人均可支配收入': [30166, 47852, 60134, 64886, 68008],
    '农村居民人均可支配收入': [14261, 26469, 33633, 36632, 39132]
}

# 将数据字典转换为 DataFrame
data_df = pd.DataFrame(data_dict)

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
plt.title('宁波Pearson相关系数矩阵热图')
plt.show()