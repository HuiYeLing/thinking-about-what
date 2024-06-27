import numpy as np  
  
# 城市坐标列表  
citys = np.array([  
    [91.1333, 29.6502],  
    [114.2211, 30.7736],  
    [113.3245, 23.1505],  
    [116.5945, 40.0799],  
    [110.3287, 20.0567],  
    [126.6227, 45.7082]  
])  
  
# 计算两点间距离的函数  
def calculate_distance(p1, p2):  
    return np.sqrt(np.sum((p1 - p2) ** 2))  
  
# 假设所有城市之间都可以直达，不需要换乘  
def calculate_fares_and_times(distance, taxi_speed=80, bus_speed=50):  
    taxi_fare = 2 * distance  # 出租车价格是距离的2倍  
    taxi_time = distance / taxi_speed  # 出租车时间  
      
    if distance <= 30:  
        bus_fare = 2.5 * distance  # 豪华大巴在30公里内是距离的2.5倍  
    elif distance <= 70:  
        bus_fare = 1.7 * distance  # 豪华大巴在30-70公里内是距离的1.7倍  
    else:  
        bus_fare = 1.4 * distance  # 豪华大巴超过70公里是距离的1.4倍  
    bus_time = distance / bus_speed  # 豪华大巴时间  
      
    return taxi_fare, taxi_time, bus_fare, bus_time  
  
# 设定评价准则：综合考虑费用、时间和方便性（这里方便性简化为不需要换乘）  
def evaluate_trip(fares_and_times, weight_fare=1, weight_time=1, weight_convenience=1):  
    taxi_fare, taxi_time, bus_fare, bus_time = fares_and_times  
    # 假设方便性是一个常数，因为这里不考虑换乘  
    convenience = 1  # 或者可以根据具体需求进行调整  
      
    # 计算总评分  
    score_taxi = -weight_fare * taxi_fare - weight_time * taxi_time + weight_convenience  
    score_bus = -weight_fare * bus_fare - weight_time * bus_time + weight_convenience  
      
    # 选择最高评分的交通方式  
    if score_taxi > score_bus:  
        return 'taxi', score_taxi  
    else:  
        return 'bus', score_bus  
  
# 遍历所有城市对并计算最优方案  
for i in range(len(citys)):  
    for j in range(i+1, len(citys)):  
        distance = calculate_distance(citys[i], citys[j])  
        fares_and_times = calculate_fares_and_times(distance)  
        optimal_mode, optimal_score = evaluate_trip(fares_and_times)  
        print(f"从城市{i}到城市{j}的最优方案是乘坐{optimal_mode}，评分为{optimal_score:.2f}")