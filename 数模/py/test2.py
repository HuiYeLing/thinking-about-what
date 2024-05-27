import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 假设df是包含特征和标签的数据集
# 特征列包括'weight', 'height', 'vegetable_intake', 'high_calorie_food', ...
# 标签列是'obesity_type'（例如，0表示正常，1表示超重，2表示肥胖）

# 读取CSV文件  
df = pd.read_csv('D:/study/begin/数模/py/obesity_data.csv')
# 划分数据集为训练集和测试集
X = df.drop('肥胖水平', axis=1)  # 特征
y = df['肥胖水平']  # 标签
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建逻辑回归模型
model = LogisticRegression()

# 训练模型
model.fit(X_train, y_train)

# 预测测试集
y_pred = model.predict(X_test)

# 评估模型
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")

# 如果需要，可以将模型保存到文件或进行进一步的优化和部署