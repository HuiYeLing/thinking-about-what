import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import matplotlib

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 输入参数
K = 8  # 允许的最大传输时间（分钟）
P_success = 0.97 # 成功接收副站气象报文的概率阈值
M = 2  # 每个主站下属的副站数量
T_max = 1  # 单个副站发送报文所需的最大时间（分钟）

# 计算单次传输成功的概率
P_single = P_success ** (1 / M)

# 计算N的最大值
N_max = math.floor(K / (M * T_max))

# 输出N的最大值
print(f"在K = {K}时，N的最大值为: {N_max}")

# 站点编号转换为字母
def station_number_to_letter(number):
    return chr(64 + number)  # 64 + 1 = 65 -> 'A'

# 根据一般传输模型给出主站间气象报文信息共享的传输方案
def generate_main_station_plan(N):
    plan = []
    for i in range(1, N + 1):
        plan.append((station_number_to_letter(i), station_number_to_letter((i % N) + 1), f"{station_number_to_letter(i)}"))
    return plan

# 生成主站间气象报文信息共享的传输方案
main_station_plan = generate_main_station_plan(N_max)

# 输出主站间气象报文信息共享的传输方案
print(f"表1 主站间气象报文信息共享的传输方案 (N = {N_max})")
print("传输轮数序号\t发送站点序号\t接收站点序号\t发送信息所属站点序号")
for idx, (send, receive, info) in enumerate(main_station_plan, start=1):
    print(f"{idx}\t{send}\t{receive}\t{info}")

# 保存主站间气象报文信息共享的传输方案为CSV文件
df_main = pd.DataFrame(main_station_plan, columns=["发送站点序号", "接收站点序号", "发送信息所属站点序号"])
df_main.index += 1  # 传输轮数序号从1开始
df_main.index.name = "传输轮数序号"
df_main.to_csv("main_station_plan.csv", encoding='utf-8-sig')

# 根据一般传输模型给出副站气象报文的传输方案
def generate_sub_station_plan(N):
    plan = []
    for i in range(1, N + 1):
        plan.append((station_number_to_letter(i), station_number_to_letter((i % N) + 1), f"{station_number_to_letter(i)}(1)"))
        plan.append((station_number_to_letter(i), station_number_to_letter((i % N) + 1), f"{station_number_to_letter(i)}(2)"))
    return plan

# 生成副站气象报文的传输方案
sub_station_plan = generate_sub_station_plan(N_max)

# 输出副站气象报文的传输方案
print(f"表2 副站气象报文的传输方案 (N = {N_max})")
print("传输轮数序号\t发送站点序号\t接收站点序号\t发送信息所属站点序号 (含信息完整性)")
for idx, (send, receive, info) in enumerate(sub_station_plan, start=1):
    print(f"{idx}\t{send}\t{receive}\t{info}")

# 保存副站气象报文的传输方案为CSV文件
df_sub = pd.DataFrame(sub_station_plan, columns=["发送站点序号", "接收站点序号", "发送信息所属站点序号 (含信息完整性)"])
df_sub.index += 1  # 传输轮数序号从1开始
df_sub.index.name = "传输轮数序号"
df_sub.to_csv("sub_station_plan.csv", encoding='utf-8-sig')

# 计算平均成功接收情况
def calculate_success_probabilities(success_rate, num_stations):
    prob_at_least_one = 1 - (1 - success_rate) ** num_stations
    avg_successful_receptions = num_stations * success_rate
    return prob_at_least_one, avg_successful_receptions

# 假设副站发送和接收消息的成功率为80%
success_rate = 0.80
num_stations = 2

# 计算成功接收概率
prob_at_least_one, avg_successful_receptions = calculate_success_probabilities(success_rate, num_stations)

# 输出成功接收概率
print(f"平均有 {prob_at_least_one * 100:.2f}% 的主站能成功接收每支分队至少一个副站的气象报文")
print(f"任一主站平均能成功接收 {avg_successful_receptions:.2f} 个副站的气象报文")


