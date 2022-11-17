# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from modules.whisper_model import Whisper_model
from modules.kobart_model import Kobart_model
import uuid
from os import path

import json

convert_model = Whisper_model()
summary_model = Kobart_model()


def index(request):
    return create_response({"msg": "hello world!"}, "application/json")

#Whisper로 STT하는 API
def uploadSpeachToText(request):
    global create_response
    try:

        ## POST가 아닌 Request Method가 요청되었을 떄
        if request.method != 'POST':
            return create_response({"msg": "invalid request method"}, "application/json", 400)


        file = request.FILES.get("file")
        if(file == None):
            return create_response({"msg" : "no file uploaded"}, "application/json", 400)

        name,extension = path.splitext(file.name)

        fs = FileSystemStorage(location='uploads/audio', base_url='uploads/audio')
        filename = fs.save(str(uuid.uuid4()) + extension, file)
        convert_result = convert_model.convert(fs.url(filename))

        text_original = convert_result['text']
        language = convert_result['lang']

        ## STT 작업이 완료되었을 때
        return create_response({"original_text" : text_original, "language" : language} ,"application/json")


    ## 이외 예외가 터졌을 때
    except Exception as e:
        return create_response({"msg" : e}, "application/json", 400)


# Kobart로 요약하는 API
def getSummaryFromText(request):
    try:
        ## POST가 아닌 Request Method가 요청되었을 떄
        if request.method != 'POST':
            return create_response({"msg": "invalid request method"}, "application/json", 400)

        text_original = request.POST.get('text')
        language = request.POST.get('lang')

        if(text_original == None or language == None):
            return create_response({"msg": "no form data"}, "application/json", 400)
        if(language != "ko"):
            return create_response({"msg": "한글인 텍스트만 요약할 수 있습니다."}, "application/json", 400)

        text_summary = summary_model.get_summary(text_original)

        #요약 작업이 완료되었을 때
        return create_response({"summary_text": text_summary}, "application/json")


    except Exception as e:
        return create_response({"msg" : e}, "application/json", 400)



def create_response(body, content_type, status=200):
    return HttpResponse(json.dumps(body).encode('utf8'), content_type=content_type, status=status)