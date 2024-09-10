import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import matplotlib
import random

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 输入参数
K = 7  # 允许的最大传输时间（分钟）
P_success = 0.9  # 成功接收副站气象报文的概率阈值
M = 2  # 每个主站下属的副站数量
T_max = 1  # 单个副站发送报文所需的最大时间（分钟）

# 计算单次传输成功的概率
P_single = P_success ** (1 / M)

# 计算N的最大值
N_max = math.floor(K / (M * T_max))

# 输出N的最大值
print(f"在K = {K}时，N的最大值为: {N_max}")

# 根据一般传输模型给出副站气象报文的传输方案
def generate_transmission_plan(N):
    plan = []
    for i in range(1, N + 1):
        plan.append((i, (i % N) + 1, f"{i}(1)"))
        plan.append((i, (i % N) + 1, f"{i}(2)"))
    return plan

# 生成传输方案
transmission_plan = generate_transmission_plan(N_max)

# 输出传输方案
print(f"表2 副站气象报文的传输方案 (N = {N_max})")
print("传输轮数序号\t发送站点序号\t接收站点序号\t发送信息所属站点序号 (含信息完整性)")
for idx, (send, receive, info) in enumerate(transmission_plan, start=1):
    print(f"{idx}\t{send}\t{receive}\t{info}")

# 保存传输方案为CSV文件
df = pd.DataFrame(transmission_plan, columns=["发送站点序号", "接收站点序号", "发送信息所属站点序号 (含信息完整性)"])
df.index += 1  # 传输轮数序号从1开始
df.index.name = "传输轮数序号"
df.to_csv("transmission_plan.csv", encoding='utf-8-sig')

# 计算平均成功接收情况
def calculate_success_probabilities(success_rate, num_stations):
    prob_at_least_one = 1 - (1 - success_rate) ** num_stations
    avg_successful_receptions = num_stations * success_rate
    return prob_at_least_one, avg_successful_receptions

# 假设副站发送和接收消息的成功率为80%
success_rate = 0.8
num_stations = 2

# 计算成功接收概率
prob_at_least_one, avg_successful_receptions = calculate_success_probabilities(success_rate, num_stations)

# 输出成功接收概率
print(f"平均有 {prob_at_least_one * 100:.2f}% 的主站能成功接收每支分队至少一个副站的气象报文")
print(f"任一主站平均能成功接收 {avg_successful_receptions:.2f} 个副站的气象报文")

# 模拟选择性重传
def simulate_selective_repeat(N, M, K, P_success):
    message_queues = {i: [] for i in range(1, N+M+1)}
    send_times = {i: 0 for i in range(1, N+M+1)}
    transmission_log = []
    failed_transmissions = []

    def adjust_polling_interval():
        # 动态调整轮询周期的逻辑
        return max(1, int(K / (N + M)))

    for t in range(K):
        polling_interval = adjust_polling_interval()
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
                send_times[i] = t + polling_interval

    # 确保所有消息都被成功接收
    while failed_transmissions:
        new_failed_transmissions = []
        for i, j, orig_t in failed_transmissions:
            if random.random() < P_success:
                message_queues[j].append(f"Message from {i} at time {orig_t}")
                for log in transmission_log:
                    if log[1] == i and log[2] == j and log[4] == "Transmission failed":
                        log[4] = message_queues[j]
            else:
                new_failed_transmissions.append((i, j, orig_t))
        failed_transmissions = new_failed_transmissions

    for i in range(1, N+1):
        received_messages = len(message_queues[i])
        expected_messages = (N-1) * K
        print(f"主站 {i} 接收到 {received_messages} 条消息，预期接收到 {expected_messages} 条消息")
        if received_messages == expected_messages:
            print(f"主站 {i} 成功接收到所有消息")
        else:
            print(f"主站 {i} 未能接收到所有消息")

    return transmission_log

# 示例参数
N = N_max  # 主站数量

# 模拟选择性重传
transmission_log = simulate_selective_repeat(N, M, K, P_success)

# 将传输日志转换为 DataFrame 并显示
df_log = pd.DataFrame(transmission_log, columns=['传输轮数', '发送站点序号', '接收站点序号', '发送信息所属站点序号', '接收站点消息队列'])
print(df_log)

# 保存结果为表格
df_log.to_csv('selective_repeat_log.csv', index=False, encoding='utf-8-sig')