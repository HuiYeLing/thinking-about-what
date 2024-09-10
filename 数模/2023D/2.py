import cvxpy as cp

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

# 定义决策变量
x1 = cp.Variable()  # 基础母羊数量
x2 = cp.Variable()  # 种公羊数量

# 定义目标函数（引入二次项）
objective = cp.Maximize(3 * x1 - 0.01 * cp.square(x1))

# 定义约束条件
constraints = [
    x1 / MOTHER_SHEEP_PER_PEN + x2 / RAM_PER_PEN + x1 / PREGNANT_SHEEP_PER_PEN + x1 / LACTATING_SHEEP_PER_PEN + (x1 * LAMB_PER_LITTER) / FATTENING_LAMB_PER_PEN <= TOTAL_PENS,
    x2 >= x1 / 50,  # 种公羊与基础母羊的比例
    x1 >= 0,
    x2 >= 0
]

# 定义问题
problem = cp.Problem(objective, constraints)

# 求解问题
problem.solve()

# 计算年化出栏羊只数量
annual_output = 3 * x1.value - 0.01 * x1.value**2

# 计算现有标准羊栏数量的缺口
target_annual_output = 1500
required_mother_sheep = target_annual_output / (1.5 * LAMB_PER_LITTER)
required_ram_sheep = required_mother_sheep / 50
required_pens = required_mother_sheep / MOTHER_SHEEP_PER_PEN + required_ram_sheep / RAM_PER_PEN + required_mother_sheep / PREGNANT_SHEEP_PER_PEN + required_mother_sheep / LACTATING_SHEEP_PER_PEN + (required_mother_sheep * LAMB_PER_LITTER) / FATTENING_LAMB_PER_PEN
pen_shortage = required_pens - TOTAL_PENS

# 生成具体的生产计划
def generate_production_plan(mother_sheep, ram_sheep):
    plan = {
        "空怀休整期": mother_sheep / MOTHER_SHEEP_PER_PEN,
        "非交配期种公羊": ram_sheep / RAM_PER_PEN,
        "自然交配期": mother_sheep / MOTHER_SHEEP_PER_PEN,
        "怀孕期": mother_sheep / PREGNANT_SHEEP_PER_PEN,
        "哺乳期": mother_sheep / LACTATING_SHEEP_PER_PEN,
        "育肥期": (mother_sheep * LAMB_PER_LITTER) / FATTENING_LAMB_PER_PEN
    }
    return plan

production_plan = generate_production_plan(x1.value, x2.value)

print(f"合理的基础母羊数量：{x1.value:.2f}只")
print(f"合理的种公羊数量：{x2.value:.2f}只")
print(f"估算的年化出栏羊只数量：{annual_output:.2f}只")
print(f"现有标准羊栏数量的缺口：{pen_shortage:.2f}个")
print("具体的生产计划：")
for stage, pens in production_plan.items():
    print(f"{stage} 需要的羊栏数量：{pens:.2f}个")