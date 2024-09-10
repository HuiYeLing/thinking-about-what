import matplotlib
import math
import matplotlib.pyplot as plt

# 设置字体以支持中文显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题



# 定义参数
NATURAL_MATING_PERIOD = 20  # 自然交配期（天）
GESTATION_PERIOD = 149  # 孕期（天）
LACTATION_PERIOD = 40  # 哺乳期（天）
FATTENING_PERIOD = 210  # 育肥期（天）
EMPTY_PERIOD = 20  # 空怀休整期（天）

# 每个阶段的羊栏容量
BARREN_EWE_CAPACITY = 14  # 空怀母羊栏容量
RAM_CAPACITY = 4  # 种公羊栏容量
MATING_CAPACITY = 14  # 自然交配期母羊栏容量
PREGNANT_EWE_CAPACITY = 8  # 怀孕母羊栏容量
LACTATING_EWE_CAPACITY = 6  # 哺乳期母羊栏容量
FATTENING_LAMB_CAPACITY = 14  # 育肥期羔羊栏容量

# 现有标准羊栏数量
TOTAL_BARNS = 112

# 每胎产羔数量
LAMB_PER_LITTER = 2

# 每年目标出栏数量
TARGET_LAMB_OUTPUT = 1500

# 计算每个阶段的羊栏需求
def calculate_barn_needs(ewe_count):
    mating_barns = ewe_count / MATING_CAPACITY
    pregnant_barns = ewe_count / PREGNANT_EWE_CAPACITY
    lactating_barns = ewe_count / LACTATING_EWE_CAPACITY
    fattening_barns = (ewe_count * LAMB_PER_LITTER) / FATTENING_LAMB_CAPACITY
    barren_barns = ewe_count / BARREN_EWE_CAPACITY
    return mating_barns, pregnant_barns, lactating_barns, fattening_barns, barren_barns

# 估算合理的种公羊和基础母羊数量
def estimate_sheep_numbers(total_barns):
    ewe_count = 0
    annual_outputs = []
    ewe_counts = []
    while True:
        mating_barns, pregnant_barns, lactating_barns, fattening_barns, barren_barns = calculate_barn_needs(ewe_count)
        total_needed_barns = mating_barns + pregnant_barns + lactating_barns + fattening_barns + barren_barns
        if total_needed_barns > total_barns:
            break
        ewe_count += 1
        annual_output = ewe_count * LAMB_PER_LITTER * (3 / 2)  # 每只基础母羊每2年生产3胎
        annual_outputs.append(annual_output)
        ewe_counts.append(ewe_count)
    
    ram_count = ewe_count / 50  # 种公羊与基础母羊比例
    return ewe_counts, annual_outputs, ram_count

# 估算现有标准羊栏数量的缺口
def estimate_barn_shortage(total_barns, target_output):
    ewe_counts, annual_outputs, _ = estimate_sheep_numbers(total_barns)
    for i, output in enumerate(annual_outputs):
        if output >= target_output:
            return 0
    additional_barns_needed = (target_output / annual_outputs[-1]) * total_barns - total_barns
    return additional_barns_needed

# 生成折线图
ewe_counts, annual_outputs, ram_count = estimate_sheep_numbers(TOTAL_BARNS)

# 确保折线图能够预测到目标出栏量
if annual_outputs[-1] < TARGET_LAMB_OUTPUT:
    additional_ewe_counts, additional_annual_outputs, _ = estimate_sheep_numbers(int(TOTAL_BARNS * (TARGET_LAMB_OUTPUT / annual_outputs[-1])))
    ewe_counts.extend(additional_ewe_counts[len(ewe_counts):])
    annual_outputs.extend(additional_annual_outputs[len(annual_outputs):])

plt.plot(ewe_counts, annual_outputs, marker='o')
plt.xlabel('基础母羊数量')
plt.ylabel('年化出栏羊只数量')
plt.title('基础母羊数量与年化出栏羊只数量的关系')
plt.grid(True)
plt.axhline(y=TARGET_LAMB_OUTPUT, color='r', linestyle='--', label='目标出栏数量')
plt.legend()
plt.show()

# 计算结果
barn_shortage = estimate_barn_shortage(TOTAL_BARNS, TARGET_LAMB_OUTPUT)

# 输出合理的基础母羊和种公羊数量
print(f"合理的基础母羊数量: {ewe_counts[-1]}")
print(f"合理的种公羊数量: {ram_count}")
print(f"年化出栏羊只数量范围: {annual_outputs[0]} - {annual_outputs[-1]}")

# 如果现有羊栏数量不足以达到目标出栏数量，计算所需的额外羊栏数量
if barn_shortage > 0:
    print(f"需要额外的标准羊栏数量: {barn_shortage}")
else:
    print("现有标准羊栏数量足够达到目标出栏数量。")