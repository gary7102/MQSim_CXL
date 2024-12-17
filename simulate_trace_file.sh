#!/bin/bash

SOURCE_PATH="./MQSim_CXL_Linux"        # 原始檔案目錄


# 外層迴圈範圍：i 從 1 到 3
for i in "LRU" "FIFO" "Random" "CFLRU"
do
	python3 modify_policy.py ${i}
    # 內層迴圈範圍：j 從 1 到 5
    for j in 2 4 16
    do
    
	
	python3 modify_setAsso.py ${j}
	
	cd ./MQSim_CXL_Linux
	make
	echo "" | ./MQSim -i ssdconfig.xml -w workload.xml
	
	cd ..
	
        # 根據 i 和 j 設定 RESULT_FOLDER_NAME
        RESULT_FOLDER_NAME="${i}_Aso${j}"
	DEST_PATH="./Results/$1/$RESULT_FOLDER_NAME" # 新資料夾完整路徑

	# 創建目標資料夾
	mkdir -p "$DEST_PATH"

	# 複製 Results 資料夾
	cp -r "$SOURCE_PATH/Results" "$DEST_PATH/Results"

	# 複製 config.txt, ssdconfig.xml, workload.xml
	cp "$SOURCE_PATH/config.txt" "$DEST_PATH"
	cp "$SOURCE_PATH/ssdconfig.xml" "$DEST_PATH"
	cp "$SOURCE_PATH/workload.xml" "$DEST_PATH"

	# 輸出完成訊息
	echo "Files and folders successfully copied to $DEST_PATH"
	


    done
done

echo "All loops completed!"

