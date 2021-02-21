# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:49:19 2021

@author: Oliver
"""

from os import listdir
from PIL import Image
 
 
def pinjie():
    # 获取当前文件夹中所有JPG图像
    im_list = [Image.open(fn) for fn in listdir() if fn.endswith('.jpg')]
    # 图片转化为相同的尺寸
    ims = []
    for i in im_list:
        new_img = i.resize((82, 82), Image.BILINEAR)
        ims.append(new_img)
    # 单幅图像尺寸
    width, height = ims[0].size
    # 创建空白长图
    result = Image.new(ims[0].mode, (width, height * len(ims)))
    # 拼接图片
    for i, im in enumerate(ims):
        result.paste(im, box=(0, i * height))
    # 保存图片
    result.save('res1.jpg')
 
 
if __name__ == '__main__':
    pinjie()