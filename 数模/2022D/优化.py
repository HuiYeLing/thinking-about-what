import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def simulate_message_sharing(N):
    # 使用字母作为主站的标识符
    stations = [chr(65 + i) for i in range(N)]  # 生成 A, B, C, D, ...
    
    # 初始化每个主站的消息队列
    message_queues = {station: [] for station in stations}
    send_times = {station: 0 for station in stations}
    
    # 创建有向图
    G = nx.DiGraph()
    
    # 模拟消息传输过程
    K = N - 1  # 传输轮数，确保每个主站都有足够的时间接收所有其他主站的消息
    for t in range(K):
        for i in stations:
            if send_times[i] <= t:
                # 发送消息给其他主站
                for j in stations:
                    if i != j:
                        message_queues[j].append(f"Message from {i} at time {t}")
                        # 在图中添加边
                        G.add_edge(i, j)
                # 更新发送时间
                send_times[i] = t + 1
    
    # 检查每个主站是否接收到所有其他主站的消息
    for i in stations:
        received_messages = len(message_queues[i])
        expected_messages = (N-1) * K
        print(f"主站 {i} 接收到 {received_messages} 条消息，预期接收到 {expected_messages} 条消息")
        if received_messages == expected_messages:
            print(f"主站 {i} 成功接收到所有消息")
        else:
            print(f"主站 {i} 未能接收到所有消息")
    
    # 绘制有向图
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', arrowsize=20)
    plt.title("主站之间的消息传输过程")
    plt.show()

# 示例：模拟 5 个主站完成消息共享
simulate_message_sharing(5)

def calculate_min_k(N):
    return N - 1

def plot_n_vs_k(max_n):
    N_values = list(range(5, max_n + 1))
    K_values = [calculate_min_k(N) for N in N_values]
    plt.plot(N_values, K_values, marker='o')
    plt.xlabel('主站数量 N')
    plt.ylabel('最小传输轮数 K')
    plt.title('主站数量与最小传输轮数的关系')
    plt.grid(True)
    plt.show()

# 示例：绘制主站数量与最小传输轮数的关系图
plot_n_vs_k(20)