from flask import Flask, request, make_response, jsonify
from werkzeug.utils import secure_filename
from modules.whisper_model import Whisper_model

import os

UPLOAD_FOLDER = 'uploads/audio/convert/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_AS_ASCII'] = False

converter = Whisper_model()

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/upload/audio', methods=["POST"])
def upload_audio():
    try:
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        convert_result = converter.convert(UPLOAD_FOLDER + file.filename)
        original_text = convert_result['text']
        return make_response(jsonify({'original_text': original_text}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'upload failed.'}), 400)


if __name__ == '__main__':
    app.run(port=8881, debug=True, threaded=True)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)