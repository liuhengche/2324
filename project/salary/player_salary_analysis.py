import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# 读取数据
df = pd.read_csv("salaries_1985to2018.csv")
players = pd.read_csv("players.csv")

# 清洗薪资数据
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df = df.dropna(subset=['salary'])

# 合并球员信息
merged = df.merge(players, left_on='player_id', right_on='_id', how='left')
merged = merged.sort_values(['player_id', 'season_start'])
merged['career_year'] = merged.groupby('player_id').cumcount() + 1

# ---- 身高英寸转换 ----
def convert_height(height_str):
    try:
        feet, inches = height_str.split('-')
        return int(feet) * 12 + int(inches)
    except:
        return None

merged['height_inch'] = merged['height'].apply(convert_height)

# ---- 体重数值提取 ----
merged['weight_num'] = merged['weight'].str.replace('lb', '', regex=False).astype(float)

# ---- 清洗 draft_pick 字段 ----
def clean_draft_pick(draft_pick):
    try:
        # 提取数字部分
        pick = ''.join(filter(str.isdigit, draft_pick))
        return int(pick) if pick else None
    except:
        return None

# 处理 draft_pick 字段
merged['draft_pick'] = merged['draft_pick'].apply(clean_draft_pick)

# 转换为数值的表现特征
perf_features = [
    'career_AST', 'career_FG%', 'career_FG3%', 'career_FT%', 'career_G',
    'career_PER', 'career_PTS', 'career_TRB'
]
for col in perf_features:
    merged[col] = pd.to_numeric(merged[col], errors='coerce')

# ---- 取每个球员最后三年 ----
last3 = merged.groupby('player_id').apply(
    lambda x: x.sort_values('career_year', ascending=False).head(3)
).reset_index(drop=True)

# 计算每个球员最后三年的平均薪资
avg_salary = last3.groupby('player_id')['salary'].mean().reset_index(name='last3_avg_salary')

# 合并平均薪资数据
merged_last3 = last3.merge(avg_salary, on='player_id', how='left')

# ---- 绘制小提琴图 ----
plt.figure(figsize=(15, 10))

# 使用渐变色系，分别为每个小提琴图指定不同的颜色
color_map = plt.cm.get_cmap('viridis', 5)  # 选择5个颜色，使用 viridis 色系

# 小提琴图展示 last3_avg_salary 的分布
plt.subplot(2, 3, 1)
sns.violinplot(x=merged_last3['last3_avg_salary'], color=color_map(0))
plt.title('Distribution of Last 3 Years Average Salary')

# 小提琴图展示 career_PTS 的分布
plt.subplot(2, 3, 2)
sns.violinplot(x=merged_last3['career_PTS'], color=color_map(1))
plt.title('Distribution of Career Points (career_PTS)')

# 小提琴图展示 career_PER 的分布
plt.subplot(2, 3, 3)
sns.violinplot(x=merged_last3['career_PER'], color=color_map(2))
plt.title('Distribution of Career PER (career_PER)')

# 小提琴图展示 career_G 的分布
plt.subplot(2, 3, 4)
sns.violinplot(x=merged_last3['career_G'], color=color_map(3))
plt.title('Distribution of Career Games (career_G)')

# 小提琴图展示 draft_pick 的分布
plt.subplot(2, 3, 5)
sns.violinplot(x=merged_last3['draft_pick'], color=color_map(4))
plt.title('Distribution of Draft Pick (draft_pick)')

plt.tight_layout()  # 调整布局，使图形更紧凑
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# 读取数据
df = pd.read_csv("salaries_1985to2018.csv")
players = pd.read_csv("players.csv")

# 清洗薪资数据
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df = df.dropna(subset=['salary'])

# 合并球员信息
merged = df.merge(players, left_on='player_id', right_on='_id', how='left')
merged = merged.sort_values(['player_id', 'season_start'])
merged['career_year'] = merged.groupby('player_id').cumcount() + 1

# ---- 身高英寸转换 ----
def convert_height(height_str):
    try:
        feet, inches = height_str.split('-')
        return int(feet) * 12 + int(inches)
    except:
        return None

merged['height_inch'] = merged['height'].apply(convert_height)

# ---- 体重数值提取 ----
merged['weight_num'] = merged['weight'].str.replace('lb', '', regex=False).astype(float)

# ---- 清洗 draft_pick 字段 ----
def clean_draft_pick(draft_pick):
    try:
        # 提取数字部分
        pick = ''.join(filter(str.isdigit, draft_pick))
        return int(pick) if pick else None
    except:
        return None

# 处理 draft_pick 字段
merged['draft_pick'] = merged['draft_pick'].apply(clean_draft_pick)

# 转换为数值的表现特征
perf_features = [
    'career_AST', 'career_FG%', 'career_FG3%', 'career_FT%', 'career_G',
    'career_PER', 'career_PTS', 'career_TRB'
]
for col in perf_features:
    merged[col] = pd.to_numeric(merged[col], errors='coerce')

# ---- 取每个球员最后三年 ----
last3 = merged.groupby('player_id').apply(
    lambda x: x.sort_values('career_year', ascending=False).head(3)
).reset_index(drop=True)

avg_salary = last3.groupby('player_id')['salary'].mean().reset_index(name='last3_avg_salary')

# ---- 表现 + 身高体重 + draft_pick 特征 ----
player_stats = merged.drop_duplicates('player_id')[['player_id'] + perf_features + ['height_inch', 'weight_num', 'draft_pick']]
data = avg_salary.merge(player_stats, on='player_id').dropna()

# ---- 归一化 身高 & 体重 ----
data['height_inch'] = (data['height_inch'] - data['height_inch'].min()) / data['height_inch'].max()
data['weight_num'] = (data['weight_num'] - data['weight_num'].min()) / data['weight_num'].max()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("salaries_1985to2018.csv")
players = pd.read_csv("players.csv")

# 清洗薪资数据
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df = df.dropna(subset=['salary'])

# 合并球员信息
merged = df.merge(players, left_on='player_id', right_on='_id', how='left')

# ---- 清洗 draft_pick 字段 ----
def clean_draft_pick(draft_pick):
    try:
        pick = ''.join(filter(str.isdigit, str(draft_pick)))
        return int(pick) if pick else None
    except:
        return None

merged['draft_pick'] = merged['draft_pick'].apply(clean_draft_pick)

# 只保留有顺位信息的数据
valid_draft = merged.dropna(subset=['draft_pick'])

# ---- 可视化 draft_pick 分布 ----
plt.figure(figsize=(12, 6))

# 条状图（Histogram）
sns.histplot(valid_draft['draft_pick'], bins=60, kde=False, color='skyblue')
plt.title('Distribution of Draft Picks - Histogram')
plt.xlabel('Draft Pick Number')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# 核密度估计图（KDE）
plt.figure(figsize=(12, 6))
sns.kdeplot(valid_draft['draft_pick'], fill=True, color='orange')
plt.title('Distribution of Draft Picks - KDE')
plt.xlabel('Draft Pick Number')
plt.ylabel('Density')
plt.grid(True)
plt.show()


# 读取数据
df = pd.read_csv("salaries_1985to2018.csv")
players = pd.read_csv("players.csv")

# 清洗薪资数据
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df = df.dropna(subset=['salary'])

# 合并球员信息
merged = df.merge(players, left_on='player_id', right_on='_id', how='left')
# 清洗 draft_pick 字段
def clean_draft_pick(draft_pick):
    try:
        pick = ''.join(filter(str.isdigit, str(draft_pick)))
        return int(pick) if pick else None
    except:
        return None

merged['draft_pick'] = merged['draft_pick'].apply(clean_draft_pick)

# 去除缺失值
valid_draft = merged['draft_pick'].dropna()

# 计算统计量（含10th和50th百分位）
summary_stats = {
    'min': valid_draft.min(),
    'max': valid_draft.max(),
    'mean': valid_draft.mean(),
    '10th_percentile': valid_draft.quantile(0.10),
    '50th_percentile (median)': valid_draft.quantile(0.50)
}

# 打印结果
for key, value in summary_stats.items():
    print(f"{key}: {value:.2f}")


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("salaries_1985to2018.csv")
players = pd.read_csv("players.csv")

# 清洗薪资数据
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df = df.dropna(subset=['salary'])

# 合并球员信息
merged = df.merge(players, left_on='player_id', right_on='_id', how='left')

# ---- 分析 career_PTS 分布 ----
# 去除无效的得分数据
valid_pts = merged.dropna(subset=['career_PTS'])

# 条状图（Histogram）
plt.figure(figsize=(12, 6))
sns.histplot(valid_pts['career_PTS'], bins=60, kde=False, color='skyblue')
plt.title('Distribution of Career Points - Histogram')
plt.xlabel('Career Total Points')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# 核密度估计图（KDE）
plt.figure(figsize=(12, 6))
sns.kdeplot(valid_pts['career_PTS'], fill=True, color='orange')
plt.title('Distribution of Career Points - KDE')
plt.xlabel('Career Total Points')
plt.ylabel('Density')
plt.grid(True)
plt.show()


import pandas as pd

# 读取数据
df = pd.read_csv("salaries_1985to2018.csv")
players = pd.read_csv("players.csv")

# 合并球员信息
merged = df.merge(players, left_on='player_id', right_on='_id', how='left')

# 去除缺失值
valid_pts = merged['career_PTS'].dropna()

# 计算统计量
summary_stats = {
    'min': valid_pts.min(),
    'max': valid_pts.max(),
    'mean': valid_pts.mean(),
    '90th_percentile (top 10%) threshold': valid_pts.quantile(0.90),
    '50th_percentile (top 50%) threshold': valid_pts.quantile(0.50)
}

# 打印结果
for key, value in summary_stats.items():
    print(f"{key}: {value:.2f}")


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("salaries_1985to2018.csv")
players = pd.read_csv("players.csv")

# 清洗薪资数据
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df = df.dropna(subset=['salary'])

# 合并球员信息
merged = df.merge(players, left_on='player_id', right_on='_id', how='left')
merged = merged.sort_values(['player_id', 'season_start'])
merged['career_year'] = merged.groupby('player_id').cumcount() + 1

# ---- 按得分分组 ----
high_pts = merged[merged['career_PTS'] > 16.20]
mid_pts = merged[(merged['career_PTS'] <= 16.20) & (merged['career_PTS'] > 8.20)]
low_pts = merged[merged['career_PTS'] <= 8.20]

# 可视化
plt.figure(figsize=(12, 8))

# 绘制高得分球员的薪资分布
sns.scatterplot(x='career_year', y='salary', data=high_pts, label='High PTS (>16.20)', color='red')

# 绘制中等得分球员的薪资分布
sns.scatterplot(x='career_year', y='salary', data=mid_pts, label='Mid PTS (8.20-16.20)', color='skyblue')

# 绘制低得分球员的薪资分布
sns.scatterplot(x='career_year', y='salary', data=low_pts, label='Low PTS (<8.20)', color='orange')

plt.title('Salary Distribution by Career Points')
plt.xlabel('Career Year')
plt.ylabel('Salary')
plt.legend()
plt.grid(True)
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("salaries_1985to2018.csv")
players = pd.read_csv("players.csv")

# 清洗薪资数据
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df = df.dropna(subset=['salary'])

# 合并球员信息
merged = df.merge(players, left_on='player_id', right_on='_id', how='left')
merged = merged.sort_values(['player_id', 'season_start'])
merged['career_year'] = merged.groupby('player_id').cumcount() + 1

# ---- 清洗 draft_pick 字段 ----
def clean_draft_pick(draft_pick):
    try:
        pick = ''.join(filter(str.isdigit, str(draft_pick)))
        return int(pick) if pick else None
    except:
        return None

merged['draft_pick'] = merged['draft_pick'].apply(clean_draft_pick)

# 分组
top_pick = merged[merged['draft_pick'] < 3]
mid_pick = merged[(merged['draft_pick'] >= 3) & (merged['draft_pick'] <= 18)]
late_pick = merged[merged['draft_pick'] > 18]

# 可视化
plt.figure(figsize=(12, 8))

sns.scatterplot(x='career_year', y='salary', data=top_pick, label='Top Pick (<3)', color='red')
sns.scatterplot(x='career_year', y='salary', data=mid_pick, label='Mid Pick (3-18)', color='skyblue')
sns.scatterplot(x='career_year', y='salary', data=late_pick, label='Low Pick (>18)', color='orange')

plt.title('Salary Distribution by Draft Pick Tier')
plt.xlabel('Career Year')
plt.ylabel('Salary')
plt.legend()
plt.grid(True)
plt.show()


# 找到 top_pick 中 career_year 最大的值
max_year = top_pick['career_year'].max()

# 筛选 career_year 等于最大值的记录
max_career_top_pick = top_pick[top_pick['career_year'] == max_year]

# 按 salary 升序排序，找到薪资最低的那一条
lowest_salary_entry = max_career_top_pick.sort_values(by='salary').iloc[0]

# 打印该球员的所有信息
print("异常点对应球员信息：")
print(lowest_salary_entry)

# 如果你只关心几个关键字段：
print("\n关键字段：")
print("Name:", lowest_salary_entry['name'])
print("Draft Pick:", lowest_salary_entry['draft_pick'])
print("Career Year:", lowest_salary_entry['career_year'])
print("Salary:", lowest_salary_entry['salary'])
print("Season Start:", lowest_salary_entry['season_start'])
# 找到late pick中单个salary值最大的那条记录
max_salary_record = late_pick.loc[late_pick['salary'].idxmax()]
# 筛选出该球员的所有数据
tim_duncan_data = merged[merged['player_id'] == 'duncati01']

# 按 career_year 排序（保险起见）
tim_duncan_data = tim_duncan_data.sort_values('career_year')

# 可视化薪资轨迹
plt.figure(figsize=(10, 6))
sns.lineplot(x='career_year', y='salary', data=tim_duncan_data, marker='o', color='purple')
plt.title('Tim Duncan Salary Trajectory')
plt.xlabel('Career Year')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

# 找到player_id为'millspa01'的所有记录
player_data = merged[merged['player_id'] == 'millspa01']

# 绘制薪资轨迹
plt.figure(figsize=(10, 6))
sns.lineplot(x='career_year', y='salary', data=player_data, marker='o', color='blue')

# 设置图表标题和标签
plt.title('Salary Trajectory of Player millspa01')
plt.xlabel('Career Year')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

# 筛选出两位球员的数据
tim_duncan_data = merged[merged['player_id'] == 'duncati01']
millspa01_data = merged[merged['player_id'] == 'millspa01']

# 按 career_year 排序（保险起见）
tim_duncan_data = tim_duncan_data.sort_values('career_year')
millspa01_data = millspa01_data.sort_values('career_year')

# 可视化两位球员的薪资轨迹
plt.figure(figsize=(10, 6))

# 绘制Tim Duncan的薪资轨迹
sns.lineplot(x='career_year', y='salary', data=tim_duncan_data, marker='o', color='purple', label='Tim Duncan')

# 绘制Millspa01的薪资轨迹
sns.lineplot(x='career_year', y='salary', data=millspa01_data, marker='o', color='blue', label='Millspa01')

# 设置图表标题和标签
plt.title('Salary Trajectory of Tim Duncan and Millspa01')
plt.xlabel('Career Year')
plt.ylabel('Salary')
plt.legend()  # 显示图例
plt.grid(True)
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# 读取数据
df = pd.read_csv("salaries_1985to2018.csv")
players = pd.read_csv("players.csv")

# 清洗薪资数据
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df = df.dropna(subset=['salary'])

# 合并球员信息
merged = df.merge(players, left_on='player_id', right_on='_id', how='left')
merged = merged.sort_values(['player_id', 'season_start'])
merged['career_year'] = merged.groupby('player_id').cumcount() + 1

# ---- 身高英寸转换 ----
def convert_height(height_str):
    try:
        feet, inches = height_str.split('-')
        return int(feet) * 12 + int(inches)
    except:
        return None

merged['height_inch'] = merged['height'].apply(convert_height)

# ---- 体重数值提取 ----
merged['weight_num'] = merged['weight'].str.replace('lb', '', regex=False).astype(float)

# ---- 清洗 draft_pick 字段 ----
def clean_draft_pick(draft_pick):
    try:
        # 提取数字部分
        pick = ''.join(filter(str.isdigit, draft_pick))
        return int(pick) if pick else None
    except:
        return None

# 处理 draft_pick 字段
merged['draft_pick'] = merged['draft_pick'].apply(clean_draft_pick)

# 转换为数值的表现特征
perf_features = [
    'career_AST', 'career_FG%', 'career_FG3%', 'career_FT%', 'career_G',
    'career_PER', 'career_PTS', 'career_TRB'
]
for col in perf_features:
    merged[col] = pd.to_numeric(merged[col], errors='coerce')

# ---- 取每个球员最后三年 ----
last3 = merged.groupby('player_id').apply(
    lambda x: x.sort_values('career_year', ascending=False).head(3)
).reset_index(drop=True)

avg_salary = last3.groupby('player_id')['salary'].mean().reset_index(name='last5_avg_salary')

# ---- 表现 + 身高体重 + draft_pick 特征 ----
player_stats = merged.drop_duplicates('player_id')[['player_id'] + perf_features + ['height_inch', 'weight_num', 'draft_pick']]
data = avg_salary.merge(player_stats, on='player_id').dropna()

# ---- 归一化 身高 & 体重 ----
data['height_inch'] = (data['height_inch'] - data['height_inch'].min()) / data['height_inch'].max()
data['weight_num'] = (data['weight_num'] - data['weight_num'].min()) / data['weight_num'].max()

from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import scipy.cluster.hierarchy as sch

# 选择用于聚类的特征
features_for_clustering = [
    'career_AST', 'career_FG%', 'career_FG3%', 'career_FT%', 'career_G',
    'career_PER', 'career_PTS', 'career_TRB',
    'height_inch', 'weight_num', 'draft_pick'
]

# 去除缺失值（保险）
cluster_data = data[features_for_clustering].dropna()

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(cluster_data)

# 层次聚类计算 linkage matrix
linked = linkage(X_scaled, method='ward')

# 绘制树状图（dendrogram）
plt.figure(figsize=(12, 6))
dendrogram(linked, truncate_mode='level', p=5)  # p=5 表示只展示前5层
plt.title('Hierarchical Clustering Dendrogram (Truncated)')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.grid(True)
plt.show()

# 选定一个聚类数，比如分成4类
data['cluster'] = fcluster(linked, t=4, criterion='maxclust')

# 可视化聚类分布（以PER和salary为例）
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='career_PER', y='last5_avg_salary', hue='cluster', palette='viridis', s=80)
plt.title('Clusters by career_PER vs. last5_avg_salary')
plt.xlabel('Career PER')
plt.ylabel('Last 5-Year Average Salary')
plt.grid(True)
plt.legend(title='Cluster')
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
corr = data.drop(columns='player_id').corr()  # 计算相关系数矩阵

plt.figure(figsize=(10, 8))
sns.heatmap(corr[['last5_avg_salary']].sort_values('last5_avg_salary', ascending=False), 
            annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation with Last 3-Year Avg Salary")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
corr = data.drop(columns='player_id').corr()  # 计算相关系数矩阵

plt.figure(figsize=(10, 8))
sns.heatmap(corr[['last3_avg_salary']].sort_values('last3_avg_salary', ascending=False), 
            annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation with Last 3-Year Avg Salary")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# ---- 使用 RandomForestRegressor 分析特征重要性 ----
X = data.drop(columns=['player_id', 'last3_avg_salary'])
y = data['last3_avg_salary']

# 初始化并训练随机森林回归模型
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 获取特征重要性
feature_importances = model.feature_importances_

# 将特征和重要性配对，并排序
feature_importance_df = pd.DataFrame({
    'feature': X.columns,
    'importance': feature_importances
}).sort_values(by='importance', ascending=False)

# ---- 绘制条形图 ----
plt.figure(figsize=(10, 6))  # 调整图形的尺寸
ax = sns.barplot(x='importance', y='feature', data=feature_importance_df, palette='Blues_d')

# 获取 x 轴范围
x_min, x_max = ax.get_xlim()

# 在每条 bar 上显示数值
for i in range(len(feature_importance_df)):
    # 动态设置文本位置
    ax.text(feature_importance_df['importance'].iloc[i] + 0.002,  # x 坐标稍微偏移条形图的右侧
            i,  # y 坐标
            f'{feature_importance_df["importance"].iloc[i]:.4f}',  # 显示小数点后 4 位
            va='center',  # 垂直居中对齐
            color='black',  # 文字颜色
            fontsize=10,  # 字体大小
            bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3')  # 添加背景框
            )

plt.title('Feature Importance - Random Forest')
plt.xlabel('Importance')
plt.ylabel('Features')
plt.show()

# 打印重要性排名
print(feature_importance_df)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error

# 加载数据
df = pd.read_csv("salaries_1985to2018.csv")
players = pd.read_csv("players.csv")

# 清洗薪资数据
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df = df.dropna(subset=['salary'])

# 合并球员信息
merged = df.merge(players, left_on='player_id', right_on='_id', how='left')

# 类型转换
for col in ['career_PER', 'career_AST', 'career_FG%', 'career_FG3%', 'career_FT%',
            'career_G', 'career_PTS', 'career_TRB', 'career_WS', 'career_eFG%']:
    merged[col] = pd.to_numeric(merged[col], errors='coerce')

# 只保留有完整数据的记录
merged_clean = merged.dropna(subset=['career_PER', 'career_AST', 'career_FG%', 'career_FG3%',
                                     'career_FT%', 'career_G', 'career_PTS', 'career_TRB', 'salary'])

# 提取每个球员的生涯最高薪资
max_salary = merged_clean.groupby('player_id')['salary'].max().reset_index()
max_salary.columns = ['player_id', 'max_salary']

# 合并表现数据（去重）
player_features = merged_clean.drop_duplicates(subset='player_id')[[
    'player_id', 'position', 'career_AST', 'career_FG%', 'career_FG3%', 'career_FT%',
    'career_G', 'career_PER', 'career_PTS', 'career_TRB'
]]

# 合并数据
data = player_features.merge(max_salary, on='player_id')

# 编码 position
le = LabelEncoder()
data['position_encoded'] = le.fit_transform(data['position'])

# 构建训练数据
X = data[['career_AST', 'career_FG%', 'career_FG3%', 'career_FT%', 'career_G',
          'career_PER', 'career_PTS', 'career_TRB', 'position_encoded']]
y = data['max_salary']

# 划分训练测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# 建模
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 评估
y_pred = model.predict(X_test)
print("Test RMSE:", mean_squared_error(y_test, y_pred, squared=False))

# 特征重要性
feature_importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
sns.barplot(x=feature_importance, y=feature_importance.index)
plt.title("Feature Importance for Predicting Max Salary")
plt.show()


import pandas as pd
import numpy as np

# 读取数据
df = pd.read_csv("salaries_1985to2018.csv")
players = pd.read_csv("players.csv")

# 清洗薪资数据
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df = df.dropna(subset=['salary'])

# 合并球员信息
merged = df.merge(players, left_on='player_id', right_on='_id', how='left')
merged['career_PER'] = pd.to_numeric(merged['career_PER'], errors='coerce')
print(merged['career_PER'].isna().sum())

# 添加球龄字段（方便对齐生涯年份）
merged = merged.sort_values(['player_id', 'season_start'])
merged['career_year'] = merged.groupby('player_id').cumcount() + 1

# 过滤前N年（如前5年）用于建模
N = 30
trajectory_df = merged[merged['career_year'] <= N]

# 1. 统计出现频率最高的前10个 position
top_positions = trajectory_df['position'].value_counts().head(18).index.tolist()
print("Top 10 most common positions:")
print(trajectory_df['position'].value_counts())

# 2. 过滤数据，只保留这10种 position 的记录
trajectory_df = trajectory_df[trajectory_df['position'].isin(top_positions)]

import matplotlib.pyplot as plt
import seaborn as sns

# 平均轨迹（按位置）
avg_traj = trajectory_df.groupby(['position', 'career_year']).agg({
    'salary': 'mean',
    'career_PER': 'mean'
}).reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=avg_traj, x='career_year', y='salary', hue='position')
plt.title("Average Salary Trajectory by Position")
plt.xlabel("Career Year")
plt.ylabel("Salary")
plt.grid(True)
plt.legend(loc='upper left')

plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=avg_traj, x='career_year', y='career_PER', hue='position')
plt.title("Average career_PER Trajectory by Position")
plt.xlabel("Career Year")
plt.ylabel("career_PER")
plt.grid(True)
plt.legend(loc='upper left')

plt.show()

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("salaries_1985to2018.csv")
players = pd.read_csv("players.csv")

# 清洗薪资数据
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df = df.dropna(subset=['salary'])

# 合并球员信息
merged = df.merge(players, left_on='player_id', right_on='_id', how='left')

# 添加球员生涯年份字段（用于聚类）
merged = merged.sort_values(['player_id', 'season_start'])
merged['career_year'] = merged.groupby('player_id').cumcount() + 1

# pivot 出所有球员的 salary 序列，不限制职业年限
salary_seq = merged.pivot(index='player_id', columns='career_year', values='salary').fillna(0)

# 标准化
scaler = StandardScaler()
salary_scaled = scaler.fit_transform(salary_seq)

# 聚类
kmeans = KMeans(n_clusters=4, random_state=42)
labels = kmeans.fit_predict(salary_scaled)

# 添加聚类标签到 salary_seq
salary_seq['cluster'] = labels

# 可视化聚类结果（使用PCA进行降维）
pca = PCA(n_components=2)
salary_pca = pca.fit_transform(salary_scaled)

# 绘制聚类图
plt.figure(figsize=(8, 6))
plt.scatter(salary_pca[:, 0], salary_pca[:, 1], c=labels, cmap='Set2')
plt.title("Clustering of Player Salary Trajectories (All Career Years)")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.show()

avg_trajectories = salary_seq.groupby('cluster').mean()

plt.figure(figsize=(10, 6))
for cluster_id, row in avg_trajectories.iterrows():
    # 确保 X 轴范围与每个 cluster 的薪资年份匹配
    career_years = range(1, len(row) + 1)
    plt.plot(career_years, row.values, label=f'Cluster {cluster_id}')

plt.title("Average Salary Trajectory by Cluster (All Career Years)")
plt.xlabel("Career Year")
plt.ylabel("Standardized Salary")
plt.legend()
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 假设你已经加载了数据，并进行了聚类操作
# 将聚类标签添加到 salary_seq 中

# 先重置索引，将 'player_id' 从索引列恢复为数据列
salary_seq_reset = salary_seq.reset_index()

# 将聚类标签添加到 salary_seq
salary_seq_reset['cluster'] = kmeans.labels_  # 将聚类标签添加到 salary_seq_reset

# 现在将聚类标签合并回原始的 merged 数据
merged_with_cluster = merged.merge(salary_seq_reset[['player_id', 'cluster']], on='player_id', how='left')
merged_with_cluster = merged_with_cluster.drop(columns=['height'])

# 去除百分号并转换为数值（例如 career_FG% 列）
def clean_percentage_column(df, column_name):
    df[column_name] = df[column_name].replace({'%': '', ',': ''}, regex=True)  # 清除百分号和逗号
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')  # 转换为数值类型

# 对所有相关列进行清理
percentage_columns = ['career_FG%', 'career_FG3%', 'career_FT%', 'career_eFG%']
for col in percentage_columns:
    clean_percentage_column(merged_with_cluster, col)

# 处理其他数值列，确保它们是数值类型
numerical_columns = ['career_PER', 'career_TRB', 'career_WS']
for col in numerical_columns:
    merged_with_cluster[col] = pd.to_numeric(merged_with_cluster[col], errors='coerce')

# 检查清理后的数据


def clean_weight_column(df, column_name):
    df[column_name] = df[column_name].str.replace('lb', '').str.strip()
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')

# 清理 weight 列
clean_weight_column(merged_with_cluster, 'weight')

# 检查清理后的 weight 列


# 对每个聚类分析球员的其他属性
cluster_analysis = merged_with_cluster.groupby('cluster').agg({
    'position': lambda x: x.mode()[0],  # 最常见的位置
    'career_AST': 'mean', 
    'career_FG%': 'mean', 
    'career_FG3%': 'mean', 
    'career_FT%': 'mean', 
    'career_G': 'mean', 
    'career_PER': 'mean',  
    'career_PTS': 'mean', 
    'career_TRB': 'mean',  
    'weight': 'mean', 
}).reset_index()

print("cluster_analysis")

# 显示聚类分析结果
print(cluster_analysis)

# 可视化每个聚类中不同位置球员的分布
position_dist = merged_with_cluster.groupby(['cluster', 'position']).size().unstack().fillna(0)

plt.figure(figsize=(12, 6))
position_dist.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title("Position Distribution by Salary Cluster")
plt.xlabel("Cluster")
plt.ylabel("Number of Players")
plt.legend(title="Position")
plt.show()


# 构建序列输入（X）和目标（y）：前5年薪资 → 第6年薪资
full_salary = merged.pivot(index='player_id', columns='career_year', values='salary')
valid_players = full_salary.dropna(subset=[1, 2, 3, 4, 5, 6])  # 至少打到第6年

X_seq = valid_players[[1, 2, 3, 4, 5]].values
y = valid_players[6].values

# 转换为 Tensor
import torch
from torch.utils.data import Dataset, DataLoader

class SalaryDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32).unsqueeze(-1)  # (B, T, 1)
        self.y = torch.tensor(y, dtype=torch.float32)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

dataset = SalaryDataset(X_seq, y)
loader = DataLoader(dataset, batch_size=32, shuffle=True)

import torch.nn as nn

class SalaryTransformer(nn.Module):
    def __init__(self, d_model=32, nhead=4, num_layers=2):
        super().__init__()
        self.embedding = nn.Linear(1, d_model)
        encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead, batch_first=True)
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.regressor = nn.Sequential(
            nn.Flatten(),
            nn.Linear(d_model * 5, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        x = self.embedding(x)
        x = self.encoder(x)
        out = self.regressor(x)
        return out.squeeze()


import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from torch.optim.lr_scheduler import ReduceLROnPlateau

# 数据准备
full_salary = merged.pivot(index='player_id', columns='career_year', values='salary')
valid_players = full_salary.dropna(subset=[1, 2, 3, 4, 5, 6])  # 至少打到第6年

X_seq = valid_players[[1, 2, 3, 4, 5]].values
y = valid_players[6].values

# 标准化薪资数据
scaler = StandardScaler()
X_seq_scaled = scaler.fit_transform(X_seq)

# 定义 Dataset 类
class SalaryDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32).unsqueeze(-1)  # (B, T, 1)
        self.y = torch.tensor(y, dtype=torch.float32)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# 划分训练集和验证集
X_train, X_val, y_train, y_val = train_test_split(X_seq_scaled, y, test_size=0.2, random_state=42)

train_dataset = SalaryDataset(X_train, y_train)
val_dataset = SalaryDataset(X_val, y_val)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# 模型定义
class SalaryTransformer(nn.Module):
    def __init__(self, d_model=32, nhead=4, num_layers=2, dropout=0.1):
        super().__init__()
        self.embedding = nn.Linear(1, d_model)
        encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead, batch_first=True, dropout=dropout)
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.regressor = nn.Sequential(
            nn.Flatten(),
            nn.Linear(d_model * 5, 64),
            nn.ReLU(),
            nn.Dropout(0.5),  # 添加 Dropout 防止过拟合
            nn.Linear(64, 1)
        )

    def forward(self, x):
        x = self.embedding(x)
        x = self.encoder(x)
        out = self.regressor(x)
        return out.squeeze()

# 实例化模型、优化器和损失函数
model = SalaryTransformer()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

# 学习率调度器
scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=2)

# 训练和验证循环
for epoch in range(20):
    model.train()  # 训练模式
    total_loss = 0
    for X_batch, y_batch in train_loader:
        pred = model(X_batch)
        loss = loss_fn(pred, y_batch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    # 在每个 epoch 结束时评估模型
    model.eval()  # 验证模式
    val_loss = 0
    with torch.no_grad():
        for X_batch, y_batch in val_loader:
            pred = model(X_batch)
            val_loss += loss_fn(pred, y_batch).item()

    # 学习率调度
    scheduler.step(val_loss)

    print(f"Epoch {epoch+1}, Train Loss: {total_loss:.4f}, Validation Loss: {val_loss:.4f}")

# 训练结束后，模型可以进行预测
