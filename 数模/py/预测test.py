import pandas as pd
import matplotlib.pyplot as plt
# 读取CSV文件  
df = pd.read_csv('D:/study/begin/数模/py/obesity_data.csv')

def calculate_bmi(weight_kg, height_m):  
    bmi = weight_kg / (height_m ** 2)  
    return bmi  

# 设置字体为SimHei显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def classify_obesity(bmi):  
    if bmi < 18.5:  
        return "体重不足"  
    elif 18.5 <= bmi < 24.0:  
        return "正常"  
    elif 24.0 <= bmi < 28.0:  
        return "肥胖类型1"  
    elif 28.0 <= bmi < 30.0:  
        return "肥胖类型2"  
    elif 30.0 <= bmi < 35.0:  
        return "肥胖类型3"  
    elif 35.0 <= bmi < 40.0:  
        return "一级超重"  
    else:  
        return "二级超重"

# 计算BMI并添加到新的列中
df['BMI'] = calculate_bmi(df['体重'], df['身高'])

# 计算肥胖等级并添加到新的列中
df['Obesity_Level'] = df['BMI'].apply(classify_obesity)

# 保存到新的CSV文件，并指定编码格式为utf-8
df.to_csv('D:/study/begin/数模/py/obesity_data_with_bmi.csv', index=False, encoding='gbk')