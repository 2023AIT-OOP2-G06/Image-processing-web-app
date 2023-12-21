import sys
import os
import time
import logging
import cv2
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CustomHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.event_type == 'modified':
            print("jjjjjjjjjjjjj")
            print(f"File {os.path.basename(event.src_path)} has been modified")
            filename=os.path.basename(event.src_path)
            #filenameにファイルネーム入ってます
            #関数書いてく 

            #mozaiku


            # 顔検出インスタンス生成
            cascadePath = filename
            faceCascade = cv2.CascadeClassifier(cascadePath)

            ###############################
            # VideoCapture用インスタンス生成
            ###############################
            cap = cv2.VideoCapture(0)

            ###############################
            # 画像サイズをVGAサイズに変更する
            ###############################
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # 最小Windowサイズを定義
            minW = 0.1*cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            minH = 0.1*cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        ##### モザイクをかけるメソッド ######
            def mosaic(img,rect,size):
    # モザイクをかける領域を取得
                (x1,y1,x2,y2)=rect
                w=x2-x1
                h=y2-y1
                i_rect = img[y1:y2,x1:x2]
                # 一度縮小して拡大する
                i_small = cv2.resize(i_rect,(size,size))
                i_mos = cv2.resize(i_small,(w,h),interpolation=cv2.INTER_AREA)
                # モザイクに画像を重ねる
                img2=img.copy()
                img2[y1:y2,x1:x2]=i_mos
                return img2

            while True:
                # カメラから画像データ取得
                ret, img =cap.read()
                # グレースケールに変換
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                # 顔検出
                faces = faceCascade.detectMultiScale( 
                    gray,
                    scaleFactor = 1.2,
                    minNeighbors = 3,
                    minSize = (int(minW), int(minH)),
                    )

            # 顔検出箇所にモザイクをかけるためのループ
                for(x,y,w,h) in faces:
                    # モザイクをかける
                    img = mosaic(img,(x,y,x+w,y+h),10)

                # 画像表示
                    cv2.imshow('face mosaic',img) 

                

            # Do a bit of cleanup
        print("\n Exit Program")
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = CustomHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
