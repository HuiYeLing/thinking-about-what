import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import numpy as np

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

# 计算统计特征
features = pd.DataFrame()
features['mean'] = data.iloc[:, 1:-1].mean(axis=1)
features['std'] = data.iloc[:, 1:-1].std(axis=1)
features['min'] = data.iloc[:, 1:-1].min(axis=1)
features['max'] = data.iloc[:, 1:-1].max(axis=1)

# 使用PCA进行降维
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data.iloc[:, 1:-1])
pca = PCA(n_components=2)
pca_features = pca.fit_transform(scaled_data)

# 将PCA特征添加到特征数据框中
features['pca1'] = pca_features[:, 0]
features['pca2'] = pca_features[:, 1]

# 使用肘部法确定最佳K值
sse = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(pca_features)
    sse.append(kmeans.inertia_)

plt.figure(figsize=(10, 8))
plt.plot(k_range, sse, marker='o')
plt.xlabel('聚类数目K')
plt.ylabel('总误差平方和 (SSE)')
plt.title('肘部法确定最佳K值')
plt.show()

# 使用轮廓系数法确定最佳K值
silhouette_scores = []
for k in k_range[1:]:  # 轮廓系数法不适用于K=1
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(pca_features)
    silhouette_scores.append(silhouette_score(pca_features, labels))

plt.figure(figsize=(10, 8))
plt.plot(k_range[1:], silhouette_scores, marker='o')
plt.xlabel('聚类数目K')
plt.ylabel('轮廓系数')
plt.title('轮廓系数法确定最佳K值')
plt.show()

# 使用最佳K值进行K-means聚类（假设最佳K值为3）
best_k = 3  # 你可以根据上面的图表选择最佳K值
kmeans = KMeans(n_clusters=best_k, random_state=42)
features['cluster'] = kmeans.fit_predict(pca_features)

print(features.head())

# 计算三种聚类的占比
cluster_counts = features['cluster'].value_counts()
cluster_percentages = cluster_counts / len(features) * 100
print("聚类类别的数量：")
print(cluster_counts)
print("\n聚类类别的占比：")
print(cluster_percentages)

# 可视化聚类结果
plt.figure(figsize=(10, 8))
plt.scatter(features['pca1'], features['pca2'], c=features['cluster'], cmap='viridis')
plt.xlabel('主成分1')
plt.ylabel('主成分2')
plt.title('药品特征的K-means聚类分析')
plt.colorbar(label='聚类类别')
plt.show()