# 作業拍照快速改檔名

### [Step0]

- 載code

### [Step1]

- 去E3載學生資料的json檔案
    - 成員 > 選擇所有____個使用者
    
    ![image](https://github.com/zenchieh/File_Rename/assets/64319084/b71fc513-84e7-4a5e-9c63-9be97ab60654)

    

- 創建一個資料夾，把JSON檔案跟兩個python code放進去
    
![image](https://github.com/zenchieh/File_Rename/assets/64319084/fc6bbe93-57e8-4bb3-8c34-09090cdc6fe9)
    

### [Step2] - (TODO : 寫成.bat一鍵完成)

- 開powershell or VScode or 其他可以跑python的環境
- 下指令
    - $ **python createStudentDir.py**
    - 會產生所有學生的資料夾
        
        ![image](https://github.com/zenchieh/File_Rename/assets/64319084/5a2b5b07-1545-4ee7-acc3-118297fec356)
        ![image](https://github.com/zenchieh/File_Rename/assets/64319084/01684ed7-72cd-45a6-a7ba-108e1244eec1)

        

### [Step3]

- 拍照，放到相對應的資料夾內

### [Step4]

- 下指令
    - $ **python dirRename.py**
    
    ![image](https://github.com/zenchieh/File_Rename/assets/64319084/8f62ab9f-5066-4a3f-a387-fa069bc4a251)
    
    - 會把資料夾內的照片改成 學號_姓名_1、學號_姓名_2 …
    - 並把它移出來 & 刪掉資料夾，並包成一個zip檔案放在該資料夾
    ![image](https://github.com/zenchieh/File_Rename/assets/64319084/1a3b19e5-f37a-4eff-99d1-5fcfdd516ff7)