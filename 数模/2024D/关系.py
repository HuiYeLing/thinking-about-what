import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 定义 X 和 Y 的范围
x = np.linspace(-190, 190, 100)
y = np.linspace(-150, 150, 100)
x, y = np.meshgrid(x, y)

# 假设一个简单的概率分布函数
# 这里使用一个高斯分布作为示例
sigma_x = 190 / 3
sigma_y = 150 / 3
z = np.exp(-((x**2 / (2 * sigma_x**2)) + (y**2 / (2 * sigma_y**2))))
# 归一化到总命中概率
total_prob = 0.6993
z = z * total_prob / np.max(z)

# 将命中概率转换为百分比
z = z * 100

# 创建三维图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制表面
surf = ax.plot_surface(x, y, z, cmap='viridis')

# 添加颜色条
cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
cbar.set_label('命中概率 (%)')

# 添加标题和标签
ax.set_title('平面范围内的命中概率分布')
ax.set_xlabel('X 坐标 (米)', fontsize=20)
ax.set_ylabel('Y 坐标 (米)', fontsize=20)
ax.set_zlabel('命中概率 (%)', fontsize=20)

# 显示图形
plt.show()