'''
python verion = 3.7
'''
import os

'''先檢查目標資料夾是否存在
    →是，結束
    →不是，建立資料夾後結束'''

foldername = 'test0610' # 這裡放入資料夾名稱

dir_base = os.getcwd() # 這裡放本py檔所在位置
print(f'本py檔的路徑為: {dir_base}')

dir = os.path.join(dir_base, foldername) # 這裡放資料夾路徑
print(f'目標資料夾路徑為: {dir}')

if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print('資料夾已存在')