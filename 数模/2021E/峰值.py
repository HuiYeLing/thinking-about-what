import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import seaborn as sns
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 设置显示中文字体 宋体
mpl.rcParams["axes.unicode_minus"] = False  # 字体更改后，会导致坐标轴中的部分字符无法正常显示，此时需要设置正常显示负号

# 读取数据
data = pd.read_excel('数模/2021E/E/附件1.xlsx')

# 假设数据在某一列中，例如 'No' 列
values = data['No']

# 生成折线图
plt.figure(figsize=(10, 6))
plt.plot(values, label='值')
plt.title('数据折线图')
plt.xlabel('索引')
plt.ylabel('值')
plt.legend()
plt.grid(True)
plt.show()

# 计算最高峰值、最低峰值和均值
max_value = values.max()
min_value = values.min()
mean_value = values.mean()

print(f"最高峰值: {max_value}")
print(f"最低峰值: {min_value}")
print(f"均值: {mean_value}")