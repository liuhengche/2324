import sys
sys.path.append(r"c:\users\yachaoyan2\appdata\roaming\python\python39\site-packages")
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.multioutput import MultiOutputRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
import os

# 定义特征列和权重（确保列索引正确）
features = [10, 17, 23, 29]  # 对应 FG%, eFG%, TRB, PTS
feature_names = ['FG%', 'eFG%', 'TRB', 'PTS']  # 特征的真实名称
weights = np.array([0.4, 0.3, 0.2, 0.1])  # 权重

# 读取训练数据（2021-2022赛季）
with open('2021-2022_processed1.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data1 = list(reader)

# 转换为DataFrame并移除表头
data1 = pd.DataFrame(data1[1:], columns=data1[0])

# 提取特征并应用权重
data_scaled = data1.iloc[:, features].astype(float) * weights
knn = NearestNeighbors(n_neighbors=5, metric='euclidean')
knn.fit(data_scaled)

# 读取测试数据（2022-2023赛季）
with open('2022-2023_processed1.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data2 = list(reader)

data2 = pd.DataFrame(data2[1:], columns=data2[0])

with open('2023-2024_processed1.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data3 = list(reader)

data3 = pd.DataFrame(data3[1:], columns=data3[0])

# 处理每一行并绘制雷达图
for i in range(min(len(data2),len(data2))):
    try:
        target_name = data2.iloc[i, 1]  # 假设第0列是球员名字
        target_stats = data2.iloc[i, features].astype(float).values  # 目标球员数据
       
        # 查找最近邻
        distances, indices = knn.kneighbors([target_stats * weights])
        similar_players = data1.iloc[indices[0]]
        similar_stats = similar_players.iloc[:, features].astype(float).mean(axis=0).values  # 相似球员平均值

        similar_player_names = similar_players.iloc[:, 1].tolist()        
        similar_2021_2022 = data1[data1.iloc[:, 1].isin(similar_player_names)]
        similar_2022_2023 = data2[data2.iloc[:, 1].isin(similar_player_names)]
        #similar_2023_2024 = data3[data3.iloc[:, 1].isin(similar_player_names)]
        similar_2021_2022 = similar_2021_2022.sort_values(by=data1.columns[1])
        similar_2022_2023 = similar_2022_2023.sort_values(by=data2.columns[1])
       
        X = similar_2021_2022.iloc[:, features].astype(float).values
        y = similar_2022_2023.iloc[:, features].astype(float).values

        if len(X) == 0 or len(y) == 0:
            raise ValueError("没有找到匹配的相似球员数据")
        if X.shape[0] != y.shape[0]:
            raise ValueError(f"数据不匹配: X有{X.shape[0]}样本，y有{y.shape[0]}样本")
       
        model = MultiOutputRegressor(XGBRegressor())

        # 训练模型
        model.fit(X, y)

        new_data = np.array([data2.iloc[i, features].astype(float).values])
        predictions = model.predict(new_data)
        print(predictions)
                   
    except Exception as e:
        print(f"Error processing row {i}: {e}")
        continue



print("Radar charts saved for all players!")
