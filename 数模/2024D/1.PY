import numpy as np

# 潜艇参数
submarine_length = 100  # 潜艇长度
submarine_width = 20    # 潜艇宽度
submarine_height = 25   # 潜艇高度
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
def calculate_hit_probability(depth_trigger):
    # 条件1：航空深弹落点在目标平面尺度范围内，且引爆深度位于潜艇上表面的下方，由触发引信引爆
    hit_condition_1 = (np.abs(x_positions) <= submarine_length / 2) & (np.abs(y_positions) <= submarine_width / 2) & (depth_trigger >= submarine_depth - submarine_height / 2)

    # 条件2：航空深弹落点在目标平面尺度范围内，且引爆深度位于潜艇上表面的上方，同时潜艇在深弹的杀伤范围内，由定深引信引爆
    hit_condition_2 = (np.abs(x_positions) <= submarine_length / 2) & (np.abs(y_positions) <= submarine_width / 2) & (depth_trigger < submarine_depth - submarine_height / 2) & (depth_trigger >= submarine_depth - submarine_height / 2 - killing_radius)

    # 条件3：航空深弹落点在目标平面尺度范围外，则到达引爆深度时，由定深引信引爆，且此时潜艇在深弹的杀伤范围内
    hit_condition_3 = (distances > submarine_length / 2) & (distances > submarine_width / 2) & (distances <= killing_radius) & (depth_trigger < submarine_depth - submarine_height / 2)

    # 计算命中概率
    hit_probability = np.mean(hit_condition_1 | hit_condition_2 | hit_condition_3)
    return hit_probability

# 对不同的定深引信引爆深度进行模拟
depth_triggers = np.arange(submarine_depth - submarine_height / 2 - killing_radius, submarine_depth + 1, 1)
hit_probabilities = [calculate_hit_probability(depth) for depth in depth_triggers]

# 找到使命中概率最大的定深引信引爆深度
max_hit_probability = max(hit_probabilities)
optimal_depth_trigger = depth_triggers[np.argmax(hit_probabilities)]

print(f"使投弹命中概率最大的定深引信引爆深度: {optimal_depth_trigger}")
print(f"最大投弹命中概率: {max_hit_probability:.4f}")