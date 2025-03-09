import ollama

import googletrans

import gtts 

import whisper

import warnings

print(googletrans.Translator().translate('', '').text)

gtts.gTTS('', lang='en').save('')

print(whisper.load_model("base").transcribe('')['text'])

warnings.filterwarnings("ignore")

print(ollama.chat("", [{"role": "user", "content": ""}]['message']['content']))
