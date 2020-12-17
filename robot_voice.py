from gtts import gTTS 
import os
from playsound import playsound

text = "Bitte Nase abdecken"

speech = gTTS(text = text, lang = 'de', slow = False)
speech.save("nicht_richtig_tragen.mp3")
playsound("keine_maske.mp3")
