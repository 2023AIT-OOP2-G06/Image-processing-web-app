import datetime
import glob

from flask import Flask, request, render_template
import random  # ランダムデータ作成のためのライブラリ

app = Flask(__name__)

# 1. プロジェクトのトップ（じゃんけんアプリや、課題のアプリへのリンクを配置するだけ）


@app.route('/')
def index():
    return render_template('indax.html')

@app.route('/upload',methods=["GET"])
def upload():
    files = glob.glob("./images/upload/*")
    for file in files:
        print(file)



    return "ok"




if __name__ == '__main__':
    app.run()
