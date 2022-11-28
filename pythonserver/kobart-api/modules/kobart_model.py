from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration
from tokenizers import SentencePieceBPETokenizer
import torch

class Kobart_model:

    __kobart_model = None
    __tokenizer = None

    def __init__(self):
        self.__tokenizer = self.__get_tokenizer()
        self.__kobart_model = self.__get_kobart_model()

    # kobart로 텍스트 파일 요약
    def get_summary(self, text_original):
        model = self.__kobart_model
        tokenizer = self.__tokenizer

        raw_input_ids = tokenizer.encode(text_original)
        input_ids = [tokenizer.bos_token_id] + \
                    raw_input_ids + [tokenizer.eos_token_id]

        summary_ids = model.generate(torch.tensor([input_ids]),
                                     max_length=256,
                                     early_stopping=True,
                                     repetition_penalty=2.0)
        summary = tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
        return summary

    def __get_tokenizer(self):
        tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-summarization')
        return tokenizer

    def __get_kobart_model(self):
        model = BartForConditionalGeneration.from_pretrained('gogamza/kobart-summarization')
        model.eval()
        return model