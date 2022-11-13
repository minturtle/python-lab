# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from modules.audio_converter import Converter
import uuid
from os import path

import json

converter = Converter()

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def fileUpload(request):
    try:
        if request.method == 'POST':
            file = request.FILES.get("file")
            if(file == None):
                return HttpResponse(json.dumps({"msg" : "no file uploaded"}).encode('utf8'), content_type="application/json", status=400)

            name,extension = path.splitext(file.name)

            fs = FileSystemStorage(location='uploads/audio', base_url='uploads/audio')
            filename = fs.save(str(uuid.uuid4()) + extension, file)
            convert_result = converter.convert(fs.url(filename))

            text_original = convert_result['text']
            language = convert_result['lang']

            #text_summary = converter.get_summary(text_original) if language == 'ko' else '한글만 요약이 가능합니다.'
            text_summary = "kobart 오류로 미구현"
            return HttpResponse(json.dumps({"original_text" : text_original, "summary_text" : text_summary}).encode('utf8'), content_type="application/json")
        return HttpResponse(json.dumps({"msg" : "invalid request method"}).encode('utf8'), content_type="application/json", status=400)
    except Exception as e:
        return HttpResponse(json.dumps({"msg" : e}), content_type="application/json", status=400)