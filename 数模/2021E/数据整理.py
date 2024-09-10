import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA
import numpy as np
from scipy.signal import find_peaks, peak_widths

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 设置显示中文字体 宋体
mpl.rcParams["axes.unicode_minus"] = False  # 字体更改后，会导致坐标轴中的部分字符无法正常显示，此时需要设置正常显示负号

# 读取数据
data = pd.read_excel('数模/2021E/E/处理后数据.xlsx')

# 查看数据的基本信息
data.info()
print(data.head())  # 查看数据的前五行
print(data.describe())  # 查看数据的描述性统计
print(data.isnull().sum())  # 查看数据的缺失值
data.isna().sum()  # 查看数据的缺失值

# 处理缺失值（这里假设用均值填充）
data.fillna(data.mean(), inplace=True)

# 处理异常值
def handle_outliers(df):
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[column] = df[column].apply(lambda x: lower_bound if x < lower_bound else (upper_bound if x > upper_bound else x))
    return df

data = handle_outliers(data)

# 删除负值
data.iloc[:, 1:] = data.iloc[:, 1:].applymap(lambda x: None if x < 0 else x)

# 删除极大值和极小值
def remove_extreme_values(df, threshold=3):
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        mean = df[column].mean()
        std = df[column].std()
        upper_bound = mean + threshold * std
        lower_bound = mean - threshold * std
        df[column] = df[column].apply(lambda x: None if x > upper_bound or x < lower_bound else x)
    return df

data = remove_extreme_values(data)
data.dropna(inplace=True)

# 处理孤立点
iso_forest = IsolationForest(contamination=0.05, random_state=42)
outliers = iso_forest.fit_predict(data.iloc[:, 1:])
data = data[outliers == 1]

# PCA降维
pca = PCA(n_components=0.95)  # 保留95%的方差
pca_features = pca.fit_transform(data.iloc[:, 1:])

# 处理多变量异常值
def mahalanobis_distance(df):
    mean = np.mean(df, axis=0)
    cov = np.cov(df, rowvar=False)
    inv_covmat = np.linalg.inv(cov)
    left_term = np.dot((df - mean), inv_covmat)
    mahal = np.dot(left_term, (df - mean).T)
    return np.diagonal(mahal)

data['mahalanobis'] = mahalanobis_distance(pca_features)
threshold = np.percentile(data['mahalanobis'], 95)
data = data[data['mahalanobis'] < threshold]
data.drop(columns=['mahalanobis'], inplace=True)

# 统一小数点格式到小数点后六位
data.iloc[:, 1:] = data.iloc[:, 1:].applymap(lambda x: f'{x:.6f}' if isinstance(x, (int, float)) else x)

# 将数据转换回数值类型
data.iloc[:, 1:] = data.iloc[:, 1:].astype(float)

# 计算每种药材在不同波段的平均光谱强度
average_spectrum = data.groupby('No').mean()

# 确保 average_spectrum 中的所有数据都是数值类型
average_spectrum = average_spectrum.apply(pd.to_numeric)

# 计算药材的特征值（PCA）
pca = PCA(n_components=3)  # 假设提取3个主要特征
principal_components = pca.fit_transform(average_spectrum)
principal_df = pd.DataFrame(data=principal_components, columns=['特征1', '特征2', '特征3'])

# K-Means聚类计算
features = data.iloc[:, 1:]  # 假设所有数值列都是特征列
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42)  # 假设聚为3类
kmeans.fit(scaled_features)
data['Cluster'] = kmeans.labels_

# 可视化聚类结果
plt.figure(figsize=(12, 8))
sns.scatterplot(x=features.columns[0], y=features.columns[1], hue='Cluster', data=data, palette='viridis')
plt.title('K-Means聚类结果')
plt.xlabel(features.columns[0])
plt.ylabel(features.columns[1])
plt.show()

# 绘制所有样本的折线图
plt.figure(figsize=(12, 8))
for i in range(data.shape[0]):
    plt.plot(data.columns[1:-1], data.iloc[i, 1:-1], label=f'样本 {i+1}')
plt.title('所有样本的折线图')
plt.xlabel('波段')
plt.ylabel('值')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))  # 调整图例位置
plt.show()

# 峰检测及计算峰参数
plt.figure(figsize=(12, 8))
for i in range(data.shape[0]):
    spectrum = data.iloc[i, 1:-1].astype(float)
    peaks, properties = find_peaks(spectrum, height=0)  # 假设高度阈值为0
    widths = peak_widths(spectrum, peaks, rel_height=0.5)  # 计算峰宽度
    
    # 打印每个峰的参数
    for j, peak in enumerate(peaks):
        peak_position = data.columns[1:-1][peak]
        peak_height = properties['peak_heights'][j]
        peak_width = widths[0][j]
        peak_area = np.trapz(spectrum[peak - int(peak_width/2): peak + int(peak_width/2)], dx=1)
        print(f"样本 {i+1} - 峰 {j+1}: 位置={peak_position}, 强度={peak_height}, 宽度={peak_width}, 面积={peak_area}")
    
    plt.plot(data.columns[1:-1], spectrum, label=f'样本 {i+1}')

plt.title('所有样本的光谱')
plt.xlabel('波段')
plt.ylabel('值')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))  # 调整图例位置
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, peak_widths

# 假设'spectrum'是你的数据
# 这里假设'spectrum'是一个二维数组，每一行代表一个样本的光谱数据
# 'data.columns[1:-1]' 是波段信息

# 示例数据
data = pd.read_excel('数模/2021E/E/处理后数据.xlsx')
spectra = data.iloc[:, 1:-1].values  # 假设光谱数据在第2列到倒数第2列之间

for i, spectrum in enumerate(spectra):
    peaks, properties = find_peaks(spectrum, height=0)  # 假设高度阈值为0
    widths = peak_widths(spectrum, peaks, rel_height=0.5)  # 计算峰宽度
    
    # 打印每个峰的参数
    for j, peak in enumerate(peaks):
        peak_position = data.columns[1:-1][peak]
        peak_height = properties['peak_heights'][j]
        peak_width = widths[0][j]
        peak_area = np.trapz(spectrum[peak - int(peak_width/2): peak + int(peak_width/2)], dx=1)
        print(f"样本 {i+1} - 峰 {j+1}: 位置={peak_position}, 强度={peak_height}, 宽度={peak_width}, 面积={peak_area}")
    
    plt.plot(data.columns[1:-1], spectrum, label=f'样本 {i+1}')

# 计算所有样本的最高峰值、最低峰值和均值
all_values = spectra.flatten()
max_value = np.max(all_values)
min_value = np.min(all_values)
mean_value = np.mean(all_values)

print(f"所有样本的最高峰值: {max_value}")
print(f"所有样本的最低峰值: {min_value}")
print(f"所有样本的均值: {mean_value}")

plt.title('所有样本的光谱')
plt.xlabel('波段')
plt.ylabel('值')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))  # 调整图例位置
plt.show()

print("end")