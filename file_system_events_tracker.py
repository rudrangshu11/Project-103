import os
import random
import shutil
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from_dir = "C:/Users/Rakhi/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created...")

    def on_deleted(self, event):
        print(f"{event.src_path} has been deleted...")

    def on_modified(self, event):
        print(f"{event.src_path} has been modified...")
    
    def on_moved(self, event):
        print(f"{event.src_path} has been moved...")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(5)
        print("Your program is running")

except KeyboardInterrupt:
    print("Stopped...")
    observer.stop()