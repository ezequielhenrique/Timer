import pygame
import os


def resource_path(relative_path):
    import sys
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


sound_dir = resource_path('sound')


def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(sound_dir + '/alert.wav')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
