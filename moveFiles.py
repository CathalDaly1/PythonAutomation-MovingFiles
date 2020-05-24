import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename.endswith("jpg") or filename.endswith("png") or filename.endswith("jpeg") or filename.endswith("tiff"):
                src = folder_to_track + "/" + filename
                new_destination = folder_destinationImages + "/" + filename
                os.rename(src, new_destination)

            if filename.endswith("pdf"):
                src = folder_to_track + "/" + filename
                new_destination = folder_destinationPDF + "/" + filename
                os.rename(src, new_destination)

            if filename.endswith("docx") or filename.endswith("doc"):
                src = folder_to_track + "/" + filename
                new_destination = folder_destinationWordDoc + "/" + filename
                os.rename(src, new_destination)


folder_to_track = "C:/Users/catha/Downloads"
folder_destinationImages = "C:/Users/catha/OneDrive/Desktop/Downloaded Images"
folder_destinationPDF = "C:/Users/catha/OneDrive/Desktop/Downloaded PDF Files"
folder_destinationWordDoc = "C:/Users/catha/OneDrive/Desktop/Downloaded Word Files"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
