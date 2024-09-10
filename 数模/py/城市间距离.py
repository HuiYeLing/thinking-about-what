import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"] # 设置显示中文字体 宋体
mpl.rcParams["axes.unicode_minus"] = False #字体更改后，会导致坐标轴中的部分字符无法正常显示，此时需要设置正常显示负号

# 城市坐标和名称
coordinates = [
    (120.1214, 30.2213, '西湖'),
    (120.1013, 30.2408, '灵隐寺'),
    (120.1312, 30.1957, '六和塔'),
    (120.1185, 30.2531, '杭州植物园'),
    (121.5395, 29.8711, '天一阁'),
    (120.5855, 29.9923, '鲁迅故里')
]

# 计算两点之间的距离
def haversine(lon1, lat1, lon2, lat2):
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine公式
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # 地球平均半径，单位为公里
    return c * r

# 创建距离矩阵
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = haversine(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])

# 使用城市名称作为矩阵的行和列标签
city_names = [city[2] for city in coordinates]
df_distances = pd.DataFrame(distance_matrix, index=city_names, columns=city_names)

from matplotlib.colors import LinearSegmentedColormap

# 创建一个只包含白色的颜色映射
white_cmap = LinearSegmentedColormap.from_list('white_cmap', ['white', 'white'], N=256)

# 绘制热力图，使用自定义的白色颜色映射
plt.figure(figsize=(10, 8))
sns.heatmap(df_distances, annot=True, fmt=".2f", cmap=white_cmap, cbar=False)
plt.title('城市间距离矩阵图（单位：公里）')
plt.show()