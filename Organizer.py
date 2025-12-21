import os
import shutil

# --- CONFIGURATION ---
# PASTE YOUR PATH HERE AGAIN
folder_path = "/Users/ams/Downloads"

# --- STEP 1: Create the subfolders ---
# Added "Sheets" and "Videos" to this list
target_folders = ["Images", "Documents", "Sheets", "Videos", "Others"]

for folder in target_folders:
    path_to_create = os.path.join(folder_path, folder)
    if not os.path.exists(path_to_create):
        os.makedirs(path_to_create)
        print(f"Created new folder: {folder}")

# --- STEP 2: The Sorting Loop ---
files = os.listdir(folder_path)

for file in files:
    # Skip the folders themselves and hidden files
    if file in target_folders or file.startswith("."):
        continue

    filename, extension = os.path.splitext(file)
    extension = extension.lower()

    # Default destination
    destination_folder = "Others"

    # --- THE NEW LOGIC ---
    if extension in [".jpg", ".jpeg", ".png", ".gif", ".svg", ".heic", ".webp"]:
        destination_folder = "Images"
    
    elif extension in [".mp4", ".mov", ".avi", ".mkv", ".webm"]:
        destination_folder = "Videos"
        
    elif extension in [".csv", ".xlsx", ".xls", ".numbers"]:
        destination_folder = "Sheets"
        
    elif extension in [".pdf", ".docx", ".txt", ".pptx", ".doc"]:
        destination_folder = "Documents"
    
    # --- MOVE IT ---
    source_path = os.path.join(folder_path, file)
    destination_path = os.path.join(folder_path, destination_folder, file)

    try:
        shutil.move(source_path, destination_path)
        print(f"Moved: {file} ---> {destination_folder}")
    except Exception as e:
        print(f"Error moving {file}: {e}")

print("Organizer run complete!")