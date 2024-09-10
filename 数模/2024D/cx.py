import numpy as np
from scipy.stats import norm

# 定义参数
L = 100  # 潜艇长度
W = 20   # 潜艇宽度
H = 25   # 潜艇高度
depth = 150  # 潜艇深度
sigma = 120  # 标准差
R = 20  # 杀伤半径

# 定义辅助函数
def calculate_norm_cdf_range(a, b, sigma):
    return norm.cdf(b, scale=sigma) - norm.cdf(a, scale=sigma)

# 定义深度分布
depth_dist = norm(loc=depth, scale=sigma)

# 重写计算命中概率的函数
def calculate_hit_probability(h):
    # 计算条件 (1) 的命中概率
    P1_x = calculate_norm_cdf_range(0, L, sigma)
    P1_y = calculate_norm_cdf_range(0, W, sigma)
    P1_z = depth_dist.cdf(h + H / 2)
    P1 = P1_x * P1_y * P1_z

    # 计算条件 (2) 的命中概率
    P2_x = calculate_norm_cdf_range(0, L, sigma)
    P2_y = calculate_norm_cdf_range(0, W, sigma)
    P2_z = depth_dist.cdf(h + H / 2) - depth_dist.cdf(h - H / 2)
    P2_r = norm.cdf(R, scale=sigma)
    P2 = P2_x * P2_y * P2_z * P2_r

    # 计算条件 (3) 的命中概率
    P3_x = 1 - P1_x
    P3_y = 1 - P1_y
    P3_r = norm.cdf(R, scale=sigma)
    P3 = P3_x * P3_y * P3_r

    # 输出每个条件的命中概率
    print(f"条件 (1) 的命中概率: {P1}")
    print(f"条件 (2) 的命中概率: {P2}")
    print(f"条件 (3) 的命中概率: {P3}")

    return P1 + P2 + P3

# 示例调用
h = 100  # 示例深度
total_probability = calculate_hit_probability(h)
print(f"总命中概率: {total_probability}")