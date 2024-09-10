import math
import matplotlib.pyplot as plt
import matplotlib
import random
import pandas as pd

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def calculate_n_max(K, P_success, M, T_max):
    P_single = P_success
    P_at_least_one_success = 1 - (1 - P_single)**M
    if P_at_least_one_success < 0.9:
        raise ValueError("单次传输成功的概率不足以满足至少一次成功的概率阈值")
    N_max = math.floor(K / (M * T_max))
    return N_max

def simulate_selective_repeat(N, M, K, P_success):
    message_queues = {i: [] for i in range(1, N+M+1)}
    send_times = {i: 0 for i in range(1, N+M+1)}
    transmission_log = []
    failed_transmissions = []

    for t in range(K):
        for i in range(1, N+1):
            if send_times[i] <= t:
                for j in range(1, N+M+1):
                    if i != j:
                        if random.random() < P_success:
                            message_queues[j].append(f"Message from {i} at time {t}")
                            transmission_log.append([t+1, i, j, i, message_queues[j]])
                        else:
                            transmission_log.append([t+1, i, j, i, "Transmission failed"])
                            failed_transmissions.append((i, j, t))
                send_times[i] = t + 1

    for t in range(K, 2*K):
        for i, j, orig_t in failed_transmissions:
            if random.random() < P_success:
                message_queues[j].append(f"Message from {i} at time {t}")
                for log in transmission_log:
                    if log[1] == i and log[2] == j and log[4] == "Transmission failed":
                        log[4] = message_queues[j]

    for i in range(1, N+1):
        received_messages = len(message_queues[i])
        expected_messages = (N-1) * K
        print(f"主站 {i} 接收到 {received_messages} 条消息，预期接收到 {expected_messages} 条消息")
        if received_messages == expected_messages:
            print(f"主站 {i} 成功接收到所有消息")
        else:
            print(f"主站 {i} 未能接收到所有消息")

    return transmission_log

def plot_n_vs_k(max_k, P_success, M, T_max):
    K_values = list(range(5, max_k + 1))
    N_values = [calculate_n_max(K, P_success, M, T_max) for K in K_values]
    
    plt.plot(K_values, N_values, marker='o')
    plt.xlabel('允许的最大传输时间 K（分钟）')
    plt.ylabel('主站的最大数量 N')
    plt.title('主站的最大数量 N 与 允许的最大传输时间 K 的关系')
    plt.grid(True)
    plt.show()

def calculate_n_max_for_k_range(min_k, max_k, P_success, M, T_max):
    results = []
    for K in range(min_k, max_k + 1):
        try:
            N_max = calculate_n_max(K, P_success, M, T_max)
            results.append((K, N_max))
        except ValueError as e:
            print(f"K={K} 时出错: {e}")
    return results

# 示例参数
P_success = 0.9  # 成功接收副站气象报文的概率阈值
M = 2  # 每个主站下属的副站数量
T_max = 1  # 单个副站发送报文所需的最大时间（分钟）

# 绘制 N 与 K 的关系图
plot_n_vs_k(20, P_success, M, T_max)

# 模拟选择性重传
N = 9  # 主站数量
K = 10  # 允许的最大传输时间
transmission_log = simulate_selective_repeat(N, M, K, P_success)

# 将传输日志转换为 DataFrame 并显示
df = pd.DataFrame(transmission_log, columns=['传输轮数', '发送站点序号', '接收站点序号', '发送信息所属站点序号', '接收站点消息队列'])
print(df)

# 保存结果为表格
df.to_csv('selective_repeat_log.csv', index=False, encoding='utf-8-sig')

# 计算并输出 K 大于等于 5 时的 N 的最大值
results = calculate_n_max_for_k_range(5, 20, P_success, M, T_max)
print("K 大于等于 5 时的 N 的最大值:")
for K, N_max in results:
    print(f"K={K}, N_max={N_max}")