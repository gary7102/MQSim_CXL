import sys

def modify_prefetcher(file_path, prefetcher_value):
    # 可用選項列表
    valid_options = ["No", "Tagged", "Best-offset", "Leap", "Feedback_direct"]

    # 檢查傳入的值是否有效
    if prefetcher_value not in valid_options:
        print(f"Error: Invalid Prefetcher value '{prefetcher_value}'.")
        print(f"The available options are: {', '.join(valid_options)}")
        sys.exit(1)

    try:
        # 讀取 config.txt 文件
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # 修改 Prefetcher 行
        updated_lines = []
        for line in lines:
            if line.startswith("Prefetcher"):
                updated_lines.append(f"Prefetcher {prefetcher_value}\n")
            else:
                updated_lines.append(line)
        
        # 寫回更新後的內容
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)
        
        print(f"Successfully updated 'Prefetcher' to {prefetcher_value} in {file_path}.")

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # 檢查是否提供參數
    if len(sys.argv) != 2:
        print("Usage: python modify_prefetcher.py <new_prefetcher_value>")
        sys.exit(1)

    # 接收參數
    prefetcher_value = sys.argv[1]  # 接收傳入的 Prefetcher 值
    config_file_path = "./MQSim_CXL_Linux/config.txt"  # 設定檔案路徑

    # 呼叫修改函數
    modify_prefetcher(config_file_path, prefetcher_value)

