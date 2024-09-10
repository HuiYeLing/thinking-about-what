import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
import matplotlib.pyplot as plt
# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义模拟参数
num_simulations = 10000
num_base_ewes = 42

# 初始化记录
pregnant_ewes_list = []
lambs_per_ewe_list = []
lamb_survival_list = []
total_loss_list = []

# 进行模拟
for sim in range(num_simulations):
    # 配种成功模拟
    pregnant_ewes = np.random.binomial(num_base_ewes, 0.85)
    pregnant_ewes_list.append(pregnant_ewes)
    
    # 孕期和产羔数模拟
    lambs_per_ewe = np.random.negative_binomial(2.2, 1/2.2, pregnant_ewes)
    lamb_survival = np.random.binomial(lambs_per_ewe, 0.97)
    lambs_per_ewe_list.extend(lambs_per_ewe)  # 使用 extend 而不是 append
    lamb_survival_list.extend(lamb_survival)  # 使用 extend 而不是 append
    
    # 计算损失
    # 假设损失计算为羊栏不足和空置损失的总和
    total_loss = (pregnant_ewes * 0.5 + lamb_survival.sum() * 0.2)  # 示例损失计算
    total_loss_list.append(total_loss)

# 绘制图表
plt.figure(figsize=(12, 6))

# 绘制孕期母羊数量分布
plt.subplot(1, 3, 1)
plt.hist(pregnant_ewes_list, bins=30, color='blue', alpha=0.7)
plt.title('孕期母羊数量分布')
plt.xlabel('孕期母羊数量')
plt.ylabel('频率')

# 绘制每只母羊的羔羊数量分布
plt.subplot(1, 3, 2)
plt.hist(lambs_per_ewe_list, bins=30, color='green', alpha=0.7)
plt.title('每只母羊的羔羊数量分布')
plt.xlabel('每只母羊的羔羊数量')
plt.ylabel('频率')

# 绘制总损失分布
plt.subplot(1, 3, 3)
plt.hist(total_loss_list, bins=30, color='red', alpha=0.7)
plt.title('总损失分布')
plt.xlabel('总损失')
plt.ylabel('频率')

plt.tight_layout()
plt.show()