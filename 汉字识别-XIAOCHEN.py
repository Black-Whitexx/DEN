'''
Author: 小陈同学 85926966+XIAOCHEN-fun@users.noreply.github.com
Date: 2023-05-19 16:23:23
LastEditors: 小陈同学 85926966+XIAOCHEN-fun@users.noreply.github.com
LastEditTime: 2023-05-19 17:02:45
FilePath: \DEN\汉字识别-XIAOCHEN.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2 as cv
import os
import numpy as np
DATASTE_PATH = "./Datasets/confirm"
ORI_PATH = "./picture"

PATH = './Datasets/confirm'
img_ori = []
kernel = np.ones((3, 3), np.uint8)

def read_img(path):
  for root, dirs, files in os.walk(path):
    for file in files:
        img_ori.append(cv.imread(os.path.join(root,file)))

def main(): 
  read_img(PATH)
  for img in img_ori:
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.adaptiveThreshold(img, 255, 0, 1, 5, 10)
    img = cv.erode(img, kernel)
    img = cv.dilate(img, kernel, iterations=1)
    
    #contours= cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #img= cv.drawContours(img, contours, -1, (0, 255, 0), 2)
    cv.imshow('img',img)
    cv.waitKey(0)

 
if __name__ == '__main__':
    main()