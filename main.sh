#!/bin/bash

# 定義目標路徑
TARGET_DIR="./trace_files"

# 外層迴圈：讀取目錄中的所有檔案
for file in "$TARGET_DIR"/*
do
    # 提取檔案名稱（不含路徑）
    file_name=$(basename "$file")
    file_name_no_ext="${file_name%.*}"
    
    # 輸出當前檔案名稱
    echo "Processing file: $file_name"
    echo "Processing file: $file_name_no_ext"


    # 在這裡執行與檔案相關的操作
    python3 set_tracefile.py "../trace_files/$file_name"

    bash simulate_trace_file.sh $file_name_no_ext	

done

echo "All files processed!"

