from googletrans import Translator
from gtts import gTTS
import pyttsx3

# Input English text
english_text = input("Enter English text: ")

# Translate English to Kannada
translator = Translator()
translated = translator.translate(english_text, src='en', dest='kn')
kannada_text = translated.text
print("Translated Text in Kannada:", kannada_text)

# Speak Kannada text using pyttsx3 (offline)
engine = pyttsx3.init()

# Set language to Kannada (Windows voices usually handle UTF-8 text)
engine.setProperty('rate', 150)  # speech speed
engine.say(kannada_text)
engine.runAndWait()