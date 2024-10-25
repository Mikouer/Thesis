import os
import pandas as pd
from sklearn.model_selection import train_test_split

# 文件名和标签的CSV文件路径
csv_file_path = "D:\\Garrus\\Thesis\\Coding\\names_labels.csv"

# 数据将被分为train和val的目录（相对路径）
train_dir = './Coding/images/train'
val_dir = './Coding/images/val'
labels_train_dir = './Coding/labels/train'
labels_val_dir = './Coding/labels/val'

# 创建必要的文件夹
os.makedirs(labels_train_dir, exist_ok=True)
os.makedirs(labels_val_dir, exist_ok=True)

# 加载CSV文件
data = pd.read_csv(csv_file_path)

# 将数据随机拆分为训练和验证集（80%训练，20%验证）
train, val = train_test_split(data, test_size=0.2, random_state=42)

# 创建YOLO格式的标注文件
def create_yolo_label_file(image_name, label, output_dir):
    # 设定中心位置和假设宽高为1.0（占据整个图像）
    class_id = 0 if label == 'donkey' else (1 if label == 'zebra' else 2)  # 假设驴是0，斑马是1，马是2
    x_center, y_center = 0.5, 0.5  # 中心坐标
    width, height = 1.0, 1.0  # 占据图像100%的宽度和高度
    
    # 文件路径
    txt_file_path = os.path.join(output_dir, f"{image_name}.txt")
    
    # 写入标注文件
    with open(txt_file_path, 'w') as f:
        f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

# 为训练集创建标注
for idx, row in train.iterrows():
    image_name = row['Name']# .replace(' ', '_')  # 替换空格
    label = row['Label']
    create_yolo_label_file(image_name, label, labels_train_dir)

# 为验证集创建标注
for idx, row in val.iterrows():
    image_name = row['Name']# .replace(' ', '_')  # 替换空格
    label = row['Label']
    create_yolo_label_file(image_name, label, labels_val_dir)

print("标注文件生成完成！")
