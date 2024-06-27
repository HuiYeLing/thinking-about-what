import numpy as np
import pandas as pd
import seaborn as sns
#忽略警号消息
import warnings
import os
warnings.filterwarnings("ignore")

import matplotlib
import matplotlib.pyplot as plt

#设置中文显示
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['font.size']=14
#解决负号问题
matplotlib.rcParams['axes.unicode_minus'] =False

data = pd.read_excel(r'D:\study\begin\python\城市比赛\1\宁波市GDP.xls', index_col=0)
# print(data.index)
# data.shape
# data.info()
# data.isna().sum()

# # 从第八行开始提取年份信息
# years = data.index[7:]
# # 将索引转换为列表（如果需要）
# years_list = years.tolist()
# # 打印年份列表查看
# print(years_list)
# # 从第八行开始提取生产总值数据
# gdp_values = data.iloc[7:, 0]  # 使用iloc访问从第八行开始的第一列数据
# # 将生产总值数据转换为列表
# gdp_list = gdp_values.tolist()
# # 打印生产总值列表查看
# print(gdp_list)

# 从第八行开始提取年份和生产总值数据
years = data.iloc[7:, 0].tolist()  # 第一列是年份数据
gdp_values = data.iloc[7:, 1].tolist()  # 第二列是生产总值数据

# 绘制年份与生产总值的折线图
plt.figure(figsize=(10, 6))  # 设置图形的大小
plt.plot(years, gdp_values, marker='o', linestyle='-', color='b')  # 绘制折线图
plt.title('年份与生产总值的关系')  # 添加标题
plt.xlabel('年份')  # 添加x轴标签
plt.ylabel('生产总值（亿元）')  # 添加y轴标签
plt.xticks(rotation=45)  # 旋转x轴标签，以便更好地显示
plt.grid(True)  # 显示网格
plt.show()  # 显示图形

