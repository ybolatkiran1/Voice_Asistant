import random
import os
import pygame
from gtts import gTTS

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio' + str(rand) + '.mp3'
    tts.save(file)

    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():  # Ses çalma bitene kadar bekle
        continue

    pygame.mixer.quit()
    os.remove(file)
