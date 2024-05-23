import numpy as np
import pandas as pd
data = pd.read_csv(r'D:\study1\data\obesity_level.csv')
#忽略警号消息
import warnings
warnings.filterwarnings("ignore")

import matplotlib
import matplotlib.pyplot as plt
#设置中文显示
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['font.size']=14
#解决负号问题
matplotlib.rcParams['axes.unicode_minus'] =False
print(data) 


# 将 'age' 列的数据转换为整数
data['Age'] = data['Age'].astype(int)

print(data)

# 将 DataFrame 输出到一个新的 CSV 文件
data.to_csv(r'D:\study1\data\obesity_level_cleaned.csv', index=False)