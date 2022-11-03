import whisper
from transformers import PreTrainedTokenizerFast
from tokenizers import SentencePieceBPETokenizer
from transformers import BartForConditionalGeneration
import torch

class Converter:
    __whisper_model = None
    __model = None
    __tokenizer = None

    def __init__(self):
        self.__whisper_model = whisper.load_model("base")
        self.__tokenizer = self.__get_tokenizer()
        self.__model = self.__get_model()


    # whisper로 음성 파일 텍스트 추출
    def convert(self, audio_file):
        text_original = self.__whisper_model.transcribe("audio-ko.mp3")['text']
        return text_original

    #kobart로 텍스트 파일 요약
    def get_summary(self, text_original):
        model = self.__model
        tokenizer = self.__tokenizer

        raw_input_ids = tokenizer.encode(text_original)
        input_ids = [tokenizer.bos_token_id] + \
                    raw_input_ids + [tokenizer.eos_token_id]

        summary_ids = model.generate(torch.tensor([input_ids]),
                                     max_length=256,
                                     early_stopping=True,
                                     repetition_penalty=2.0)
        summary = tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
        print("요약 : " + summary)

    def __get_tokenizer(self):
        tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-summarization')
        return tokenizer


    def __get_model(self):
        model = BartForConditionalGeneration.from_pretrained('gogamza/kobart-summarization')
        model.eval()
        return model



converter = Converter()

original = converter.convert("audio-ko.mp3")
summary = converter.get_summary(original)

print(original, summary)