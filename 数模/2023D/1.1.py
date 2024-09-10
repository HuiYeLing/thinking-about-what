# 定义参数
NATURAL_MATING_PERIOD = 20  # 自然交配期（天）
PREGNANCY_PERIOD = 149      # 母羊孕期（天）
LACTATION_PERIOD = 40       # 哺乳期（天）
FATTENING_PERIOD = 210      # 羔羊育肥期（天）
REST_PERIOD = 20            # 母羊空怀休整期（天）
LAMB_PER_LITTER = 2         # 每胎产羔数量

# 每栏容量
MOTHER_SHEEP_PER_PEN = 14   # 每栏基础母羊数量
RAM_PER_PEN = 4             # 每栏种公羊数量
PREGNANT_SHEEP_PER_PEN = 8  # 每栏待产母羊数量
LACTATING_SHEEP_PER_PEN = 6 # 每栏哺乳母羊数量
FATTENING_LAMB_PER_PEN = 14 # 每栏育肥羔羊数量

# 标准羊栏数量
TOTAL_PENS = 112            # 标准羊栏数量

# 计算每年需要的基础母羊数量
def calculate_required_mother_sheep(desired_annual_output):
    cycles_per_year = 1.5  # 每只基础母羊每2年可生产3胎，即每年1.5胎
    lambs_per_cycle = desired_annual_output / cycles_per_year
    mother_sheep_per_cycle = lambs_per_cycle / LAMB_PER_LITTER
    return mother_sheep_per_cycle

# 计算每年需要的种公羊数量
def calculate_required_ram_sheep(mother_sheep_per_cycle):
    return mother_sheep_per_cycle / 50  # 按1:50的比例配置

# 计算所需的羊栏数量
def calculate_required_pens(mother_sheep_per_cycle):
    pens_for_mothers = mother_sheep_per_cycle / MOTHER_SHEEP_PER_PEN
    pens_for_rams = calculate_required_ram_sheep(mother_sheep_per_cycle) / RAM_PER_PEN
    pens_for_pregnant = mother_sheep_per_cycle / PREGNANT_SHEEP_PER_PEN
    pens_for_lactating = mother_sheep_per_cycle / LACTATING_SHEEP_PER_PEN
    pens_for_fattening = (mother_sheep_per_cycle * LAMB_PER_LITTER) / FATTENING_LAMB_PER_PEN
    return pens_for_mothers + pens_for_rams + pens_for_pregnant + pens_for_lactating + pens_for_fattening

# 计算在现有羊栏数量下的基础母羊和种公羊数量
def calculate_max_mother_sheep(total_pens):
    # 通过迭代找到最大基础母羊数量
    low, high = 0, total_pens * MOTHER_SHEEP_PER_PEN
    while low < high:
        mid = (low + high + 1) // 2
        if calculate_required_pens(mid) <= total_pens:
            low = mid
        else:
            high = mid - 1
    return low

# 计算年化出栏羊只数量
def calculate_annual_output(mother_sheep_per_cycle):
    cycles_per_year = 1.5  # 每只基础母羊每2年可生产3胎，即每年1.5胎
    return mother_sheep_per_cycle * cycles_per_year * LAMB_PER_LITTER

# 计算在现有羊栏数量下的基础母羊数量
max_mother_sheep = calculate_max_mother_sheep(TOTAL_PENS)
annual_output = calculate_annual_output(max_mother_sheep)

print(f"在现有羊栏数量下的基础母羊数量：{max_mother_sheep:.2f}只")
print(f"估算的年化出栏羊只数量：{annual_output:.2f}只")