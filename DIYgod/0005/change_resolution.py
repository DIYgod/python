# -*- coding: utf-8 -*-
# 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

from PIL import Image

def change_resolution(picPath, reslution):
    img = Image.open(picPath)
    x, y = img.size
    print x, y
    changex = float(x) / reslution[0]
    changey = float(y) / reslution[1]

    # 判断分辨率是否满足
    if changex > 1 or changey > 1:
        change = changex if changex > changey else changey
        print change
        print int(reslution[0] / change), int(reslution[1] / change)
        img.resize((int(x / change), int(y / change))).save('result.jpg')

if __name__ == '__main__':
    change_resolution('pictest.jpg', (1136, 640))
