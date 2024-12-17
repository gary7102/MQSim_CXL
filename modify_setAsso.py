import sys

def modify_config_file(file_path, cache_placement_value):
    try:
        # 讀取 config.txt 文件
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # 修改 Cache_placement 行
        updated_lines = []
        for line in lines:
            if line.startswith("Cache_placement"):
                updated_lines.append(f"Cache_placement {cache_placement_value}\n")
            else:
                updated_lines.append(line)
        
        # 寫回更新後的內容
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)
        
        print(f"Successfully updated 'Cache_placement' to {cache_placement_value} in {file_path}.")
    
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # 檢查是否提供參數
    if len(sys.argv) != 2:
        print("Usage: python modify_config.py <new_cache_placement_value>")
        sys.exit(1)

    # 接收參數
    try:
        new_cache_placement = int(sys.argv[1])  # 將傳入的參數轉為整數
        config_file_path = "./MQSim_CXL_Linux/config.txt"  # 設定檔案路徑
        
        # 呼叫修改函數
        modify_config_file(config_file_path, new_cache_placement)
    except ValueError:
        print("Error: Please provide a valid integer value for 'Cache_placement'.")

