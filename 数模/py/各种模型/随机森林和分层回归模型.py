import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv(r"D:\study\begin\数模\py\obesity_data.csv")

# 分离目标变量和特征变量
y = df['肥胖水平']
X = df.drop('肥胖水平', axis=1)

# 数值特征和分类特征
numeric_features = ['年龄','身高','体重','食用蔬菜的频次','食用主餐的次数','两餐之间的食品消费','每日耗水量','高热量饮料消耗量','运动频率','TUE','CA酒精消耗量']
categorical_features = ['性别','家庭肥胖史','是否频繁食用高热量食物','是否吸烟','日常交通方式']

# 预处理数值特征：缺失值填充和标准化
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# 预处理分类特征：独热编码
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# 合并数值和分类特征预处理步骤
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# 创建线性回归模型管道
reg_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 拟合模型
reg_pipeline.fit(X_train, y_train)

# 预测
y_pred = reg_pipeline.predict(X_test)

# 评估模型（此处假设你的目标变量是数值型的，可以计算MSE, MAE等）
from sklearn.metrics import mean_squared_error, mean_absolute_error
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'Mean Absolute Error: {mae:.2f}')

# 你可以进一步绘制预测结果与实际结果的对比图等