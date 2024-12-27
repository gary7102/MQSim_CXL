import matplotlib.pyplot as plt

# 模擬數據
set_associativity = [2, 4, 16]  # 原始 X 軸數據
fifo =  [68.77, 68.87,69.08]            # FIFO 策略的數據
rand =  [68.49, 68.65,68.74]            # Rand 策略的數據
lru =   [69.52, 70.21,70.77]             # LRU 策略的數據
cflru = [69.52, 72.04,74.23]           # CFLRU 策略的數據

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
plt.title("ycsb_f_p")
plt.xlabel("Set Associativity")
plt.ylabel("Percentage of sub-µs requests (%)")

# 添加圖例
plt.legend()

# 添加網格線
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("./figure11/ycsb_f_p.png")
# 顯示圖表
#plt.tight_layout()
#plt.show()

