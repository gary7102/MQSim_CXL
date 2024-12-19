import sys

def modify_total_requests(config_file_path, trace_file_path):
    try:
        # 計算 trace 文件的行數
        with open(trace_file_path, 'r') as trace_file:
            total_lines = sum(1 for _ in trace_file)

        # 修改 config.txt 文件中的 Total_number_of_requests
        with open(config_file_path, 'r') as config_file:
            lines = config_file.readlines()

        updated_lines = []
        for line in lines:
            if line.startswith("Total_number_of_requests"):
                updated_lines.append(f"Total_number_of_requests {total_lines}\n")
            else:
                updated_lines.append(line)

        # 寫回更新後的 config.txt
        with open(config_file_path, 'w') as config_file:
            config_file.writelines(updated_lines)

        print(f"Successfully updated 'Total_number_of_requests' to {total_lines} in {config_file_path}.")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # 檢查是否提供必要參數
    if len(sys.argv) != 3:
        print("Usage: python modify_requests.py <config_file_path> <trace_file_path>")
        sys.exit(1)

    # 接收參數
    config_file_path = sys.argv[1]
    trace_file_path = sys.argv[2]

    # 修改配置
    modify_total_requests(config_file_path, trace_file_path)

