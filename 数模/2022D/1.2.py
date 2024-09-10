import pandas as pd
import numpy as np

def simulate_message_sharing(N, K):
    # 初始化每个主站的消息队列
    message_queues = {i: [f"{i}_完整"] for i in range(1, N+1)}  # 每个主站初始有一个完整的自己的消息
    
    # 记录消息传输过程
    transmission_log = []
    
    # 模拟消息传输过程
    for t in range(1, K+1):
        for i in range(1, N+1):  # 只考虑主站发送消息
            # 发送消息给其他主站
            for j in range(1, N+1):
                if i != j:
                    # 发送消息
                    if len(message_queues[i]) >= 150:
                        message_to_send = message_queues[i][:150]
                        message_queues[i] = message_queues[i][150:]
                    else:
                        message_to_send = message_queues[i]
                        message_queues[i] = []
                    
                    message_queues[j].extend(message_to_send)  # 发送消息
                    # 记录传输日志
                    transmission_log.append([
                        t, 
                        i, 
                        j, 
                        message_to_send.copy(),  # 发送的信息
                        message_queues[j].copy()  # 接收站点已有的信息
                    ])
    
    return transmission_log

def evaluate_model(transmission_log, N):
    # 转换为 DataFrame
    df = pd.DataFrame(transmission_log, columns=[
        '传输轮数', 
        '发送站点序号', 
        '接收站点序号', 
        '发送信息所属站点序号(含信息完整性)', 
        '此轮后接收站点已有信息所属站点序号(含信息完整性)'
    ])
    
    # 计算每个主站成功接收每支分队至少一个副站的气象报文的概率
    success_probabilities = []
    for i in range(1, N+1):
        received_messages = df[df['接收站点序号'] == i]['发送信息所属站点序号(含信息完整性)'].explode().unique()
        success_probability = len(received_messages) / (N - 1)
        success_probabilities.append(success_probability)
    
    return success_probabilities

# 示例调用
N = 9
K = 5
transmission_log = simulate_message_sharing(N, K)
success_probabilities = evaluate_model(transmission_log, N)

# 打印结果
print(f"在 {K} 分钟内，{N} 个主站间气象报文的信息共享成功接收概率：")
for i, prob in enumerate(success_probabilities, 1):
    print(f"主站 {i} 的成功接收概率：{prob:.2f}")

# 保存结果为表格
df = pd.DataFrame(transmission_log, columns=[
    '传输轮数', 
    '发送站点序号', 
    '接收站点序号', 
    '发送信息所属站点序号(含信息完整性)', 
    '此轮后接收站点已有信息所属站点序号(含信息完整性)'
])
df.to_csv('message_sharing_log.csv', index=False, encoding='utf-8-sig')