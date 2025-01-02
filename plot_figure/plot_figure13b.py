import matplotlib.pyplot as plt
import numpy as np

# 手動輸入比例數據（百分比）
data = {
    'BERT': [[83.27,13.10,3.63], [88.99,8.02,3], [87.79,8.92,3.29], [91.69,5.54,2.77],[88.65,8.34,3.01]],
    'Radiosity': [[64.43,32.32,3.25], [94.75,4.09,1.16], [96.93,2.21,0.86], [96.91,2.28,0.81], [90.56,7.96,1.48]],
    'XZ': [[72.2,4.58,23.22], [70.83,3.92,25.25], [70.62,3.91,25.47], [73.39,3.31,23.3], [72.05,3.78,24.17]],
    'YCSB': [[70.70,9.08,20.22], [68.23,9.48,22.29], [69.15,9.64,21.21], [69.23,8.93,21.84], [69.63,8.91,21.46]]
}



categories = list(data.keys())
strategies = ['NP', 'NL', 'FD', 'BO', 'LP']

x = np.arange(len(categories))  # Categories 的索引
bar_width = 0.15  # 每個策略欄的寬度
bar_spacing = 0.1  # 每五個柱狀圖間的額外間隔
group_spacing = 0.5  # 每組之間的額外間隔

# 顏色與斜線樣式
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
hatches = ['//', '\\\\', 'xx']

fig, ax = plt.subplots(figsize=(12, 6))

# 紀錄柱狀圖位置
bar_positions = []

# 畫多組柱狀圖
for j, category in enumerate(categories):
    group_start = j * (len(strategies) * (bar_width + bar_spacing) + group_spacing)
    for i, strategy in enumerate(strategies):
        cache_hit, hit_under_miss, cache_miss = data[category][i]
        x_pos = group_start + i * (bar_width + bar_spacing)  # 計算每個柱狀圖的位置
        bar_positions.append(x_pos)
        ax.bar(x_pos, cache_hit, width=bar_width, 
               label='Cache Hit' if i == 0 and j == 0 else "", color=colors[0], hatch=hatches[0])
        ax.bar(x_pos, hit_under_miss, width=bar_width, 
               bottom=cache_hit, label='Hit-under-miss' if i == 0 and j == 0 else "", 
               color=colors[1], hatch=hatches[1])
        ax.bar(x_pos, cache_miss, width=bar_width, 
               bottom=cache_hit + hit_under_miss, label='Cache Miss' if i == 0 and j == 0 else "", 
               color=colors[2], hatch=hatches[2], edgecolor='black')

# 設置 X 軸的下標
xticks_positions = []
xticks_labels = []
for j, category in enumerate(categories):
    for i, strategy in enumerate(strategies):
        group_start = j * (len(strategies) * (bar_width + bar_spacing) + group_spacing)
        x_pos = group_start + i * (bar_width + bar_spacing)
        xticks_positions.append(x_pos)
        xticks_labels.append(strategy)

# 設置群組名稱
group_positions = [
    j * (len(strategies) * (bar_width + bar_spacing) + group_spacing) + 
    (len(strategies) - 1) * (bar_width + bar_spacing) / 2
    for j in range(len(categories))
]
ax.set_xticks(group_positions)
ax.set_xticklabels(categories, fontsize=12)

# 顯示每組對應的策略名稱
for j, category in enumerate(categories):
    group_start = j * (len(strategies) * (bar_width + bar_spacing) + group_spacing)
    for i, strategy in enumerate(strategies):
        x_pos = group_start + i * (bar_width + bar_spacing)
        ax.text(x_pos, -10, strategy, ha='center', fontsize=10, rotation=45)

# 標題和坐標標籤
ax.set_title("Cache Performance Metrics", fontsize=16)
ax.set_xlabel("Category", fontsize=12)
ax.set_ylabel("Rate (%)", fontsize=12)
ax.set_ylim(0, 110)

# 添加圖例（限制三個條目）
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:3], labels[:3], loc='upper right')

# 添加分隔線
for j in range(1, len(categories)):
    sep_pos = j * (len(strategies) * (bar_width + bar_spacing) + group_spacing) - group_spacing / 2
    ax.axvline(sep_pos, color='black', linestyle='--', linewidth=0.8)

#plt.savefig("./figure13b/vir.png")

