import cv2
import os
import time
import numpy as np

img_length = 224
path = "./"  # 原图所在文件夹
for root, dirs, files in os.walk(path):
      for dir in dirs:
        print(dir)
        dir_path = os.path.join(root, dir)
        for sub_root, sub_dirs, sub_files in os.walk(dir_path):
          for img in sub_files:
            _path = os.path.join(sub_root,img)
            img = cv2.imread(_path)
            shape = max(img.shape)
            height, width = img.shape[:2]
            top = int((shape - height) / 2)
            bottom = shape - height - top
            left = int((shape - width) / 2)
            right = shape - width - left
            img = cv2.copyMakeBorder(img, top, bottom, left, right,
                             cv2.BORDER_CONSTANT, value=[255, 255, 255])
            res = cv2.resize(img, (img_length, img_length), interpolation=cv2.INTER_CUBIC)
            os.remove(_path)
            cv2.imwrite(_path + "+c.png", res)
            