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

data = pd.read_excel(r'D:\study\begin\python\城市比赛\1\6城GDP对比.xlsx', index_col=0)

print(data.shape)
print(data.index)
print(data.columns)
print(data)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 假设 data 是已经加载好的 DataFrame
data = {
    "年份": ["2010", "2015", "2018", "2019", "2020"],
    "生产总值（宁波）": [5264.70, 8295.35, 11193.14, 12035.11, 12408.66],
    "生产总值(青岛)": [5350.69, 8658.57, 10949.38, 11741.31, 12400.56],
    "生产总值(无锡)": [5758.00, 8681.37, 11202.98, 11803.32, 12370.48],
    "生产总值（长沙）": [4440.32, 8502.60, 11003.41, 11574.22, 12142.52],
    "生产总值(郑州)": [5758.00, 8515.00, 10670.14, 11586.42, 11850.35],
    "生产总值(绍兴)": [2811.75, 4424.69, 5382.72, 5785.51, 5963.76]
}
df = pd.DataFrame(data)

# 将 DataFrame 从宽格式转换为长格式
df_long = pd.melt(df, id_vars=["年份"], var_name="城市", value_name="生产总值")

# 绘制折线图
plt.figure(figsize=(10, 6))
lineplot = sns.lineplot(data=df_long, x="年份", y="生产总值", hue="城市", marker="o")

plt.title("城市生产总值对比")
plt.xlabel("年份")
plt.ylabel("生产总值")
plt.xticks(rotation=45)
plt.legend(title="城市")

# 显示数值
for i, point in df_long.iterrows():
    lineplot.text(point['年份'], point['生产总值'], f"{point['生产总值']:.2f}", 
                  horizontalalignment='left', size='small', color='black', weight='semibold')

plt.tight_layout()
plt.show()