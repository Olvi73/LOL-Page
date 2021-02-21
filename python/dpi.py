from PIL import Image
import os
import shutil

x=82
y=82

now_path = os.getcwd() + '\\' + 'img'
# new_path = os.mkdir(now_path + '\\' + 'new_img')
new_dir = os.getcwd() + '\\' + 'new_img'

# 修改图片大小
def smaller_img(x, y, path):
    path = str(path)
    old_img = Image.open(path)
    img_deal = old_img.resize((x, y), Image.ANTIALIAS) 
    img_deal = img_deal.convert('RGB') 
    img_deal.save('switch_' + file_name)
# 遍历文件夹下的文件，并判断是否是JPG文件
for file_name in os.listdir(now_path):
    files_path = now_path + '\\' + file_name
    if 'jpg' in files_path:
        smaller_img(x, y, files_path)
        # 遍历文件来判断是否是转换后的jpg文件
        for move_name in os.listdir(os.getcwd()):
            move_path = os.getcwd() + '\\' + move_name
            if 'switch' in move_path:
                shutil.move(move_path,new_dir)
            else:
                 print(move_path, '无须移动')
        print(file_name, 'switch success')
    else:
        print(file_name, 'is not img')
