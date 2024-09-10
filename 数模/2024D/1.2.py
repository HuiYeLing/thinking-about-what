import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 潜艇参数
submarine_depth = 150   # 潜艇中心位置的深度定位值
sigma = 120             # 水平定位标准差
killing_radius = 20     # 深弹杀伤半径

# 模拟潜艇中心位置的水平坐标（X, Y），服从正态分布
num_simulations = 100000
x_positions = np.random.normal(0, sigma, num_simulations)
y_positions = np.random.normal(0, sigma, num_simulations)

# 计算深弹落点与潜艇中心位置的距离
distances = np.sqrt(x_positions**2 + y_positions**2)

# 定义一个函数来计算命中概率
def calculate_hit_probability(submarine_length, submarine_width, submarine_height, depth_trigger):
    # 条件1：航空深弹落点在目标平面尺度范围内，且引爆深度位于潜艇上表面的下方，由触发引信引爆
    hit_condition_1 = (np.abs(x_positions) <= submarine_length / 2) & (np.abs(y_positions) <= submarine_width / 2) & (depth_trigger >= submarine_depth - submarine_height / 2)

    # 条件2：航空深弹落点在目标平面尺度范围内，且引爆深度位于潜艇上表面的上方，同时潜艇在深弹的杀伤范围内，由定深引信引爆
    hit_condition_2 = (np.abs(x_positions) <= submarine_length / 2) & (np.abs(y_positions) <= submarine_width / 2) & (depth_trigger < submarine_depth - submarine_height / 2) & (depth_trigger >= submarine_depth - submarine_height / 2 - killing_radius)

    # 条件3：航空深弹落点在目标平面尺度范围外，则到达引爆深度时，由定深引信引爆，且此时潜艇在深弹的杀伤范围内
    hit_condition_3 = (distances > submarine_length / 2) & (distances > submarine_width / 2) & (distances <= killing_radius) & (depth_trigger < submarine_depth - submarine_height / 2)

    # 计算命中概率
    hit_probability = np.mean(hit_condition_1 | hit_condition_2 | hit_condition_3)
    return hit_probability

# 不同潜艇尺寸
submarine_sizes = [
    (100, 20, 25),  # 长100m，宽20m，高25m
    (120, 25, 30),  # 长120m，宽25m，高30m
    (150, 30, 35),  # 长150m，宽30m，高35m
]

# 定深引信引爆深度范围
depth_triggers = np.arange(submarine_depth - 50, submarine_depth + 1, 1)

# 存储不同尺寸下的命中概率
all_hit_probabilities = []

for length, width, height in submarine_sizes:
    hit_probabilities = [calculate_hit_probability(length, width, height, depth) for depth in depth_triggers]
    all_hit_probabilities.append(hit_probabilities)

# 绘制不同潜艇尺寸下的命中概率曲线
plt.figure(figsize=(10, 6))
for i, (length, width, height) in enumerate(submarine_sizes):
    plt.plot(depth_triggers, all_hit_probabilities[i], label=f'潜艇尺寸: 长{length}m, 宽{width}m, 高{height}m')
plt.xlabel('定深引信引爆深度 (m)')
plt.ylabel('命中概率')
plt.title('命中概率与定深引信引爆深度的关系（不同潜艇尺寸）')
plt.legend()
plt.grid(True)
plt.show()