import cv2
import os
import numpy as np
import time

def cut(path):
  img= cv2.imread(path)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#gray
  gaussian_img = cv2.GaussianBlur(gray, (5, 5), 0)
  ret, binary = cv2.threshold(gaussian_img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU);#binary
  kernel1 = np.ones((3, 3), np.uint8)
  eroded_img = cv2.erode(binary, kernel1, iterations=2)
  kernel2 = np.ones((9, 9), np.uint8)
  dilated_img = cv2.dilate(eroded_img, kernel2, iterations=4)
  contours, hierarchy = cv2.findContours(dilated_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


  rects = [cv2.boundingRect(cnt) for cnt in contours]
  i=0 
  for rect in rects:
    x, y, w, h = rect
    if(w > 90 and h > 90 and w < 200 and h<200):
      #cv2.circle(img, (int(x+w/2), int(y+h/2)), int(max(w,h)/2), (0, 0, 255), 2)
      #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
      crop_img = img[y:y+h, x:x+w]
      i = i + 1
      cv2.imwrite(path + str(i) + '.jpg' ,crop_img)
      

if __name__ == '__main__':
  print('daaa')
  filePath = './'
  for root, dirs, files in os.walk(filePath):
      for dir in dirs:
        dir_path = os.path.join(root, dir)
        for sub_root, sub_dirs, sub_files in os.walk(dir_path):
            for image in sub_files:
              path = os.path.join(sub_root,image)
              cut(path)
              os.remove(path)
              