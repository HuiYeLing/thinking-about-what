import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 读取数据
df = pd.read_csv(r"D:\study\begin\数模\py\obesity_data.csv") # 注意：在Windows中，文件路径中的反斜杠需要被双写或者使用原始字符串（r"路径"）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 选择数值变量列（这里仅作为示例，并且假设性别已经被编码为数值或者排除在外）
numeric_cols = ['肥胖水平', '年龄', '身高', '体重', '家庭肥胖史', '是否频繁食用高热量食物',
                '食用蔬菜的频次', '食用主餐的次数', '两餐之间的食品消费', '是否吸烟', '每日耗水量',
                '高热量饮料消耗量', '运动频率', 'TUE', 'CA酒精消耗量', '日常交通方式']  # 替换为实际的数值列名

# 假设所有列都已经是数值型的（如果不是，则需要进行适当的转换或编码）
X = df[numeric_cols]

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 执行PCA
pca = PCA(n_components=2)  # 选择降维到2个主成分，仅用于可视化
X_pca = pca.fit_transform(X_scaled)

# 可视化前两个主成分
plt.figure(figsize=(10, 8))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1])
plt.xlabel('第一主成分')
plt.ylabel('第二主成分')
plt.title('PCA降维后的数据可视化')
plt.show()

# 如果你还想获取PCA组件的详细信息（如解释方差的比例），可以这样做：
explained_variance_ratio = pca.explained_variance_ratio_
print("每个主成分解释的方差比例:", explained_variance_ratio)