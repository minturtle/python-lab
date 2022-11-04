from flask import Flask, request, make_response, jsonify
from werkzeug.utils import secure_filename
from convert_to_text import Converter
from flask_cors import CORS

import os

UPLOAD_FOLDER = 'uploads/audio/convert/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})



converter = Converter()

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/upload/audio', methods=["POST"])
def upload_audio():
    try:
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        original_text = converter.convert(UPLOAD_FOLDER + file.filename)
        return make_response(jsonify({'original_text': original_text}), 400)
    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'upload failed.'}), 400)


if __name__ == '__main__':
    app.run(port=8881, debug=True)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)