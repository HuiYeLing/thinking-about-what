import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 参数定义
L = 100  # 潜艇长度
W = 20   # 潜艇宽度
H = 25   # 潜艇高度
R = 20   # 深弹杀伤半径
sigma = 120  # 水平定位标准差
sigma_z = 40  # 垂直定位标准差
h0 = 150  # 潜艇中心位置的深度定位值
l = 120  # 潜艇中心位置实际深度的最小值

# 定义命中概率函数
def hit_probability(depth):
    # 水平定位在潜艇尺度范围内的概率
    P_x_in = norm.cdf(L/2, 0, sigma) - norm.cdf(-L/2, 0, sigma)
    P_y_in = norm.cdf(W/2, 0, sigma) - norm.cdf(-W/2, 0, sigma)
    
    # 深弹引爆深度在潜艇上表面以下的概率
    P_z_below = norm.cdf(depth, h0, sigma_z)
    
    # 深弹引爆深度在潜艇上表面以上的概率
    P_z_above = 1 - norm.cdf(depth, h0, sigma_z)
    
    # 深弹引爆深度在潜艇上表面与杀伤半径范围内的概率
    P_z_in_kill_radius = norm.cdf(h0 + H/2 + R, h0, sigma_z) - norm.cdf(h0 - H/2, h0, sigma_z)
    
    # 总的命中概率
    P = P_x_in * P_y_in * (P_z_below + P_z_above * P_z_in_kill_radius)
    return P

# 计算不同引爆深度下的命中概率
depths = np.linspace(l - R, h0 + H/2 + R, 1000)
probabilities = [hit_probability(depth) for depth in depths]

# 找到最大命中概率及对应的引爆深度
max_probability = max(probabilities)
optimal_depth = depths[np.argmax(probabilities)]

# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(depths, probabilities, label='命中概率')
plt.axvline(optimal_depth, color='r', linestyle='--', label=f'最佳引爆深度: {optimal_depth:.2f} m')
plt.xlabel('引爆深度 (m)')
plt.ylabel('命中概率')
plt.title('不同引爆深度下的命中概率')
plt.legend()
plt.grid(True)
plt.show()

print(f'最佳引爆深度: {optimal_depth:.2f} m')
print(f'最大命中概率: {max_probability:.4f}')
