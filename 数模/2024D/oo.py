import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats import norm

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 潜艇参数
submarine_length = 10  # 潜艇长度
submarine_width = 5    # 潜艇宽度
submarine_depth = 150  # 潜艇深度

# 深弹参数
kill_radius = 20       # 深弹杀伤半径

# 正态分布参数
sigma = 5  # 水平坐标定位误差标准差

# 定义命中概率函数
def hit_probability(detonation_depth):
    # 判断是否命中
    if 117.5 <= detonation_depth <= 182.5:
        return 1  # 在有效深度范围内，命中概率为1
    return 0

# 生成定深引信引爆深度的数组
detonation_depths = np.linspace(100, 200, 100)
prob = [hit_probability(d) * 100 for d in detonation_depths]  # 转换为百分比

# 绘制定深引信引爆深度与命中概率的关系图
plt.figure(figsize=(10, 5))
plt.plot(detonation_depths, prob, label='定深引信引爆深度与命中概率')
plt.xlabel('定深引信引爆深度 (米)',fontsize=20)
plt.ylabel('命中概率 (%)',fontsize=20)  # 修改标签为百分比
plt.title('定深引信引爆深度与命中概率的关系图')
plt.legend(fontsize=20)
plt.grid(True)
# 增大坐标轴上的数字字号
plt.tick_params(axis='both', which='major', labelsize=15)
plt.show()