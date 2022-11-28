import json

from flask import Flask, request, make_response, jsonify
from modules.kobart_model import Kobart_model

import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


summary_model = Kobart_model()

@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/summarization", methods=["POST"])
def summaryzation():
    params = json.loads(request.get_data(), encoding='utf-8')

    summary_txt = summary_model.get_summary(params["text"])


if __name__ == '__main__':
    app.run(port=8882, debug=True, threaded=True)