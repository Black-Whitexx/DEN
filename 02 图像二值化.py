import cv2
import os
import time

path = "G:/HWDB1.x/Gnt1.1Test_png"  # 原图所在文件夹
save_path = "G:/HWDB1.x/Gnt1.1Test_gray"  # 二值化后的图片存储路径
files = os.listdir(path)  # 获取原图所在文件夹中的文件
# print(files)

time_start = time.perf_counter()
for file in files:  # 遍历文件夹中的文件
    f_img = path + "/" + file  # 记录原图片路径
    save_path_img = save_path + "/" + file  # 记录剪裁后的图片存储路径
    GrayImage = cv2.imread(f_img, cv2.IMREAD_GRAYSCALE)  # 读取图片并转换为灰度图像数组
    Gaussian_img = cv2.GaussianBlur(GrayImage, (3, 3), 0)  # 使用高斯滤波模糊图像  参数1:图片矩阵 参数2:卷积核 参数3:越大越模糊
    ret, thresh_img = cv2.threshold(Gaussian_img, 0, 255,
                                    cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 使用大津算法零阈值二值化经过高斯滤波模糊后的图像
    cv2.imwrite(save_path_img, thresh_img)
time_end = time.perf_counter()
print("图片二值化用时：" + str(time_end - time_start) + "秒")  # 600秒左右
