import os
import shutil
"""
def move_files(source_dir, target_dir, start_num, end_num):
    # 创建目标目录（如果不存在）
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 移动文件
    for i in range(start_num, end_num + 1):
        source_file = os.path.join(source_dir, f"{i}.txt")
        target_file = os.path.join(target_dir, f"{i}.txt")
        # 如果源文件存在，则执行移动操作
        if os.path.exists(source_file):
            shutil.move(source_file, target_file)
            print(f"Moved {source_file} to {target_file}")
        else:
            print(f"Source file {source_file} does not exist")

# 源目录和目标目录的路径
source_directory = r'D:\pycharm\my_yolo\yolov7\my_datasets\labels\train'
target_directory = r'D:\pycharm\my_yolo\yolov7\my_datasets\labels\val'
# 要移动的文件范围
start_file_number = 20210001500
end_file_number = 20210001580

# 执行文件移动操作
move_files(source_directory, target_directory, start_file_number, end_file_number)

   """
#把1500到1580之间的作为验证集

#把1830到1900之间作为验证集

###################################
#下面是把某个目录下所有文件的文件路径输出到一个特定txxt里
###################################

def list_files(directory, output_file):
    # 打开文本文件，准备写入文件路径
    with open(output_file, 'w') as f:
        # 遍历目录中的所有文件和子目录
        for root, dirs, files in os.walk(directory):
            # 输出所有文件的绝对路径到文本文件
            for file in files:
                file_path = os.path.join(root, file)
                f.write(file_path + '\n')

# 指定目录的路径和输出文件的路径
directory_path = r'D:\pycharm\my_yolo\yolov7\my_datasets\images\val'
output_file_path = r'D:\pycharm\my_yolo\yolov7\my_datasets\val.txt'

# 调用函数将目录下所有文件的绝对路径写入到文本文件中
list_files(directory_path, output_file_path)

 #               """


#把1500到1580之间的作为验证集

#把1830到1900之间作为验证集