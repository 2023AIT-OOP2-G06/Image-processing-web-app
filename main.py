import datetime
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploaded_images'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/upload/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        # ファイルがリクエストに含まれていない場合の処理
        return 'No file part'

    file = request.files['file']
    print(file)

    if file.filename == '':
        # ファイルが選択されていない場合の処理
        return 'No selected file'

    # ファイルを保存するディレクトリを指定
    upload_folder = './images/upload'
    
    # ディレクトリが存在しない場合は作成
    os.makedirs(upload_folder, exist_ok=True)

    # ファイルを保存
    file.save(os.path.join(upload_folder, file.filename))

    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)