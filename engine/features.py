import os
import re
import threading
import time
import pygame
import eel 
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

@eel.expose
def playAssistantSound():
    def sound():
        music_dir = "www\\assets\\audio\\star_sound.wav"
        time.sleep(0.5)

        pygame.mixer.init()
        pygame.mixer.music.load(music_dir)
        pygame.mixer.music.play()

    threading.Thread(target=sound, daemon=True).start()

def openCommand(query):
    query=query.replace("ASSISTANT_NAME","")
    query=query.replace("open","")
    query.lower()

    if query!="":
        speak("Opening "+query)
        os.system('start '+query)
    else:
        speak("Not found")    


def PlayYoutube(query):
    search_term=extract_yt_term(query)
    speak("Playing "+search_term+" on youtube")
    kit.playonyt(search_term)


def extract_yt_term(command):
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    match=re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None
