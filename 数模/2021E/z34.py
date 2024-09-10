import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from scipy.signal import savgol_filter
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import accuracy_score, mean_squared_error, make_scorer
import numpy as np

# 读取数据
data = pd.read_excel('数模/2021E/E/附件4.xlsx')

# 数据清洗
for column in data.select_dtypes(include=['float64', 'int64']).columns:
    mean = data[column].mean()
    std = data[column].std()
    data = data[(data[column] >= mean - 3 * std) & (data[column] <= mean + 3 * std)]

# 将 'Class' 列中的类别转换为数值类型
label_encoder = LabelEncoder()
data['Class'] = label_encoder.fit_transform(data['Class'].astype(str)) + 1  # 转换为 1, 2, 3

# 检查并处理类别数量不足的问题
class_counts = data['Class'].value_counts()
sufficient_class_data = data[data['Class'].isin(class_counts[class_counts > 1].index)]

# 数据分割
train_data, test_data = train_test_split(sufficient_class_data, test_size=0.2, stratify=sufficient_class_data['Class'])

# 光谱预处理
def preprocess_spectrum(spectrum):
    # 去噪：使用Savitzky-Golay滤波器
    smoothed = savgol_filter(spectrum, window_length=11, polyorder=2)
    
    # 归一化：标准化到相同的尺度
    scaler = StandardScaler()
    normalized = scaler.fit_transform(smoothed.reshape(-1, 1)).flatten()
    
    # 基线校正：假设基线为最小值
    baseline_corrected = normalized - np.min(normalized)
    
    return baseline_corrected

# 对训练集和测试集的光谱数据进行预处理
for column in train_data.select_dtypes(include=['float64', 'int64']).columns:
    train_data[column] = preprocess_spectrum(train_data[column].values)
    test_data[column] = preprocess_spectrum(test_data[column].values)

# 将所有列名转换为字符串类型
train_data.columns = train_data.columns.astype(str)
test_data.columns = test_data.columns.astype(str)

# 特征选择（假设已经计算了VIP分数）
def get_vip_scores(data):
    # 伪代码：实际实现需要根据具体模型计算VIP分数
    return np.random.rand(data.shape[1])

numeric_columns = train_data.select_dtypes(include=['float64', 'int64']).columns

# 定义 PLS 模型
pls_class = PLSRegression(n_components=2)
pls_op = PLSRegression(n_components=2)

# 训练 PLS 模型
pls_class.fit(train_data[numeric_columns], train_data['Class'])
pls_op.fit(train_data[numeric_columns], train_data['OP'])

# 定义自定义评分函数
accuracy_scorer = make_scorer(accuracy_score)
mse_scorer = make_scorer(mean_squared_error)

# 使用交叉验证评估模型
class_scores = cross_val_score(pls_class, train_data[numeric_columns], train_data['Class'], cv=5, scoring=accuracy_scorer)
op_scores = cross_val_score(pls_op, train_data[numeric_columns], train_data['OP'], cv=5, scoring=mse_scorer)

print("Class模型的交叉验证准确率:", class_scores)
print("OP模型的交叉验证均方误差:", op_scores)

# 预测并评估最终模型
class_predictions = pls_class.predict(test_data[numeric_columns])
op_predictions = pls_op.predict(test_data[numeric_columns])

final_class_accuracy = accuracy_score(test_data['Class'], class_predictions.round())
final_op_mse = mean_squared_error(test_data['OP'], op_predictions)

print("Class模型的最终准确率:", final_class_accuracy)
print("OP模型的最终均方误差:", final_op_mse)

# 填充缺失值的函数
def fill_missing_values(data, model, features, target):
    missing_index = data[data[target].isnull()].index
    
    # 如果没有缺失值，直接返回原始数据
    if missing_index.empty:
        return data
    
    # 确保 features 中的列名存在于 data 中
    features = [feature for feature in features if feature in data.columns]
    
    # 提取特征数据
    feature_data = data.loc[missing_index, features]
    
    # 预测缺失值
    predicted_values = model.predict(feature_data)
    
    # 填充缺失值
    data.loc[missing_index, target] = predicted_values
    
    return data

# 确保 selected_features 的列名与 data 的列名一致
selected_features = numeric_columns.intersection(data.columns)

# 填充 Class 列的缺失值
data_filled = fill_missing_values(data, pls_class, selected_features, 'Class')

# 填充 OP 列的缺失值
data_filled = fill_missing_values(data_filled, pls_op, selected_features, 'OP')

# 将填充完的数据表输出到Excel文件
data_filled.to_excel('填充后的数据414.xlsx', index=False)