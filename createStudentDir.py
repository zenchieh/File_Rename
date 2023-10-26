import json
import os

'''
學校給的JSON檔案格式如下
所以要抓firstname & idnumber
{
    "firstname": "薛懿倫",
    "lastname": "電機系 \/ UEE",
    "idnumber": "0610702",
    "department": "電機系 \/ UEE",
    "institution": "",
    "city": ""
}

'''

# 要放資料夾的路徑
student_dir_path = "C:\\Users\\zen\\Desktop\\test"
# JSON文件的路徑
json_file_path = "C:\\Users\\zen\\Desktop\\test\\courseid_49244_participants.json"

# 讀Json file
with open('C:\\Users\\zen\\Desktop\\test\\courseid_49244_participants.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 遍歷每個學生資料
for student in data[0]:
    firstname = student["firstname"]
    idnumber = student["idnumber"]

    # 創建學生資料夾
    folder_name = f"{idnumber}_{firstname}"
    os.makedirs(folder_name, exist_ok=True)

print(f"資料夾已創建: {os.listdir()}")







