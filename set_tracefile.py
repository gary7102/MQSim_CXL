import sys
import xml.etree.ElementTree as ET

def update_file_path(new_file_path):
    # XML 文件路徑，寫死在程式中
    xml_file_path = "./MQSim_CXL_Linux/workload.xml"

    try:
        # 解析 XML 文件
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # 尋找 File_Path 標籤
        for element in root.iter('File_Path'):
            element.text = new_file_path

        # 將修改後的 XML 文件儲存回去
        tree.write(xml_file_path, encoding="us-ascii", xml_declaration=True)
        print(f"Successfully updated File_Path to: {new_file_path}")

    except FileNotFoundError:
        print(f"Error: The file '{xml_file_path}' was not found.")
    except ET.ParseError:
        print(f"Error: Failed to parse the XML file '{xml_file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_file_path.py <new_file_path>")
        sys.exit(1)

    new_file_path = sys.argv[1]

    # 呼叫函式修改 File_Path
    update_file_path(new_file_path)

