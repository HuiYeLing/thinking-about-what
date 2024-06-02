import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv(r"D:\study\begin\数模\py\obesity_data.csv")  # 注意：在Windows中，文件路径中的反斜杠需要被双写或者使用原始字符串（r"路径"）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题
# 选择数值变量列（这里仅作为示例）
numeric_cols = ['肥胖水平', '性别', '年龄','身高','体重','家庭肥胖史','是否频繁食用高热量食物','食用蔬菜的频次','食用主餐的次数','两餐之间的食品消费','是否吸烟','每日耗水量','高热量饮料消耗量','运动频率','TUE','CA酒精消耗量','日常交通方式' ]  # 替换为实际的数值列名

# 确保没有缺失值（如果有缺失值，可以使用dropna()或fillna()等方法处理）
df_numeric = df[numeric_cols].dropna()

# 计算相关性矩阵
corr_matrix = df_numeric.corr()

def corr_to_text(corr):
    if corr > 0.75:
        return '强正相关'
    elif corr > 0.5:
        return '正相关'
    elif corr > 0.25:
        return '弱正相关'
    elif corr < -0.75:
        return '强负相关'
    elif corr < -0.5:
        return '负相关'
    elif corr < -0.25:
        return '弱负相关'
    else:
        return '无相关'

    # 应用这个函数到相关性矩阵的每一个元素，并创建一个新的矩阵用于注解
corr_text = np.vectorize(corr_to_text)(corr_matrix)

# 绘制热力图，不显示数字，而是显示文字描述
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=corr_text, cmap='coolwarm', fmt='', annot_kws={"size": 8})
plt.xlabel('变量', fontsize=12)
plt.ylabel('变量', fontsize=12)
plt.tick_params(labelsize=10)
plt.title('数值变量相关性热力图（文字描述）')
plt.show()
