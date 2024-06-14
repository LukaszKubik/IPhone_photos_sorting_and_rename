import os
import shutil

# Providing path to main folder with photos subfolders
print("Please input photo folders path")
main_folder = input()

# File formats to process
file_formats = ['.jpg','.JPEG', '.HEIC', '.PNG']

# Function to change file name accorrding to new scheme
def rename_and_move_file(file_path, new_name, main_folder):
    extension = os.path.splitext(file_path)[1]
    new_file_name = f"{new_name}{extension}"
    new_file_path = os.path.join(main_folder, new_file_name)

    # Moving file
    shutil.move(file_path, new_file_path)
    return new_file_path

# Loop by subfolders
for root, dirs, files in os.walk(main_folder, topdown=False):
    for file in files:
        if any(file.endswith(format) for format in file_formats):
            # Gathering subfolder name (format: yyyymm__)
            folder_name = os.path.basename(root)
            if len(folder_name) >= 6:
                year = folder_name[:4]
                month = folder_name[4:6]
                new_name = f"{year}-{month} {os.path.splitext(file)[0]}"
                file_path = os.path.join(root, file)
                new_file_path = rename_and_move_file(file_path, new_name, main_folder)
                print(f"Renamed and moved: {file_path} -> {new_file_path}")

    # Deleting empty subfolders
    if not os.listdir(root):
        os.rmdir(root)
        print(f"Removed empty folder: {root}")