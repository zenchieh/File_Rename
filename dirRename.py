import os
import shutil
import zipfile

directory_path = 'C:\\Users\\zen\\Desktop\\test'


#  ** 注意 : 資料夾名稱須為 學號_姓名 EX: 312513000_王曉明 **


# 開始遍歷路徑中子資料夾內的檔案
for root, dirs, files in os.walk(directory_path):
    # 遍歷子資料夾
    for subdirectory in dirs:
        # 拆開學號和姓名
        student_info = subdirectory.split("_")
        if len(student_info) == 2:
            student_id, student_name = student_info

            new_filename_prefix = f"{student_id}_{student_name}"

            # 拿到子資料夾下的所有檔案
            file_list = os.listdir(os.path.join(root, subdirectory))

            # 遍歷並重新命名文件
            for i, filename in enumerate(file_list, start=1):

                file_extension = os.path.splitext(filename)[-1]
                new_filename = f"{new_filename_prefix}_{i}{file_extension}"

                old_filepath = os.path.join(root, subdirectory, filename)
                new_filepath = os.path.join(root, subdirectory, new_filename)
                os.rename(old_filepath, new_filepath)

                print(f"Renamed: {old_filepath} to {new_filepath}")

# 將每個子資料夾檔案往外移一層 & 把資料夾刪除
for root, dirs, files in os.walk(directory_path, topdown=False):
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)

        for file_name in os.listdir(dir_path):
            src = os.path.join(dir_path, file_name)
            dst = os.path.join(root, file_name)
            shutil.move(src, dst)

        os.rmdir(dir_path)

# 把json檔案和py檔刪除
for root, dirs, files in os.walk(directory_path):
    for file_name in files:
        if file_name.endswith(('.json', '.py')):
            file_path = os.path.join(root, file_name)
            os.remove(file_path)

# 壓縮輸出zip檔案
'''
# TODO : the code below do not compression size, need to fix

folder_name = os.path.basename(directory_path)
zip_filename = f"{folder_name}.zip"
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            arcname = os.path.relpath(file_path, directory_path)
            zipf.write(file_path, arcname)

shutil.move(zip_filename, os.path.join(directory_path, zip_filename))
'''
