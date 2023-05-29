import os
import sys

# 定义一个名字叫做rename的函数
def rename(filePath):
    # os.walk 查找文件
    for root, dirs, files in os.walk(filePath):
      for dir in dirs:
        print(dir)
        dir_path = os.path.join(root, dir)
        for sub_root, sub_dirs, sub_files in os.walk(dir_path):
            i = 0
            for fileName in sub_files:
              if fileName != sys.argv[0]:
                if fileName.endswith('jpg'):
                    os.rename(os.path.join(sub_root, fileName),os.path.join(sub_root, str(i)+'.png'))
                    i = i + 1


if __name__ == '__main__':
    filePath = R'./'
    rename(filePath)
