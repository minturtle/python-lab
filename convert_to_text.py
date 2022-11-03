import whisper
from transformers import PreTrainedTokenizerFast
from tokenizers import SentencePieceBPETokenizer
from transformers import BartForConditionalGeneration
import torch

#whisper로 음성 파일 텍스트 추출
whisper_model = whisper.load_model("base")

text_original = whisper_model.transcribe("audio-ko.mp3")['text']
print("원문 : " + text_original)


#kobart로 텍스트 파일 요약
def tokenizer():
    tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-summarization')
    return tokenizer


def get_model():
    model = BartForConditionalGeneration.from_pretrained('gogamza/kobart-summarization')
    model.eval()
    return model


model = get_model()
tokenizer = tokenizer()

raw_input_ids = tokenizer.encode(text_original)
input_ids = [tokenizer.bos_token_id] + \
            raw_input_ids + [tokenizer.eos_token_id]

summary_ids = model.generate(torch.tensor([input_ids]),
                     max_length=256,
                     early_stopping=True,
                     repetition_penalty=2.0)
summary = tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
print("요약 : " + summary)
