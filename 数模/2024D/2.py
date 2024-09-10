import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义参数
L = 100  # 潜艇长
W = 20   # 潜艇宽
H = 25   # 潜艇高
R = 20   # 深弹杀伤半径
sigma = 120  # 水平定位标准差
sigma_z = 40  # 垂直定位标准差
h0 = 150  # 潜艇中心位置的深度定位值
l = 120  # 潜艇中心位置实际深度的最小值

# 定义命中概率函数
def hit_probability(H, L, W, R, sigma, sigma_z, h0, l):
    # 条件 (1) 的命中概率
    P1_x = norm.cdf(L/2, 0, sigma) - norm.cdf(-L/2, 0, sigma)
    P1_y = norm.cdf(W/2, 0, sigma) - norm.cdf(-W/2, 0, sigma)
    P1_z = norm.cdf(h0 - H/2, h0, sigma_z)
    P1 = P1_x * P1_y * P1_z
    
    # 条件 (2) 的命中概率
    P2_x = norm.cdf(L/2, 0, sigma) - norm.cdf(-L/2, 0, sigma)
    P2_y = norm.cdf(W/2, 0, sigma) - norm.cdf(-W/2, 0, sigma)
    P2_z = norm.cdf(h0 + H/2, h0, sigma_z) - norm.cdf(h0 - H/2, h0, sigma_z)
    P2_r = norm.cdf(R, 0, sigma)
    P2 = P2_x * P2_y * P2_z * P2_r
    
    # 条件 (3) 的命中概率
    P3_x = 1 - (norm.cdf(L/2, 0, sigma) - norm.cdf(-L/2, 0, sigma))
    P3_y = 1 - (norm.cdf(W/2, 0, sigma) - norm.cdf(-W/2, 0, sigma))
    P3_r = norm.cdf(R, 0, sigma)
    P3 = P3_x * P3_y * P3_r
    
    # 总的命中概率
    P = P1 + P2 + P3
    return P

# 计算不同引爆深度下的命中概率
H_values = np.linspace(h0 - H, h0 + H, 1000)
probabilities = [hit_probability(H, L, W, R, sigma, sigma_z, h0, l) for H in H_values]

# 找到最大命中概率及对应的引爆深度
max_probability = max(probabilities)
optimal_H = H_values[np.argmax(probabilities)]

# 绘制结果
plt.plot(H_values, probabilities, label='命中概率')
plt.axvline(optimal_H, color='r', linestyle='--', label=f'最佳引爆深度: {optimal_H:.2f} m')
plt.xlabel('引爆深度 (m)')
plt.ylabel('命中概率')
plt.title('不同引爆深度下的命中概率')
plt.legend()
plt.grid(True)
plt.show()

print(f'最佳引爆深度: {optimal_H:.2f} m')
print(f'最大命中概率: {max_probability:.4f}')

