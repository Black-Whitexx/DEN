import os
import numpy as np
import struct
from PIL import Image
import time

data_dir = "G:/HWDB1.x/Gnt1.1Test"
dir_name = 'H:/dataset/png'
if not os.path.exists(dir_name):
    os.makedirs(dir_name)


def read_from_gnt_dir(gnt_dir=data_dir):
    def one_file(f):
        header_size = 10
        while True:
            header = np.fromfile(f, dtype='uint8', count=header_size)
            if not header.size: break
            sample_size = header[0] + (header[1] << 8) + (header[2] << 16) + (header[3] << 24)
            tagcode = header[5] + (header[4] << 8)
            tag = struct.pack('>H', tagcode).decode('gbk')
            width = header[6] + (header[7] << 8)
            height = header[8] + (header[9] << 8)
            if header_size + width * height != sample_size:
                break
            image = np.fromfile(f, dtype='uint8', count=width * height).reshape((height, width))
            yield image, tag

    for file_name in os.listdir(gnt_dir):
        if file_name.endswith('.gnt'):
            file_path = os.path.join(gnt_dir, file_name)
            with open(file_path, 'rb') as f:
                for image, tag in one_file(f):
                    file_name_no_endswith = file_name[:-6]
                    yield image, tag, file_name_no_endswith


counter = 0
gnt_counter = 1
file_name_no_endswith_old = ''
cut_img_num = 3200
cut_file_num = 1000
time_start = time.perf_counter()
for image, tag, file_name_no_endswith in read_from_gnt_dir(gnt_dir=data_dir):
    counter += 1
    im = Image.fromarray(image)
    if file_name_no_endswith_old != '':
        if file_name_no_endswith_old != file_name_no_endswith:  # 若文件名变化，则重新编号
            print("字符数 = ", counter - 1, "-", cut_img_num, "=", counter - 1 - cut_img_num)
            counter = 1
            print('第', gnt_counter, '个文件已读取')
            gnt_counter += 1
    file_name_no_endswith_old = file_name_no_endswith
    if counter > cut_img_num:
        im.convert('RGB').save(dir_name + '/' + file_name_no_endswith + '-' + str(counter) + '.png')
    if gnt_counter > cut_file_num:
        break
# print("字符数 = ", counter - 1, "-", cut_num, "=", counter - 1 - cut_num)
# print('以上为第', gnt_counter, '个文件')
print('Data transformation finished ...')
time_end = time.perf_counter()
print("文件读取用时：" + str(time_end - time_start) + "秒")  # 600秒左右
