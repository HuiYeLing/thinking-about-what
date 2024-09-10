import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

# 读取数据
data = pd.read_excel('数模/2021E/E/附件3.xlsx')

def calculate_absorbance_features(data_row):
    # 假设数据行是从0开始索引的，并且吸光度数据从第4个元素开始
    # 检查数据行是否足够长以包含吸光度数据
    if len(data_row) < 4:
        return None, None, None, None  # 数据行太短，无法计算特征
    
    # 提取吸光度数据
    absorbance_data = data_row[3:]
    
    # 计算最大值、平均值、标准差和范围
    max_value = np.max(absorbance_data)
    avg_value = np.mean(absorbance_data)
    std_dev = np.std(absorbance_data)
    min_value = np.min(absorbance_data)
    
    # 计算范围
    range_value = max_value - min_value
    
    return max_value, avg_value, std_dev, range_value

# 计算每一行的吸光度特征
features = data.apply(lambda row: calculate_absorbance_features(row), axis=1)
features_df = pd.DataFrame(features.tolist(), columns=['max', 'mean', 'std', 'range'])

print("Features shape:", features_df.shape)

# 检测缺失值
missing_values = features_df.isnull().sum()
print("缺失值统计:\n", missing_values)

# 处理缺失值，用KNN填充
imputer = KNNImputer(n_neighbors=5)
imputed_features = imputer.fit_transform(features_df)

print("Imputed features shape:", imputed_features.shape)

# 将填充后的数据转换回DataFrame
imputed_features_df = pd.DataFrame(imputed_features, columns=features_df.columns)

# 将填充后的数据保存到新的Excel文件
imputed_features_df.to_excel('填充后的数据3.xlsx', index=False)

print("缺失值填充完成，并已保存到 '填充后的数据3.xlsx'")