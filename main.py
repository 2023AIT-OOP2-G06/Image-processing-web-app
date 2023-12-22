from flask import Flask, render_template
import os
import glob

app = Flask(__name__)

app = Flask(__name__, static_url_path='/images')

IMG_LIST = os.listdir("./images/upload")
IMG_FOLDER = os.path.join("./images/upload", "file")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload',methods=["GET"])
def upload():
    files = glob.glob("./images/upload/*")
    for file in files:
          print(file)

    IMG_LIST = os.listdir("./images/upload")

    IMG_FOLDER = os.path.join("./images/upload", "file")
    print(IMG_FOLDER)

    app.config["UPLOAD_FOLDER"] = IMG_FOLDER

    return "ok"




if __name__ == "__main__":
    app.run(debug=True)