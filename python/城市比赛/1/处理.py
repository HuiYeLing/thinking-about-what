import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data_dict = {
 '年份': ['2000', '2005', '2010', '2015', '2020'],
 '总人口（万人）': [613.87, 639.3, 704.07, 828.27, 1006.08],
 'GDP（亿元）': [720.85, 1589.41, 4440.32, 8502.6, 12142.52],
 '社会消费品零售总额（亿元）': [332.16, 691.24, 1622.09, 3150.24, 4469.76],
 '货物运输量（万吨）': [5910, 10991, 22947, 33932, 38838],
 '城镇居民人均可支配收入（元）': [7529.76, 12433.9, 22813.9, 39961.1, 57971],
 '农村居民人均可支配收入（元）': [2941, 4735, 10639.8, 23601, 34754],
 '用电量（万度）': [221763, 923856, 1603152, 2464961, 4116782]
}

df = pd.DataFrame(data_dict)

# Calculate the correlation matrix
corr = df.corr()

# Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Pearson Correlation Matrix Heatmap')
plt.show()
