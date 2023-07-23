import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/VihanPC/Downloads"              # Add the path of you "Downloads" folder.



dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Handler Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey {event.src_path} has been Created")

    def on_deleted(self, event):
        print(f"Hey {event.src_path} has been Deleted")
        
    def on_modified(self, event):
        print(f"Hey {event.src_path} has been Modifed")

    def on_moved(self, event):
        print(f"Hey {event.src_path} has been Moved")
        
        

        
# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()

