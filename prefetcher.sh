#!/bin/bash

# 定義目標路徑
TARGET_DIR="./trace_files"
SOURCE_PATH="./MQSim_CXL_Linux"        # 原始檔案目錄

# 外層迴圈：讀取目錄中的所有檔案
for file in "$TARGET_DIR"/*
do
    for prefetcher in "No" "Tagged" "Best-offset" "Leap" "Feedback_direct"
    do
    # 提取檔案名稱（不含路徑）
    file_name=$(basename "$file")
    file_name_no_ext="${file_name%.*}"

    # 輸出當前檔案名稱
    echo "Processing file: $file_name"
    echo "Processing file: $file_name_no_ext"


    
    # 在這裡執行與檔案相關的操作
    python3 modify_prefetcher.py $prefetcher
    python3 set_tracefile.py "../trace_files/$file_name"
    python3 modify_req.py "./MQSim_CXL_Linux/config.txt" "./trace_files/$file_name" 
    cd ./MQSim_CXL_Linux
    make
    echo "" | ./MQSim -i ssdconfig.xml -w workload.xml

    cd ..

    # 根據 i 和 j 設定 RESULT_FOLDER_NAME
    RESULT_FOLDER_NAME=$prefetcher
    DEST_PATH="./Results_prefetcher/$file_name_no_ext/$RESULT_FOLDER_NAME" # 新資料夾完整路徑

    # 創建目標資料夾
    mkdir -p "$DEST_PATH"

    # 複製 Results 資料夾
    cp -r "$SOURCE_PATH/Results" "$DEST_PATH"

    # 複製 config.txt, ssdconfig.xml, workload.xml
    cp "$SOURCE_PATH/config.txt" "$DEST_PATH"
    cp "$SOURCE_PATH/ssdconfig.xml" "$DEST_PATH"
    cp "$SOURCE_PATH/workload.xml" "$DEST_PATH"

    # 輸出完成訊息
    echo "Files and folders successfully copied from "$SOURCE_PATH/Results" to $DEST_PATH"
    


    done
done

echo "All files processed!"

