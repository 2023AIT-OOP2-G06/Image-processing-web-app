import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CustomHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.event_type == 'modified':
            print(f"File {event.src_path} has been modified")
            
class Main:
    # fileを常に読み込むコードを書いて、変更があったら、各画像処理を行うようにする。
    def run(self):
        pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
