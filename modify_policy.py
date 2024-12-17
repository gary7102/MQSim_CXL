import sys

def modify_cache_policy(file_path, cache_policy_value):
    try:
        # 讀取 config.txt 文件
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # 修改 Cache_policy 行
        updated_lines = []
        for line in lines:
            if line.startswith("Cache_policy"):
                updated_lines.append(f"Cache_policy {cache_policy_value}\n")
            else:
                updated_lines.append(line)
        
        # 寫回更新後的內容
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)
        
        print(f"Successfully updated 'Cache_policy' to {cache_policy_value} in {file_path}.")
    
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # 檢查是否提供參數
    if len(sys.argv) != 2:
        print("Usage: python modify_cache_policy.py <new_cache_policy_value>")
        sys.exit(1)

    # 接收參數
    cache_policy = sys.argv[1]  # 接收傳入的 Cache_policy 值
    config_file_path = "./MQSim_CXL_Linux/config.txt"  # 設定檔案路徑

    # 呼叫修改函數
    modify_cache_policy(config_file_path, cache_policy)

