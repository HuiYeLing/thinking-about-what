import pandas as pd  
import matplotlib.pyplot as plt  
from matplotlib.font_manager import FontProperties
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# 读取CSV文件  
df = pd.read_csv('D:/study/begin/数模/py/obesity_data.csv')

# 设置字体为SimHei显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建一个标签编码器
le = LabelEncoder()

# 将所有的成因和肥胖水平转换为数值类型
df_encoded = df.copy()
for column in df_encoded.columns:
    df_encoded[column] = le.fit_transform(df_encoded[column])

# 计算相关性
correlation = df_encoded.corr()

# 创建一个热力图
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm')






# 在图表上标注相关或不相关
for i in range(correlation.shape[0]):
    for j in range(correlation.shape[1]):
        if correlation.iloc[i, j] > 0.5:
            plt.text(i+0.5, j+0.5, '相关', ha='center', va='center', color='black')
        elif correlation.iloc[i, j] < -0.5:
            plt.text(i+0.5, j+0.5, '不相关', ha='center', va='center', color='black')

plt.show()