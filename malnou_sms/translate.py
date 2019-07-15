from googletrans import Translator

def translator_init():
    return Translator()

def translate(Tref, message):
    return Tref.translate(message, dest='en')
