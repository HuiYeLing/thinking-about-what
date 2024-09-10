import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 设置显示中文字体 宋体
mpl.rcParams["axes.unicode_minus"] = False  # 字体更改后，会导致坐标轴中的部分字符无法正常显示，此时需要设置正常显示负号

# 读取数据
data = pd.read_excel('数模/2021E/E/附件4.xlsx')

# 取前100行数据
data = data.head(100)

# 将class列的ABCD换成对应的1234
data['Class'] = data['Class'].map({'A': 1, 'B': 2, 'C': 3, 'D': 4})

# 分离特征和目标变量
features = data.drop(columns=['Class', 'OP'])
class_target = data['Class']
op_target = data['OP']

# 将特征列的名称转换为字符串类型
features.columns = features.columns.astype(str)

# 填充Class列的缺失值
class_train = features[class_target.notna()]
class_target_train = class_target[class_target.notna()]
class_test = features[class_target.isna()]

log_reg_class = LogisticRegression()
log_reg_class.fit(class_train, class_target_train)
class_pred = log_reg_class.predict(class_test)

data.loc[class_target.isna(), 'Class'] = class_pred

# 填充OP列的缺失值
op_train = features[op_target.notna()]
op_target_train = op_target[op_target.notna()]
op_test = features[op_target.isna()]

log_reg_op = LogisticRegression()
log_reg_op.fit(op_train, op_target_train)
op_pred = log_reg_op.predict(op_test)

data.loc[op_target.isna(), 'OP'] = op_pred

# 打印填充后的数据
print(data.head(20))

# 输出填充后的数据到Excel文件
data.to_excel('填充后的数据.xlsx', index=False)