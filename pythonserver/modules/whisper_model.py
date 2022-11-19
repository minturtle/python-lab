import whisper
import torch
import sys


class Whisper_model:
    __whisper_model = None
    __kobart_model = None
    __tokenizer = None

    def __init__(self):
        self.__whisper_model = self.__get_whisper_model("base")

    def __get_whisper_model(self, model_name):
        return whisper.load_model(model_name)

    # whisper로 음성 파일 텍스트 추출
    def convert(self, audio_file):
        result = self.__whisper_model.transcribe(audio_file)
        text_original = result['text']
        language = result['language']
        return {"text" : text_original, "lang" : language}



if __name__ == "__main__":
    converter = Converter()
    print(converter.convert(sys.argv[1]))
