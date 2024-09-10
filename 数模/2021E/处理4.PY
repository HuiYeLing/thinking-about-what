import pandas as pd
from scipy.signal import savgol_filter
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# 读取数据
data1 = pd.read_excel('数模/2021E/E/附件4_cleaned.xlsx')

# 将所有列名转换为字符串类型
data1.columns = data1.columns.astype(str)

# 打印列名以检查数据结构
print("数据列名：", data1.columns)

# 假设我们对所有数值型列进行去噪处理
numeric_columns = data1.select_dtypes(include=['float64', 'int64']).columns

# 检查并处理缺失值
data1[numeric_columns] = data1[numeric_columns].fillna(method='ffill').fillna(method='bfill')

# 对每个数值型列进行去噪处理
for col in numeric_columns:
    data1[col] = savgol_filter(data1[col], window_length=5, polyorder=2)

# 初始化 StandardScaler
scaler = StandardScaler()

# 对数值型列进行归一化处理
data1[numeric_columns] = scaler.fit_transform(data1[numeric_columns])

# 将分类变量转换为哑变量
data1 = pd.get_dummies(data1)

# 假设 'OP' 是目标变量
X = data1.drop(columns=['OP'])
y = data1['OP']

# 将目标变量转换为数值类型
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 使用 PCA 进行降维
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# 建立线性回归模型
lr = LinearRegression()
lr.fit(X_train_pca, y_train)

# 预测
y_pred = lr.predict(X_test_pca)

# 计算均方误差
mse = mean_squared_error(y_test, y_pred)
print(f"均方误差: {mse}")

# 保存模型和预处理器
joblib.dump(lr, 'linear_regression_model.pkl')
joblib.dump(pca, 'pca_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')

print("线性回归模型和 PCA 模型建立完成，并已保存到 'linear_regression_model.pkl' 和 'pca_model.pkl'")