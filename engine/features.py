import threading
import time
import pygame
import eel 

@eel.expose
def playAssistantSound():
    def sound():
        music_dir = "www\\assets\\audio\\star_sound.wav"
        time.sleep(0.5)

        pygame.mixer.init()
        pygame.mixer.music.load(music_dir)
        pygame.mixer.music.play()

    threading.Thread(target=sound, daemon=True).start()
