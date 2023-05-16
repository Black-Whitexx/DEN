import glob
import numpy as np
import cv2
import os
import time


all_imgs_path = glob.glob(r'G:\HWDB1.x\Gnt1.1Test_size_new\*.png')
f_path = "G:/HWDB1.x/Gnt1.1Test_size_new"
files = os.listdir(f_path)
species = ['0001']
file_label_0 = '0001'
for file in files:
    file_label = file[:4]
    if file_label != file_label_0:
        species.append(file_label)
        file_label_0 = file_label
species_to_id = dict((c, i) for i, c in enumerate(species))
print(species_to_id)
all_labels = []
for img in all_imgs_path:
    for i, c in enumerate(species):  # 区分出每个img，应该属于什么类别
        if c in img:
            all_labels.append(i)

# 划分测试集和训练集
index = np.random.permutation(len(all_imgs_path))
all_imgs_path = np.array(all_imgs_path)[index]
all_labels = np.array(all_labels)[index]
# 80%的样本作为训练集
s = int(len(all_imgs_path) * 0.8)
print("训练集取", s, "张图片")
train_imgs = all_imgs_path[:s]
train_labels = all_labels[:s]
test_imgs = all_imgs_path[s + 1:]
test_labels = all_imgs_path[s + 1:]

start = time.time()
save_path = "G:/HWDB1.x/Datasets"
mod = 'train'
count = 0
for file in all_imgs_path:
    if count > s:
        mod = 'test'
    save_path_img = save_path + '/' + mod
    if not os.path.exists(save_path_img):
        os.makedirs(save_path_img)
    save_path_img = save_path_img + '/' + str(all_labels[count])
    if not os.path.exists(save_path_img):
        os.makedirs(save_path_img)
    save_path_img = save_path_img + '/' + file[31:]
    img = cv2.imread(file)
    cv2.imwrite(save_path_img, img)
    count += 1
print("创建数据集所用时间: {:.4f}秒".format(time.time() - start))
