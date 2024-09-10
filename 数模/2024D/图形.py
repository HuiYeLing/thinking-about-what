import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 定义圆的坐标和半径
circles = {
    1: (0, 0),
    2: (-100, 0),
    3: (100, 0),
    4: (0, -100),
    5: (0, 100),
    6: (0, 50),
    7: (0, -50)
}
radius = 10  # 小圆的半径
big_circle_radius = 120  # 大圆的半径

# 创建图形和坐标轴
fig, ax = plt.subplots()

# 绘制大圆
big_circle = plt.Circle((0, 0), big_circle_radius, color='blue', fill=False, linewidth=2, label='潜艇的活动范围')
ax.add_artist(big_circle)

# 绘制小圆
small_circle_color = 'red'  # 小圆的统一颜色
for i, (x, y) in circles.items():
    small_circle = plt.Circle((x, y), radius, color=small_circle_color, fill=True, label=f'导弹编号{i}')
    ax.add_artist(small_circle)

# 设置坐标轴范围和比例
ax.set_xlim(-150, 150)
ax.set_ylim(-150, 150)
ax.set_aspect('equal', 'box')

# 添加图例
plt.legend()

# 显示图形
plt.title('分批投弹的阵列示意图')
plt.xlabel('X 坐标')
plt.ylabel('Y 坐标')
plt.grid(True)
plt.show()


