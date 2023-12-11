import os
import shutil


files = os.listdir('./Leetcode')
for file in files:
    file_path = './Leetcode/' + file
    if os.path.isfile(file_path) and file_path.split('.')[-1] == 'py':
        new_file_name = 'Leetcode_' + os.path.basename(file_path)
        os.rename(file_path, './Leetcode/' + new_file_name)


