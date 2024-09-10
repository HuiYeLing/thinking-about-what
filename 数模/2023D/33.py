import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义模拟参数
num_simulations = 90000  # 增加模拟次数
num_base_ewes = 42
breeding_success_rate = 0.85
gestation_period_mean = 148.5
gestation_period_std = 1.5
lambs_per_ewe_mean = 2.2
lamb_survival_rate = 0.97
lactation_period_base = 40
lactation_period_variation = 5
rest_period_min = 18

# 初始化记录
total_loss_list = []

# 进行模拟
for sim in range(num_simulations):
    # 配种成功模拟
    pregnant_ewes = np.random.binomial(num_base_ewes, breeding_success_rate)
    
    # 孕期和产羔数模拟
    gestation_periods = np.random.normal(gestation_period_mean, gestation_period_std, pregnant_ewes)
    lambs_per_ewe = np.random.negative_binomial(lambs_per_ewe_mean, 1/lambs_per_ewe_mean, pregnant_ewes)
    lamb_survival = np.random.binomial(lambs_per_ewe, lamb_survival_rate)
    
    # 哺乳期和育肥期模拟
    lactation_periods = np.random.randint(lactation_period_base - lactation_period_variation, 
                                          lactation_period_base + lactation_period_variation + 1, pregnant_ewes)
    fattening_periods = 210 + (lactation_period_base - lactation_periods) * 2
    
    # 计算损失
    total_loss = 0
    for i in range(pregnant_ewes):
        # 计算每个阶段的羊栏需求和损失
        breeding_loss = 20 * 3  # 配种期损失
        gestation_loss = gestation_periods[i] * 6  # 孕期损失
        lactation_loss = lactation_periods[i] * 7  # 哺乳期损失
        fattening_loss = fattening_periods[i] * 9  # 育肥期损失
        rest_loss = rest_period_min * 9  # 空怀休整期损失
        
        total_loss += breeding_loss + gestation_loss + lactation_loss + fattening_loss + rest_loss
    
    total_loss_list.append(total_loss)

# 贝叶斯更新函数
def bayesian_update(prior, likelihood):
    posterior = prior * likelihood
    posterior /= posterior.sum()  # 归一化
    return posterior

# 假设先验分布是均匀分布
prior = np.ones(num_simulations) / num_simulations

# 计算每个模拟结果的似然
likelihood = np.exp(-np.array(total_loss_list) / np.mean(total_loss_list))

# 更新后验分布
posterior = bayesian_update(prior, likelihood)

# 选择后验概率最大的生产计划
optimal_index = np.argmax(posterior)
optimal_loss = total_loss_list[optimal_index]

# 绘制总损失分布
plt.figure(figsize=(12, 6))
plt.hist(total_loss_list, bins=30, color='red', alpha=0.7)
plt.title('总损失分布')
plt.xlabel('总损失')
plt.ylabel('频率')
plt.tight_layout()
plt.show()

# 输出最优生产计划
print(f"最优生产计划的总损失为: {optimal_loss}")