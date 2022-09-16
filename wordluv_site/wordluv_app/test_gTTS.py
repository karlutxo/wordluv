# https://pypi.org/project/gTTS/

from gtts import gTTS


tts = gTTS("C'est l'ordinateur en parlant", lang='fr')
tts.save('voice.mp3')