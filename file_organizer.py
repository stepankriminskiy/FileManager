import os
import shutil

# Define the source directory and the target directories
source_dir = os.path.expanduser('C:/Users/stepa/OneDrive/Desktop')
target_dirs = {
    os.path.expanduser('C:/Users/stepa/OneDrive/Desktop/Screenshots'): ['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mkv'],
    os.path.expanduser('C:/Users/stepa/OneDrive/Documents'): ['doc', 'docx', 'txt', 'pdf'],
}

# create the directories if needed
for target_dir, extensions in target_dirs.items():
    os.makedirs(target_dir, exist_ok=True)

# files in the source directory
files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

# move files to corresponding directories
for file in files:
    file_extension = file.split('.')[-1].lower()
    for target_dir, extensions in target_dirs.items():
        if file_extension in extensions:
            shutil.move(os.path.join(source_dir, file), os.path.join(target_dir, file))
            break

#reorganizing the downloads folder
source_dir = os.path.expanduser('~/Downloads')
target_dirs = {
    os.path.expanduser('C:/Users/stepa/OneDrive/Pictures'): ['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mkv'],
    os.path.expanduser('C:/Users/stepa/OneDrive/Documents'): ['doc', 'docx', 'txt', 'pdf'],
    os.path.expanduser('~/Downloads/Zipped'): ['zip', 'rar', 'tar', 'gz', '7z'],
    os.path.expanduser('~/Downloads/Executables'): ['exe', 'msi', 'bat', 'cmd', 'dll'],
    os.path.expanduser('~/Music'): ['mp3', 'wav', 'aac', 'ogg'],
}


# create the directories if needed
for target_dir, extensions in target_dirs.items():
    os.makedirs(target_dir, exist_ok=True)

# files in the source directory
files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

# move files to corresponding directories
for file in files:
    file_extension = file.split('.')[-1].lower()
    for target_dir, extensions in target_dirs.items():
        if file_extension in extensions:
            shutil.move(os.path.join(source_dir, file), os.path.join(target_dir, file))
            break

source_dir = os.path.expanduser('C:/Users/stepa/OneDrive/Documents')
target_dirs = {
    os.path.expanduser('C:/Users/stepa/OneDrive/Documents/Word'): ['doc', 'docx'],
    os.path.expanduser('C:/Users/stepa/OneDrive/Documents/PDFS'): ['pdf', 'txt'],
    os.path.expanduser('C:/Users/stepa/OneDrive/Media'): ['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mkv'],
    os.path.expanduser('C:/Users/stepa/OneDrive/Documents/Zipped'): ['zip', 'rar', 'tar', 'gz', '7z'],
}
# create the directories if needed
for target_dir, extensions in target_dirs.items():
    os.makedirs(target_dir, exist_ok=True)

# files in the source directory
files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

# move files to corresponding directories
for file in files:
    file_extension = file.split('.')[-1].lower()
    for target_dir, extensions in target_dirs.items():
        if file_extension in extensions:
            shutil.move(os.path.join(source_dir, file), os.path.join(target_dir, file))
            break

print("done moving")