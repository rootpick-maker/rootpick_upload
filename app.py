

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return "RootPick Upload Server is Running!"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 200

# gunicorn용 Flask 인스턴스 노출
application = app

# 아래는 로컬 테스트용. Render에서는 사용 안 함.
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=10000)
