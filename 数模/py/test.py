import numpy as np
import pandas as pd
import seaborn as sns
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
# 将 'Height' 列的数据保留两位小数，并转换为格式化字符串
data['Height'] = data['Height'].round(2).map('{:.2f}'.format)
# 将 'Weight' 列的数据转换为整数
data['Weight'] = data['Weight'].astype(int)
print(data)

# # 选择所有的数字列
# numeric_data = data.select_dtypes(include=[np.number])

# # 对每一个数值型特征，绘制它与 '0be1dad' 的散点图
# for column in numeric_data.columns:
#     if column != '0be1dad':
#         plt.figure(figsize=(6, 4))
#         sns.scatterplot(x=column, y='0be1dad', data=numeric_data)
#         plt.title(f'Relationship between {column} and 0be1dad')
#         plt.show()
# 查找重复的行
duplicates = data.duplicated()
print(f'Number of duplicate rows = {duplicates.sum()}')

# 删除重复的行
data = data.drop_duplicates()

# 再次查找重复的行，确认已经删除
duplicates = data.duplicated()
print(f'Number of duplicate rows after removal = {duplicates.sum()}')

# 检查每一列是否有缺失值
missing_values = data.isnull().sum()
print(missing_values)

# 检查整个数据集是否有缺失值
total_missing_values = missing_values.sum()
print(f'Total number of missing values in the dataset = {total_missing_values}')

# 定义一个映射字典，将肥胖水平的文本值映射为数字值
obesity_level_mapping = {
    'Ormal_Weight': 0,
    'Insufficient_Weight': -1,
    'Obesity_Type_I': 1,
    'Obesity_Type_ll': 2,
    'Obesity_Type_lll': 3,
    'Overweight_Level_I': 4,
    'Overweight_Level_Il': 5
}

# 使用 replace 函数替换值
data['0be1dad'] = data['0be1dad'].replace(obesity_level_mapping)

from scipy import stats
import numpy as np

# 计算 Z-Score
z_scores = np.abs(stats.zscore(data.select_dtypes(include=[np.number])))

# 定义一个阈值，通常使用的阈值是 3，这意味着所有 Z-Score 大于 3 的数据点都被认为是异常值
threshold = 3

# 获取异常值
outliers = data[(z_scores > threshold).all(axis=1)]
print(f'Number of outliers = {len(outliers)}')

# 将处理后的数据保存为新的 CSV 文件
data.to_csv(r'D:\study1\data\processed_obesity_level_new.csv', index=False)

import seaborn as sns

# 将 '0be1dad' 列的数据转换为数值类型，以便进行绘图
data['0be1dad'] = pd.to_numeric(data['0be1dad'], errors='coerce')

# 创建散点图
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Weight', y='0be1dad', data=data)
plt.title('Relationship between Weight and Obesity Level')
plt.show()