import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = os.path.expanduser('~/Downloads')
target_dirs = {
    os.path.expanduser('C:/Users/stepa/OneDrive/Pictures'): ['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mkv'],
    os.path.expanduser('C:/Users/stepa/OneDrive/Documents/PDFS'): ['pdf', 'txt'],
    os.path.expanduser('C:/Users/stepa/OneDrive/Documents/Word'): ['doc', 'docx'],
    os.path.expanduser('~/Downloads/Zipped'): ['zip', 'rar', 'tar', 'gz', '7z'],
    os.path.expanduser('~/Downloads/Executables'): ['exe', 'msi', 'bat', 'cmd', 'dll'],
    os.path.expanduser('C:/Users/stepa/OneDrive/Music'): ['mp3', 'wav', 'aac', 'flac', 'ogg', 'wma', 'm4a', 'opus'],
}


class Handler(FileSystemEventHandler):
    def process(self, event):
        # create the directories if needed
        for target_dir, extensions in target_dirs.items():
            os.makedirs(target_dir, exist_ok=True)

        # move files to corresponding directories
        for file in os.listdir(source_dir):
            file_path = os.path.join(source_dir, file)
            if os.path.isfile(file_path):
                file_extension = file.split('.')[-1].lower()
                for target_dir, extensions in target_dirs.items():
                    if file_extension in extensions:
                        shutil.move(file_path, os.path.join(target_dir, file))
                        break

    def on_modified(self, event):
        self.process(event)

def main():
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

main()