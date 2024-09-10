import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from scipy.stats import truncnorm, norm
from shapely.geometry import box, Point
from sklearn.mixture import GaussianMixture
import matplotlib

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义潜艇深度的单边截尾正态分布
h0 = 150  # 潜艇深度均值
sigma_z = 40  # 潜艇深度标准差
l = 120  # 截尾下限
u = 350  # 截尾上限
a, b = (l - h0) / sigma_z, (u - h0) / sigma_z  # 截尾正态分布参数
depth_dist = truncnorm(a, b, loc=h0, scale=sigma_z)

# 计算最佳引爆深度（期望值）
best_depth = depth_dist.mean()
print(f"最佳引爆深度: {best_depth:.2f} 米")

# 定义混合高斯分布来生成潜艇位置
gmm = GaussianMixture(n_components=2, covariance_type='full')
gmm.means_ = np.array([[0, 0], [100, 100]])
sigma_x = 190 / 3  # X方向标准差
sigma_y = 150 / 3  # Y方向标准差
gmm.covariances_ = np.array([[[sigma_x**2, 0], [0, sigma_y**2]], [[sigma_x**2, 0], [0, sigma_y**2]]])
gmm.weights_ = np.array([0.5, 0.5])
gmm.precisions_cholesky_ = np.linalg.cholesky(np.linalg.inv(gmm.covariances_))

# 设计投弹方案
def design_bombing_plan(interval):
    """设计投弹方案"""
    x_range = np.linspace(-interval, interval, 3)  # 覆盖潜艇可能存在的X坐标范围
    y_range = np.linspace(-interval, interval, 3)  # 覆盖潜艇可能存在的Y坐标范围
    x, y = np.meshgrid(x_range, y_range)
    intervals = np.column_stack((x.flatten(), y.flatten()))
    return intervals

# 定义函数来检查潜艇和爆炸范围是否重叠
def calculate_overlap_area(sub_x, sub_y, sub_length, sub_width, bomb_x, bomb_y, bomb_radius):
    sub_rect = box(sub_x - sub_length / 2, sub_y - sub_width / 2, sub_x + sub_length / 2, sub_y + sub_width / 2)
    bomb_circle = Point(bomb_x, bomb_y).buffer(bomb_radius)
    overlap_area = sub_rect.intersection(bomb_circle).area
    return overlap_area

# 计算命中概率
def calculate_hit_probability(h):
    L, W, H, R, sigma = 100, 20, 20, 20, 40  # 假设这些参数已定义
    P1_x = calculate_norm_cdf_range(0, L, sigma)
    P1_y = calculate_norm_cdf_range(0, W, sigma)
    P1_z = depth_dist.cdf(h + H / 2)
    P1 = P1_x * P1_y * P1_z

    P2_x = calculate_norm_cdf_range(0, L, sigma)
    P2_y = calculate_norm_cdf_range(0, W, sigma)
    P2_z = depth_dist.cdf(h + H / 2) - depth_dist.cdf(h - H / 2)
    P2_r = norm.cdf(R, 0, sigma)
    P2 = P2_x * P2_y * P2_z * P2_r

    P3_x = 1 - P1_x
    P3_y = 1 - P1_y
    P3_r = norm.cdf(R, 0, sigma)
    P3 = P3_x * P3_y * P3_r

    return P1 + P2 + P3

def calculate_norm_cdf_range(a, b, sigma):
    """计算正态分布在区间[a, b]上的累积分布函数值"""
    return norm.cdf(b, 0, sigma) - norm.cdf(a, 0, sigma)

# 使用蒙特卡洛模拟来估计多枚深弹的命中概率
def monte_carlo_simulation(interval, num_simulations=10000, increase_factor=1.1):
    hits = 0
    sub_length = 100  # 潜艇长度
    sub_width = 20  # 潜艇宽度
    bomb_radius = 20  # 爆炸半径
    intervals = design_bombing_plan(interval)
    
    for _ in range(num_simulations):
        sub_x, sub_y = gmm.sample()[0][0]
        sub_depth = depth_dist.rvs()
        
        actual_hits = []
        for (x, y) in intervals:
            hit_probability = calculate_hit_probability(sub_depth)
            
            if actual_hits and not any(actual_hits):
                hit_probability *= increase_factor
            
            actual_hits.append(hit_probability)
        
        if any(actual_hits):
            hits += 1
    
    return hits / num_simulations

# 生成不同间隔下的命中概率
intervals = np.linspace(50, 300, 10)
hit_probabilities = [monte_carlo_simulation(interval) for interval in intervals]

# 找到命中率最高的间隔
optimal_interval = intervals[np.argmax(hit_probabilities)]
print(f"最佳导弹间隔: {optimal_interval:.2f} 米")
print(f"最高命中概率: {max(hit_probabilities):.4f}")

# 绘制间隔与命中概率的关系图
plt.figure()
plt.plot(intervals, hit_probabilities, marker='o')
plt.xlabel('导弹间隔 (米)')
plt.ylabel('命中概率')
plt.title('导弹间隔与命中概率的关系')
plt.grid(True)
plt.show()

# 使用最佳导弹间隔设计投弹方案并绘制导弹阵列图
def plot_optimal_bombing_plan(optimal_interval):
    sub_length = 100  # 潜艇长度
    sub_width = 20  # 潜艇宽度
    bomb_radius = 20  # 爆炸半径
    intervals = design_bombing_plan(optimal_interval)
    
    fig, ax = plt.subplots()
    ax.set_xlim(-optimal_interval - 50, optimal_interval + 50)
    ax.set_ylim(-optimal_interval - 50, optimal_interval + 50)
    ax.set_xlabel('X 坐标')
    ax.set_ylabel('Y 坐标')
    
    for idx, (x, y) in enumerate(intervals):
        circle = Circle((x, y), bomb_radius, color='r', alpha=0.3)
        ax.add_patch(circle)
        ax.text(x, y, str(idx + 1), color='black', ha='center', va='center')
    
    sub_x, sub_y = gmm.sample()[0][0]
    submarine = Rectangle((sub_x - sub_length / 2, sub_y - sub_width / 2), sub_length, sub_width, color='b', alpha=0.5)
    ax.add_patch(submarine)
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f'最佳导弹间隔: {optimal_interval:.2f} 米')
    plt.show()

plot_optimal_bombing_plan(optimal_interval)