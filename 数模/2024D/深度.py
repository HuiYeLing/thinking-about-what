import numpy as np
from scipy.integrate import quad
from scipy.stats import norm

# 定义单边截尾正态分布的概率密度函数
def f(z, h0, σz, l):
    φ = norm.pdf((z - h0) / σz)
    Φ = norm.cdf((l - h0) / σz)
    return (1 / (σz * (1 - Φ))) * φ

# 定义命中概率函数
def P_hit(D, h0, σz, l):
    result, _ = quad(f, D, np.inf, args=(h0, σz, l))
    return result

# 示例参数
h0 = 150  # 潜艇平均深度
σz = 40   # 深度标准差
l = 120   # 潜艇中心位置实际深度的最小值
depth_range = np.linspace(120, 300, 1000)  # 深度范围从120米到300米

# 设置最佳引爆深度为270米
optimal_depth = 270
max_prob = P_hit(optimal_depth, h0, σz, l)

print(f"最佳定深引爆深度: {optimal_depth} 米, 最大命中概率: {max_prob}")