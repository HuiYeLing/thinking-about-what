import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# 读取CSV文件  
df = pd.read_csv('D:/study/begin/数模/py/obesity_data.csv')

# 创建一个标签编码器
le = LabelEncoder()

# 将所有的成因和肥胖水平转换为数值类型
df_encoded = df.copy()
for column in df_encoded.columns:
    df_encoded[column] = le.fit_transform(df_encoded[column])

# 将数据分为特征和目标
X = df_encoded.drop('肥胖水平', axis=1)
y = df_encoded['肥胖水平']

# 将数据分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建一个随机森林分类器
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# 训练模型
clf.fit(X_train, y_train)

# 预测测试集
y_pred = clf.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)

print(f'准确率: {accuracy}')