# import pandas as pd
# import os

# # Define your CSV file path and YOLO format output directory
# csv_file = 'FYP2/archive (3)/data.csv'
# output_dir = 'FYP2/archive (3)/original/labels'

# # Read CSV file into a pandas DataFrame
# df = pd.read_csv(csv_file)

# # Remove rows with NaN values in the relevant columns
# df.dropna(subset=['image_name', 'class_name', 'x_min', 'y_min', 'x_max', 'y_max'], inplace=True)

# # Create the output directory if it doesn't exist
# os.makedirs(output_dir, exist_ok=True)

# # Class mapping for YOLO format
# class_map = {'car': 0, 'bus': 1, 'truck': 2, 'cycle': 3}

# # Create YOLO format annotation files
# for index, row in df.iterrows():
#     filename = row['image_name']
#     img_width = 1920  # Update with your actual image width
#     img_height = 1080  # Update with your actual image height
#     class_name = row['class_name']
    
#     # Check for unexpected class names
#     if class_name not in class_map:
#         print(f"Unexpected class name: {class_name} at row {index}")
#         continue
    
#     x_min = row['x_min']
#     y_min = row['y_min']
#     x_max = row['x_max']
#     y_max = row['y_max']

#     # Calculate YOLO format values
#     x_center = (x_min + x_max) / 2.0 / img_width
#     y_center = (y_min + y_max) / 2.0 / img_height
#     width = (x_max - x_min) / img_width
#     height = (y_max - y_min) / img_height

#     # Get class ID from class_map
#     class_id = class_map[class_name]

#     # Create YOLO annotation file
#     txt_filename = os.path.join(output_dir, os.path.splitext(os.path.basename(filename))[0] + '.txt')

#     # Ensure the directory for the annotation file exists
#     os.makedirs(os.path.dirname(txt_filename), exist_ok=True)

#     with open(txt_filename, 'a') as f:
#         f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

# print("YOLO format annotation files created successfully.")

import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
original_img_dir = 'C:/Users/Hp/Desktop/UNIVERSITY/FYP/FYP2/archive (3)/original/imgs'
original_label_dir = 'C:/Users/Hp/Desktop/UNIVERSITY/FYP/FYP2/archive (3)/original/labels'
train_img_dir = 'YOLO/dataset/train/images'
train_label_dir = 'YOLO/dataset/train/labels'
val_img_dir = 'YOLO/dataset/val/images'
val_label_dir = 'YOLO/dataset/val/labels'

# Create directories if they don't exist
os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# Get list of all images and corresponding labels
all_images = os.listdir(original_img_dir)
all_labels = [f.replace('.jpg', '.txt') for f in all_images]

# Filter out images without corresponding labels
images_with_labels = [img for img in all_images if os.path.exists(os.path.join(original_label_dir, img.replace('.jpg', '.txt')))]
labels_with_images = [label for label in all_labels if os.path.exists(os.path.join(original_label_dir, label))]

# Split data into training and validation sets
train_images, val_images, train_labels, val_labels = train_test_split(
    images_with_labels, labels_with_images, test_size=0.2, random_state=42
)

# Function to move files to the respective directories
def move_files(image_list, label_list, img_dest, label_dest):
    for img, label in zip(image_list, label_list):
        shutil.copy2(os.path.join(original_img_dir, img), os.path.join(img_dest, img))
        shutil.copy2(os.path.join(original_label_dir, label), os.path.join(label_dest, label))

# Move the files
move_files(train_images, train_labels, train_img_dir, train_label_dir)
move_files(val_images, val_labels, val_img_dir, val_label_dir)

print('Data split into training and validation sets successfully!')

