import numpy as np
import matplotlib.pyplot as plt

# 定義數據
categories = ['BERT', 'Radiosity', 'XZ', 'YCSB']  # 移除了 'Page Rank'
methods = ['NL', 'FD', 'BO', 'LP']
metrics = ['Accuracy', 'Coverage', 'Lateness', 'Pollution']

# 模擬數據，每個負載對應每個方法的數據
data = {
    "Accuracy": {
        "BERT": [25.9798,30.4686 , 21.4187,26.8531],
        "Radiosity": [60.2647,57.6004,80.1948, 84.6864],
        "XZ": [24.7836,15.668, 47.8713 , 29.2561],
        "YCSB": [38.033,37.5894 ,27.8846, 34.322],
    },
    "Coverage": {
        "BERT": [18.8504,11.946, 22.1703, 30.4408],
        "Radiosity": [60.0087,59.6424, 85.7311, 77.834],
        "XZ": [6.84791,4.14778,4.03277,5.92109],
        "YCSB": [22.4402,12.198 , 18.3042, 20.7481],
    },
    "Lateness": {
        "BERT": [27.6344,23.2615 , 24.4169, 32.9132],
        "Radiosity": [80.692,56.6377 ,85.3395, 90.8654],
        "XZ": [57.1932,35.2943,82.4427,72.674],
        "YCSB": [18.2683,25.93 ,2.97816, 25.8879],
    },
    "Pollution": {
        "BERT": [71.397,43.5489,52.4833, 73.1976],
        "Radiosity": [34.391,34.8927, 30.6471,33.3807],
        "XZ":[52.4532,35.7541,1.34095,38.0399],
        "YCSB": [77.3439,48.1958 , 22.5671, 60.714],
    },
}

# 設置圖表參數
bar_width = 0.2
x = np.arange(len(categories) * len(methods))  # 每組負載的中心位置
offsets = np.linspace(-0.3, 0.3, len(metrics))  # 為不同參數設置偏移量

# 創建圖表
fig, ax = plt.subplots(figsize=(12, 6))

# 定義顏色和填充樣式
colors = ['gray', 'white', 'black', 'lightgray']
hatches = ['/', '\\', '-', 'o']

# 繪製柱形圖
for i, (metric, offset) in enumerate(zip(metrics, offsets)):
    y_values = []
    for category in categories:
        # 為每個方法取對應的數據，Lateness 和 Pollution 設為負值
        values = [
            data[metric][category][methods.index(method)]
            if metric in ['Accuracy', 'Coverage'] else -data[metric][category][methods.index(method)]
            for method in methods
        ]
        y_values.extend(values)
    ax.bar(x + offset, y_values, bar_width, label=metric,
           color=colors[i % len(colors)], edgecolor='black', hatch=hatches[i % len(hatches)])

# 設置 X 軸標籤
grouped_labels = []
for category in categories:
    for method in methods:
        grouped_labels.append(f"{method}\n{category}")  # 顯示 method 與 category 的下標

ax.set_xticks(x)
ax.set_xticklabels(grouped_labels, fontsize=9, rotation=0)

# 添加分隔線
for i in range(1, len(categories)):
    ax.axvline(x=i * len(methods) - 0.5, color='black', linestyle='--', linewidth=1)

# 設置縱軸刻度
ax.set_yticks([100, 50, 0, -50, -100])
ax.set_ylim(-100, 100)
ax.set_yticklabels(['100', '50', '0', '50', '100'])  # 反轉下半部顯示

# 設置標籤和標題
ax.set_ylabel('Prefetcher Metrics', fontsize=12)
ax.set_title('Accuracy, Coverage, Lateness, and Pollution metrics for the prefetchers', fontsize=14)

# 添加圖例
ax.legend(title="Metrics", loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4)

# 添加網格線
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 調整布局
plt.tight_layout()

# 顯示圖表
#plt.show()
plt.savefig("./physical.png")
