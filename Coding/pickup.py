import os
import shutil



# 定义路径
source_folder = './Coding/labels/train'  # 包含文件名的文件夹
target_folder = './Coding/donkeys-horses-zebra-images-dataset/test/donkey'  # 查找同名文件的目标文件夹
output_folder = 'D:/Garrus/Thesis/Coding/images/train'  # 存放提取文件的新文件夹

# 创建输出文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 获取源文件夹内的文件名（去除扩展名）
source_files = {os.path.splitext(file)[0] for file in os.listdir(source_folder)}

# 遍历目标文件夹，查找同名文件
for file in os.listdir(target_folder):
    # 使用 os.path.splitext() 确保下划线不被移除
    file_name, file_ext = os.path.splitext(file)
    # 保证下划线没有被替换
    if file_name in source_files:
        # 如果找到同名文件，复制到新的文件夹中
        source_path = os.path.join(target_folder, file)
        destination_path = os.path.join(output_folder, file)
        shutil.copy2(source_path, destination_path)

print("文件提取完成！")
