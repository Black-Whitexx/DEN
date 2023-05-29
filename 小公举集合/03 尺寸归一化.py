import cv2
import os
import time

img_length = 224
path = "G:/HWDB1.x/Gnt1.1Test_gray"
save_path = "G:/HWDB1.x/Gnt1.1Test_size_new"
files = os.listdir(path)
time_start = time.perf_counter()
for file in files:
    f_img = path + "/" + file
    save_path_img = save_path + "/" + file
    img = cv2.imread(f_img)
    shape = max(img.shape)
    height, width = img.shape[:2]
    top = int((shape - height) / 2)
    bottom = shape - height - top
    left = int((shape - width) / 2)
    right = shape - width - left
    img = cv2.copyMakeBorder(img, top, bottom, left, right,
                             cv2.BORDER_CONSTANT, value=[255, 255, 255])
    res = cv2.resize(img, (img_length, img_length), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(save_path_img, res)
time_end = time.perf_counter()
print("图片尺寸归一化用时：" + str(time_end - time_start) + "秒")  # 800秒左右
