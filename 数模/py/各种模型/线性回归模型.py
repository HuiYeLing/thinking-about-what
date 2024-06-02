import pandas as pd
from sklearn.metrics import mean_squared_error
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
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='median'), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)])

# 创建Pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('scaler', StandardScaler()),
                           ('classifier', LinearRegression())])

# 拟合模型
pipeline.fit(X_train, y_train)

# 评估模型性能
y_pred = pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
