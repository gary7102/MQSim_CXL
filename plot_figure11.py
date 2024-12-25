import matplotlib.pyplot as plt

# 模擬數據
set_associativity = [2, 4, 16]  # 原始 X 軸數據
fifo = [60, 70, 80]            # FIFO 策略的數據
rand = [65, 75, 85]            # Rand 策略的數據
lru = [58, 72, 78]             # LRU 策略的數據
cflru = [62, 77, 90]           # CFLRU 策略的數據

# 創建均勻的 X 軸數據
x_positions = range(len(set_associativity))  # 均勻間距 [0, 1, 2]

# 創建圖表
plt.figure(figsize=(6, 4))

# 繪製不同策略的數據線
plt.plot(x_positions, fifo, label="FIFO", marker='x', linestyle='--')
plt.plot(x_positions, rand, label="Rand", marker='o', linestyle='-')
plt.plot(x_positions, lru, label="LRU", marker='v', linestyle='-.')
plt.plot(x_positions, cflru, label="CFLRU", marker='s', linestyle=':')

# 設置 X 軸刻度為等寬，並顯示原始數據值
plt.xticks(x_positions, set_associativity)

# 添加標題和軸標籤
plt.title("Sub-µs Request (%) - BERT")
plt.xlabel("Set Associativity")
plt.ylabel("Sub-µs Request (%)")

# 添加圖例
plt.legend()

# 添加網格線
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("Figure11.png")
# 顯示圖表
#plt.tight_layout()
#plt.show()

