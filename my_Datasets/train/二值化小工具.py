import cv2
import os
import time
import numpy as np

path = "./"  # 原图所在文件夹
for root, dirs, files in os.walk(path):
      for dir in dirs:
        print(dir)
        dir_path = os.path.join(root, dir)
        for sub_root, sub_dirs, sub_files in os.walk(dir_path):
          for img in sub_files:
            _path = os.path.join(sub_root,img)
            img = cv2.imread(_path)
            
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            Gaussian_img = cv2.GaussianBlur(gray, (3, 3), 0)  # 使用高斯滤波模糊图像  参数1:图片矩阵 参数2:卷积核 参数3:越大越模糊
            ret, thresh_img = cv2.threshold(Gaussian_img, 70, 255,
                                    cv2.THRESH_BINARY)  # 使用大津算法零阈值二值化经过高斯滤波模糊后的图像
            cv2.imwrite(_path + 'b.png', thresh_img)
            os.remove(_path)


