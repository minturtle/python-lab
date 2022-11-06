from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from modules.audio_converter import Converter

import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def fileUpload(request):
    converter = Converter()
    if request.method == 'POST':

        file = request.FILES["file"]
        fs = FileSystemStorage(location='uploads/audio', base_url='uploads/audio')
        filename = fs.save(file.name, file)
        convert_result = converter.convert(fs.url(filename))

        text_original = convert_result['text']
        language = convert_result['lang']

        text_summary = converter.get_summary(text_original) if language == 'ko' else '한글만 요약이 가능합니다.'
        return HttpResponse(json.dumps({"original_text" : text_original, "summary_text" : text_summary}).encode('utf8'), content_type="application/json")
    return HttpResponse(json.dumps({"msg" : "invalid request"}).encode('utf8'), content_type="application/json", status=400)