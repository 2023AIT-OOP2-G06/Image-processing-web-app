import cv2

class generate_grayscale:
    def run(self, filename):
        #読み込み先の取得
        pass_name = 'images/upload/' + filename
        #画像生成
        img = cv2.imread(pass_name)
        #グレースケール化
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #画像の保存
        cv2.imwrite('images/edit/grayscale_' + filename, img_gray)
        
if __name__ == "__main__":
    sample = generate_grayscale()
    sample.run('iconfinder-server-4417119_116634.png')
