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
  
# 计算乘坐出租车和豪华大巴的费用  
def calculate_fares(distance):  
    taxi_fare = 2 * distance  # 出租车价格是距离的2倍  
    if distance <= 30:  
        bus_fare = 2.5 * distance  # 豪华大巴在30公里内是距离的2.5倍  
    elif distance <= 70:  
        bus_fare = 1.7 * distance  # 豪华大巴在30-70公里内是距离的1.7倍  
    else:  
        bus_fare = 1.4 * distance  # 豪华大巴超过70公里是距离的1.4倍  
    return taxi_fare, bus_fare  
  
# 初始化一个字典来存储所有城市对之间的最低费用  
min_fares = {}  
  
# 遍历所有可能的城市对  
for i in range(len(citys)):  
    for j in range(i+1, len(citys)):  
        # 计算距离  
        distance = calculate_distance(citys[i], citys[j])  
        # 计算费用  
        taxi_fare, bus_fare = calculate_fares(distance)  
        # 选择最低费用  
        min_fare = min(taxi_fare, bus_fare)  
        # 存储最低费用和对应的交通方式  
        min_fares[(i, j)] = {  
            'distance': distance,  
            'taxi_fare': taxi_fare,  
            'bus_fare': bus_fare,  
            'min_fare': min_fare,  
            'mode': 'taxi' if taxi_fare == min_fare else 'bus'  
        }  
  
# 打印结果  
for key, value in min_fares.items():  
    print(f"从城市{key[0]}到城市{key[1]}的距离是{value['distance']:.2f}公里，最低费用是{value['min_fare']:.2f}元，推荐交通方式是{value['mode']}")