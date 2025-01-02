import numpy as np
import matplotlib.pyplot as plt

# 模擬數據
categories = ['BERT', 'Radiosity', 'XZ', 'YCSB']
methods = ['NP', 'NL', 'FD', 'BO', 'LP']
data = [
    [83.43 ,64.72 ,72.26 ,71.99],  # NP
    [89.05 ,94.76 ,70.85 ,69.2],  # NL
    [87.86 ,96.93 ,70.69 ,70.16],  # FD
    [91.73 ,96.91 ,73.45 ,70.41],  # BO
    [88.74 ,90.6  ,72.07 ,70.71]   # LP
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
plt.savefig("./figure13a/prefetcher_vir.png")
# 顯示圖表
#plt.show()

