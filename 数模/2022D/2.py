import math
import matplotlib.pyplot as plt
import matplotlib

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def calculate_n_max(K, P_success, M, T_max):
    # 计算单次传输成功的概率
    P_single = P_success
    
    # 计算至少一次成功的概率
    P_at_least_one_success = 1 - (1 - P_single)**M
    
    # 确保至少一次成功的概率满足阈值
    if P_at_least_one_success < 0.9:
        raise ValueError("单次传输成功的概率不足以满足至少一次成功的概率阈值")
    
    # 计算 N 的最大值
    N_max = math.floor(K / (M * T_max))
    
    return N_max

def plot_n_vs_k(max_k, P_success, M, T_max):
    K_values = list(range(5, max_k + 1))
    N_values = [calculate_n_max(K, P_success, M, T_max) for K in K_values]
    
    plt.plot(K_values, N_values, marker='o')
    plt.xlabel('允许的最大传输时间 K（分钟）')
    plt.ylabel('主站的最大数量 N')
    plt.title('主站的最大数量 N 与 允许的最大传输时间 K 的关系')
    plt.grid(True)
    plt.show()

# 示例参数
P_success = 0.9  # 成功接收副站气象报文的概率阈值
M = 2  # 每个主站下属的副站数量
T_max = 1  # 单个副站发送报文所需的最大时间（分钟）

# 绘制 N 与 K 的关系图
plot_n_vs_k(20, P_success, M, T_max)