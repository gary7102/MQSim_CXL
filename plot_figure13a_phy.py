import numpy as np
import matplotlib.pyplot as plt

# 模擬數據
categories = ['BERT', 'Radiosity', 'XZ', 'YCSB']
methods = ['NP', 'NL', 'FD', 'BO', 'LP']
data = [
    [86.79,64.52 ,71.71 ,75.65],  # NP
    [83.64,84.03 ,63.84 ,72.53],  # NL
    [85.93,83.66 ,67.36 ,74.56],  # FD
    [86.42,91.14 ,71.63 ,74.23],  # BO
    [85.03,88.41 ,66.82 ,73.25]   # LP
]

# 設置條形圖的位置
bar_width = 0.15
x = np.arange(len(categories))

# 繪製條形圖
fig, ax = plt.subplots(figsize=(8, 4))
for i, method in enumerate(methods):
    ax.bar(x + i * bar_width, data[i], width=bar_width, label=method)

# 設置標籤與刻度
ax.set_xlabel('Workloads', fontsize=12)
ax.set_ylabel('Percentage of sub-µs requests (%)', fontsize=12)
ax.set_title('Percentage of sub-µs requests', fontsize=14)
ax.set_xticks(x + bar_width * (len(methods) - 1) / 2)
ax.set_xticklabels(categories, fontsize=10)
ax.legend(title='Methods', fontsize=10, title_fontsize=12, loc='upper center', ncol=len(methods), bbox_to_anchor=(0.5, 1.15))

# 添加網格線
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 調整布局
plt.tight_layout()
plt.savefig("./figure13a/prefetcher_phy.png")
# 顯示圖表
#plt.show()

